from flask import Flask, render_template, request, url_for
from subprocess import call
import threading
import os
import logging, sys

app = Flask(__name__)
cwd = os.getcwd()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/login')
def login():
    return render_template('modal_log_in.html')

@app.route('/dataset')
def processDataset():
    dataset_name = request.args.lists()

    # dataset_name.get('dataset_name', default=-1, type="")
    dataset_name = list(dataset_name)
    # dataset_name = dataset_name.get('dataset_name', default=-1, type="")

    print("Dataset : %s  " % dataset_name)
    return 'ok'

@app.route('/favicon.ico/')
def linedupDaependency(): #TODO clean up code
   try:
       return url_for('static', filename='lineup/favicon.ico')
   except Exception as e:
       return str(e)

def startupLineUp():
    logging.info("Starting Lineup...")
    directory = cwd + '/Lineup' #running through terminal
    # call('npm run start:lineup_demos_source', cwd=directory, shell=True)


def startupServer():
    logging.info("Starting server...")
    app.run(port=5000, threaded=True)

def main():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    lineupThread = threading.Thread(target=startupLineUp)
    lineupThread.start()

    serverThread = threading.Thread(target=startupServer)
    serverThread.start()


if __name__ == '__main__':
    main()
