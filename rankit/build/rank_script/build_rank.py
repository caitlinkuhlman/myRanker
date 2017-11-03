import numpy as np
import pandas as pd

import pyximport
pyximport.install()
from rankit.build.rank_script.rlscore.learner import PPRankRLS



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

def build(dataset, pairs) :
    pair_indices = pairs["high"].append(pairs["low"]).drop_duplicates().values
    data_train = dataset.iloc[pair_indices]

    data = np.nan_to_num(dataset.drop('States', axis=1))
    X = np.nan_to_num(data_train.drop('States', axis=1))
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
    res['State'] = dataset['States']
    res['Prediction'] = y_pred
    res.set_index('State', inplace=True)
    res = res.rank()

    return res




