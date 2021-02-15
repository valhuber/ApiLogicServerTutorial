# ApiLogicServerTutorial

[![Binder](http://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/valhuber/ApiLogicServerTutorial/HEAD?urlpath=lab)

Jupyter Lab Notebook for [API Logic Server](https://github.com/valhuber/ApiLogicServer#readme).  You can run either
via MyBinder or local install, as described below.

# MyBinder - no local install

Use **MyBinder** to avoid any local install:
1. Click the Binder logo
   * In about 15 seconds, a JupyterLab should open (see below)
2. Double Click as shown below to open the notebook, and follow the remaining instructions to configure your workspace

<figure><img src="https://github.com/valhuber/ApiLogicServer/blob/main/images/tutorial/MyBinder-Initial.png?raw=true"></figure>


# Local Install

Or, you can **install** to run the notebook locally:
```
git clone https://github.com/valhuber/ApiLogicServerTutorial.git
cd ApiLogicServerTutorial
virtualenv venv
source venv/bin/activate   # windows venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```
