
# coding: utf-8

# In[1]:

import itertools
import json
import numpy as np
from scipy import stats
import pylab as pl
from sklearn import svm, linear_model, cross_validation
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn import linear_model
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import ElasticNetCV
from sklearn.cross_validation import train_test_split
from sklearn import cross_validation
from sklearn import grid_search
from sklearn import metrics
from learning2rank.rank import RankNet
import pyximport
pyximport.install()
from rankit.build.rank_script.rlscore.learner import PPRankRLS
from rankit.build.rank_script.rlscore.measure import cindex


# In[2]:

def validate_10(message, estimator, X, y):
    print(message)
    count=0
    for i in range(10):
        kfold = cross_validation.KFold(len(X), n_folds=5, shuffle=True)
        scores = cross_validation.cross_val_score(estimator, X, y, cv=kfold, n_jobs=-1, scoring='r2' )
        score=np.average(scores)
        #print(i, score)
        count += score
    avg_score = count/10
    print("Averge R2 score: ", avg_score)
    
def normalize(df):
    return(df - df.mean()) / df.std()

def scale(df):
    return(100 * (df - df.min()) / (df.max() - df.min()))

def clean_data(data):
    data.sort_index(inplace=True)
    for col in data.columns:
        data[col] = data[col].str.replace(r',', '')
        data[col] = data[col].str.replace(r'$', '')
        data[col] = data[col].str.replace(r'%', '')
    data.set_index('States', inplace=True)
    data.sort_index(inplace=True)
#     data = normalize(data)
#     data.fillna(value = 0, inplace=True)


# In[3]:

def load_matters_data():
    #load data
    data = pd.read_csv("matters_indices_2014.csv")
    cost_data = pd.read_csv("cost_metrics_2014.csv")
    tax_data = pd.read_csv("tax_metrics_2014.csv")
    quality_data = pd.read_csv("quality_metrics_2014.csv")
    talent_data = pd.read_csv("talent_metrics_2014.csv")
    
    #drop metrics with missing data
    cost_data.drop(['State Spending Per Capita', 'State and Local Debt Per Capita', 'State Highway Cost Per Mile'], axis=1, inplace=True)
    talent_data.drop(['Tech Employment as Percent of Total Employment', 'Total Tech Employment', 'STEM-related Bachelors Degrees Awarded','Percentage of Workforce with Bachelors Degree or Higher','STEM Degrees per Capita'], axis=1, inplace=True)
    tax_data.drop(['State and Local Tax Burden Per Capita in $', 'State and Local Tax Burden as Percent of Personal Income', 'Research and Development Tax Credit Refundability Rate','Corporate Income Tax-Sourcing Rules','Corporate Income Tax-Apportionment Method','Research and Development Tax Credit Rate','Research and Development Tax Credit ASC Rate'], axis=1, inplace=True)
    quality_data.drop(['8th Grade Student Performance Science', '8th Grade Student Performance Math', 'School Quality', '4th Grade Student Performance Science', '8th Grade Student Performance Reading','4th Grade Student Performance Math'], axis=1, inplace=True)

    #clean data
    clean_data(cost_data)
    clean_data(talent_data)
    clean_data(tax_data)
    clean_data(quality_data)

    #get df with only cost index metrics
    cost_perfect = cost_data[['Retail Price of Electricity', 'Median Earnings', 'Average Family Health Insurance Premium', 'UI Premium Per Employee']]

    #get index values
    data.set_index('States', inplace=True)
    data.sort_index(inplace=True)
    cost_labels = data['MATTERS Cost of Doing Business Index']

    all_data = pd.concat([cost_data, talent_data, tax_data, quality_data, cost_labels], axis=1, join='inner')
    all_data = all_data.convert_objects(convert_numeric=True)
    all_data.drop('United States', axis=0, inplace=True)
    
    return all_data


# In[ ]:
#RLS implementation:
# http://staff.cs.utu.fi/~aatapa/software/RLScore/tutorial_ranking.html#tutorial-3-learning-from-pairwise-preferences


def cv_rls(X, y):
    #Trains RLS with default parameters (regparam=1.0, kernel='LinearKernel')
    kfold = cross_validation.KFold(len(X), n_folds=5, shuffle=True)

    avg_cindex = 0
    avg_tau = 0
    for train, test in kfold:
        
        get_pairs(X[train], y)
        learner = PPRankRLS(X_train, pairs_start, pairs_end)
        #Test set predictions
        y_pred = learner.predict(X[test])
        avg_cindex += cindex(y[test], y_pred)
        avg_tau += stats.kendalltau(y_compute[test], y_pred)[0]
        
    print("Average cindex score: %f" %(avg_score/5))
    print("Average tau score: %f" %(avg_tauS/5))
    


# In[4]:

