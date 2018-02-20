import os, json

# Return the full dataset
def getDataset(dataset_name):
    # get the absolute path of the dataset

    datasets_dir = os.path.dirname(os.path.abspath(os.path.dirname(__name__)) + "/rankit/datasets/static/")
    abs_file_path = os.path.join(datasets_dir, dataset_name+".json")

    # load the json file contents into json object
    with open(abs_file_path, 'r') as data_file:
        datastore = json.load(data_file)
    return datastore