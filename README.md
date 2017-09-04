# myRanker

New ranking analysis tool based on [Caleydo lineup](https://github.com/Caleydo/lineupjs).

To get started with development: 

## Prerequisites

Install [npm](https://www.npmjs.com/), [Node.js](http://nodejs.org/), [Yeoman](http://yeoman.io/) and the [Phovea Generator](https://github.com/phovea/generator-phovea).

 As an example to do this on Ubuntu 14.04 I did the following:
  
`sudo apt-get install npm`

`curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -`

`sudo apt-get install -y nodejs`

`npm install -g yo`

`npm install -g github:phovea/generator-phovea`
    
**Ubuntu has an operating system specific issue when installing nodejs (you may not need):**
    
#create a symlink for "node" command

`sudo ln -s `which nodejs` /usr/local/bin/node`



## Installation

- Clone this repository and cd into the myRanker directory
- Create workspace: `yo phovea:workspace` with the following inputs:
  * Virtual Environment: none
  * Additional Plugins: none (just press Enter)
- Install dependencies: `npm install`
- Creating a symbolic link for the LineUp library
  * `rm -r node_modules/lineupjs/*` 
  * `ln -s "lineup.js" "node_modules/lineupjs"`

## Run Workspace

- Run `npm run start:lineup_demos_source`
- Open web browser with the URL (e.g. localhost:8080) printed in the console output