def get_pairs(X, y):
    pairs_start = []
    pairs_end = []
    for i in range(len(X)):
        for j in range(len(X)):
            if y[i] > y[j]:
                pairs_start.append(i)
                pairs_end.append(j)
            elif y[i] < y[j]:
                pairs_start.append(j)
                pairs_end.append(i)

                
                
#compare pairwise RLS ranking to linear regression model 
def score_models(X, y):
       
    #cindex
    pairs_cindex = 0
    reg_cindex = 0
    lr_cindex = 0
    #tau
    pairs_tau = 0
    reg_tau = 0
    lr_tau = 0
    #r2
    pairs_r2 = 0
    reg_r2 = 0
    lr_r2 = 0
    
    for i in range(10):
        
        kfold = cross_validation.KFold(len(X), n_folds=5, shuffle=True)
 
        for train, test in kfold:
            pairs_start, pairs_end = get_pairs(X[train], y[train])
            learner = PPRankRLS(X[train], pairs_start, pairs_end)
            reg = GlobalRankRLS(X[train], y[train])
            lr_estimator = linear_model.LinearRegression(fit_intercept=True)
            lr_estimator.fit(X[train], y[train])

            #Test set predictions
            y_pred = learner.predict(X[test])
            reg_pred = reg.predict(X[test])
            lr_pred = lr_estimator.predict(X[test])

            #cindex
            pairs_cindex += cindex(y_compute[test], y_pred)
            reg_cindex += cindex(y_compute[test], reg_pred)
            lr_cindex += cindex(y_compute[test], lr_pred)
            #tau
            pairs_tau += stats.kendalltau(y_compute[test], y_pred)[0]
            reg_tau += stats.kendalltau(y_compute[test], reg_pred)[0]
            lr_tau += stats.kendalltau(y_compute[test], lr_pred)[0]
            #r2
            pairs_r2 += metrics.r2_score(y_compute[test], y_pred)
            reg_r2 += metrics.r2_score(y_compute[test], reg_pred)
            lr_r2 += metrics.r2_score(y_compute[test], lr_pred)
        
    print('Cindex score:')
    print("RLS: %.5f" % (pairs_cindex/50))
    print("Reg: %.5f" % (reg_cindex/50))
    print("Lr: %.5f" % (lr_cindex/50))
    
    print('\nTau score:')   
    print("RLS: %.5f" % (pairs_tau/50))
    print("Reg: %.5f" % (reg_tau/50))
    print("Lr: %.5f" % (lr_tau/50))
          
    print('\nr2 score:') 
    print("RLS: %.5f" % (pairs_r2/50))
    print("Reg: %.5f" % (reg_r2/50))
    print("Lr: %.5f" % (lr_r2/50))
    
    
    
#vary number of state pairs to train on and evaluate RLS and linear regression
def eval_num_pairs(X, y):
    
    for i in [24, 16, 12, 8, 6, 4, 3, 2]:
        
        print("\n FOLDS = %i" %(i))
        print("INSTANCES = %i" %(48/i))
        print("PAIRS = %i" %(comb(48/i, 2)*2))
        
        #cindex
        pairs_cindex = 0
        lr_cindex = 0
        #tau
        pairs_tau = 0
        lr_tau = 0
        #r2
        pairs_r2 = 0
        lr_r2 = 0
    
        for j in range(10):
            kfold = cross_validation.KFold(len(X), n_folds=i, shuffle=True)
            for train, test in kfold:
                #train on smaller test set
                pairs_start, pairs_end = get_pairs(X[test], y[test])
                learner = PPRankRLS(X[test], pairs_start, pairs_end)
                lr_estimator = linear_model.LinearRegression(fit_intercept=True)
                lr_estimator.fit(X[test], y[test])

                #predict on larger training set
                y_pred = learner.predict(X[train])
                lr_pred = lr_estimator.predict(X[train])

                #cindex
                pairs_cindex += cindex(y_compute[train], y_pred)
                lr_cindex += cindex(y_compute[train], lr_pred)
                #tau
                pairs_tau += stats.kendalltau(y_compute[train], y_pred)[0]
                lr_tau += stats.kendalltau(y_compute[train], lr_pred)[0]
                #r2
                pairs_r2 += metrics.r2_score(y_compute[train], y_pred)
                lr_r2 += metrics.r2_score(y_compute[train], lr_pred)
        
        print('Cindex score:')
        print("RLS: %.5f" % (pairs_cindex/(i*10)))
        print("Lr: %.5f" % (lr_cindex/(i*10)))

        print('\nTau score:')   
        print("RLS: %.5f" % (pairs_tau/(i*10)))
        print("Lr: %.5f" % (lr_tau/(i*10)))

        print('\nr2 score:') 
        print("RLS: %.5f" % (pairs_r2/(i*10)))
        print("Lr: %.5f" % (lr_r2/(i*10)))


