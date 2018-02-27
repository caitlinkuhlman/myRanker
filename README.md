# RANKIT

RANKIT allows users to manipulate rankings through personalized data visualization and rank building. When interpreting multi-attribute datasets, a slight change of weight between attributes can heavily impact ranking results. Most publically available rankings do not expose the attributes used to compose the ranking. This lack of disclosure results in possible exploitation of data because rankings can imply a conclusion that is not necessarily true.

To allow for unbiased extrapolation of data, RANKIT is composed of two tools: Explore and Build.

To learn more about each tool, read our [guide](https://github.com/RankerToolWebsite/myRanker/wiki).

## Tool: Build

Build is a machine learning tool that is trained through user selected preferences of rank object instances. The Build tool collects data from pairwise comparisons of sample objects completed by the user. The tool applies a regression analysis to this data and determines a pattern and ranks all object within a dataset according to that pattern.

## Tool: Explore

Explore is an interactive tool that allows you to view and query through dataset information:

- Visualize a dataset and its attribute independent of the Build Tool
- Observe a personalized ranking of the entire dataset from partial rankings formulated in Build 
	- Displays attributes by their relative importance on the dataset’s ranking

## Getting Started

### Prerequisites:

- [npm](https://www.npmjs.com/)
	- `$ sudo apt-get install npm`
- [Node.js](http://nodejs.org/)
	- `$ sudo apt-get install -y nodejs`
- [Yeoman](http://yeoman.io/)
	- `$ npm install -g yo`
- [Phovea Generator](https://github.com/phovea/generator-phovea)
	- `$ npm install -g github:phovea/generator-phovea`
- [Python 3](https://www.python.org)
- [Pip](https://pypi.python.org/pypi/pip)
- [Flask](http://flask.pocoo.org/)
	- `$ pip install Flask`


### Run: 

#### To download dependiencies:

*in myRanker directory:*

`$ pip3 install -r requirements.txt`

*[optional] you may need to also set the path to numpy if you get a cython error:*

`$ export CFLAGS=-I$<location of Python>/lib/python<version>/site-packages/numpy/core/include`

Example: `export CFLAGS=-I/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/numpy/core/include/`

#### To startup the server:

*run project:* `$ python3 run.py`

