import numpy as np
import pandas as pd

import pyximport
pyximport.install()
from rankit.build.rank_script.rlscore.learner import PPRankRLS
from math import log10, floor


# WE use the RLS library.
# Tutorial:
# # http://staff.cs.utu.fi/~aatapa/software/RLScore/tutorial_ranking.html#tutorial-3-learning-from-pairwise-preferences
# 
# pairfile format:
# 
# obj1,obj2,label
# 
# $label \in \{-1, 1\}$


def normalize(df):
    return(df - df.mean()) / df.std()

def scale(df):
    return(100 * (df - df.min()) / (df.max() - df.min()))

# def clean_dataset(dataset, primary_key):
#     cleaned_dataset = dataset.select_dtypes([np.number]).copy()
#     cleaned_dataset[primary_key] = dataset[primary_key]
#     return cleaned_dataset

def clean_dataset(dataset, primary_key):
    #   temp make primary key index so it doesn't get converted
    dataset.set_index(primary_key, inplace=True)
    cleaned_dataset = pd.get_dummies(dataset)
    cleaned_dataset.reset_index(inplace=True)
    return cleaned_dataset


def build(dataset, pairs, primary_key = 'Title', rank = 'Rank') :
    pair_indices = pairs["high"].append(pairs["low"]).drop_duplicates().values
    dataset = clean_dataset(dataset, primary_key)

    data_train = dataset.iloc[pair_indices]

    data = np.nan_to_num(dataset.drop(primary_key, axis=1))
    X = np.nan_to_num(data_train.drop(primary_key, axis=1))
    # print X
    pairs_start = []
    pairs_end = []
    # put pair data into format for RLS learner
    for i in range(len(pairs)):
        a = pairs.iloc[i]
        indx1 = np.where(pair_indices == a["high"])[0][0]
        indx2 = np.where(pair_indices == a["low"])[0][0]
        pairs_start.append(indx1)
        pairs_end.append(indx2)

    # train learner on pair data
    learner = PPRankRLS(X, pairs_start, pairs_end)
    y_pred = learner.predict(data)
    weights = learner.predictor.W

    res = pd.DataFrame()

    res['Prediction'] = y_pred
    res = res.rank(ascending=False)

    dataset[rank] = res['Prediction']
    return dataset




