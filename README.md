# Data collection tools
This is a project with many data collection tools.

You can test the web version of the tool here:
http://datatools.jvmsolutions.tech/

# Installing

## Data Collection Tools

> git clone https://github.com/aureliowozhiak/data_collection_tool

> cd data_collection_tool

> pip install -r requirements.txt


## CherryPy
This project has CherryPy dependency to run in web version

### Supported python version
CherryPy supports Python 3.5 through to 3.8.
CherryPy can be easily installed via common Python package managers such as setuptools or pip.

> easy_install cherrypy

> pip install cherrypy

You may also get the latest CherryPy version by grabbing the source code from Github:

*This need to be run, inside the "data_collection_tools" folder*

> git clone https://github.com/cherrypy/cherrypy

> cd cherrypy

> python setup.py install

# Project Architectural
This project has a MVC (Model–view–controller) software architectural, so the folders inside "src" has this structure:
![Model–view–controller - software architectural](docs/mvc.png)