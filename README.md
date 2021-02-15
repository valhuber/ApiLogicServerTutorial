# ApiLogicServerTutorial

[![Binder](http://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/valhuber/ApiLogicServerTutorial/HEAD?urlpath=lab)

There is widespread agreement that APIs are strategic to the business, required for mobile apps and internal / external systems integration.

The problem is that they are time-consuming and complex to develop. This reduces strategic business agility.  At the tactical level, UI development can be delayed while awaiting API coding.

API Logic Server provides strategic business agility, by creating an executable server for a database.
Instead of weeks to months, follow this 10-20 minute Tutorial to **create**, **explore** and **customize** 
the 3 main elements of an API Logic Server:
1. A JSON:**API** for a database, with Open API (Swagger)
1. Business **Logic**, using a combination of spreadsheet like rules and Python
1. A Basic Web App - multi-page, multi-table, with intelligent joins and layouts

This project is a Jupyter notebook for the [API Logic Server](https://github.com/valhuber/ApiLogicServer#readme).
You can run it either:
* on the cloud using MyBinder (no install), or
* locally (enables all Browser-based options)

See the instructions for both options, below.

# MyBinder - no local install

Use **MyBinder** to avoid any local install:
1. Click the Binder logo (image above)
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
