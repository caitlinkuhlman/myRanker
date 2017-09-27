from flask import Flask, render_template
from subprocess import call
import threading
import os

app = Flask(__name__)
cwd = os.getcwd()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<ref>')
def landingPageRef(ref):
    return render_template(ref)

def startupLineUp():
    print("Starting Lineup...")
    directory = cwd + '/Lineup' #running through terminal
    #directory = '/Users/Toki/Desktop/myRanker' #running through PyCharm (for me :P)
    call('npm run start:lineup_demos_source', cwd=directory, shell=True)


def startupServer():
    print("Starting server...")
    app.run(port=5000, threaded=True)

def main():

    lineupThread = threading.Thread(target=startupLineUp)
    lineupThread.start()

    serverThread = threading.Thread(target=startupServer)
    serverThread.start()


if __name__ == '__main__':
    main()

