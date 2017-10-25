# RANKit

RANKit allows users to manipulate rankings through personalized data visualization and rank building. When interpreting multi-attribute datasets, a slight change of weight between attributes can heavily impact ranking results. Most publically available rankings do not expose the attributes used to compose the ranking. This lack of disclosure results in possible exploitation of data because rankings can imply a conclusion that is not necessarily true. 

To allow for unbiased extrapolation of data, RANKit is composed of two tools: Explore and Visualize.

To learn more about each tool, read our [guide](https://github.com/RankerToolWebsite/myRanker/wiki). 

## Tool: Explore

Based on [Caleydo LineUp](https://github.com/Caleydo/lineupjs), Explore is an interactive tool that allows you to visualize your desired ranking:

- Combine multiple attributes into a single, combined column to create a ranking
- Immediate responsive visual change of the rank with the modification of:
	- Weights of specified attribute 
	- Values of specified attribute

## Tool: Build 

Build is a machine learning tool that is trained through user selected preferences of rank object instances. The Build tool collects data from pairwise comparisons of sample objects completed by the user. The tool applies a regression analysis to this data and determines a pattern and ranks all object within a dataset according to that pattern. 

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


### Run: *CURRENTLY IN DEVELOPMENT*

To startup the server: `$ python3 run.py`
