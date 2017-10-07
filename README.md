# RANKit

RANKit empowers users to manipulate rankings through personalized data visualization and rank building. When considering the interpretation of multi-attribute datasets, a slight shift of importance from one attribute to another can heavily impact end ranking results. Yet, the concealment of algorithms used to compute the ranking leave consumers limited in knowledge about the derivation of rankings, resulting in possible exploitation of data to imply a conclusion that is not necessarily true. 

To allow for unbiased extrapolation of data, RANKit is composed of two tools: Explore and Visualize.

To learn more about each tool, read our [guide](https://github.com/RankerToolWebsite/myRanker/wiki). 

## Tool: Explore

Based on [Caleydo LineUp](https://github.com/Caleydo/lineupjs), Explore is an interactive tool that allows you to viualzie your desired ranking:

- Combine multiple attributes into a single, combined column to create a ranking
- Immediate responsive visual change of the rank with the modification of:
	- Weights of specified attribute 
	- Values of specified attribute

## Tool: Build 

A machine learning tool that is trained on user specified preferences of rank object instances. The user supplies a pairwise comparisons for a sample of the objects from a dataset to the Build tool, which in consuming the information, applies regression analysis to determine concrete results to formulate a ranking for all objects within a dataset. 

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

To startup the server: `$ python3 app.py`
