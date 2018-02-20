import os, json

import  rankit.build.rank_script.build_rank as build_rank
import  pandas as pd


primary_key = 'Title'
rank = 'Rank'


# Return the full dataset
def getDataset(dataset_name):
    # get the absolute path of the dataset

    datasets_dir = os.path.dirname(os.path.abspath(os.path.dirname(__name__)) + "/rankit/datasets/")
    print(datasets_dir)
    abs_file_path = os.path.join(datasets_dir, dataset_name+".json")

    # load the json file contents into json object
    with open(abs_file_path, 'r') as data_file:
        datastore = json.load(data_file)
    return datastore

def filterByPrimaryKey(datastore):
    #filter only object names
    datastore_ids = list(map(lambda data: data[primary_key], datastore))
    datastore_ids.sort()

    return datastore_ids


def getRanking(dataset_name, primaryKeyPairs):

    # get the dataset from json file in list format
    dataset_list = getDataset(dataset_name)
    # convert each primary key into index in pairs sent from client
    primaryKeyToIndex(dataset_list, primaryKeyPairs)

    pairs_json = json.dumps(primaryKeyPairs)
    pairs = pd.read_json(pairs_json)

    dataset = pd.read_json(json.dumps(dataset_list))

    rank, weights = build_rank.build(dataset=dataset, pairs=pairs)
    return rank.to_json(orient='records'), weights

def primaryKeyToIndex(dataset_list, primaryKeyPairs):
    for obj in primaryKeyPairs:
        for key in obj:
            # obj[high], obj[low]
            primKey = obj[key]
            index = findIndex(primKey, dataset_list)
            obj[key] = index


def findIndex(primKey, dataset_list):
    index = 0
    for list_entry in dataset_list:
        if list_entry[primary_key] == primKey:
            return index
        else:
            index = index + 1