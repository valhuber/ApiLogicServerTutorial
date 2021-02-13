import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)

# ApiLogicServer - enable flask fab create-admin
import logic_bank_utils.util as logic_bank_utils
logic_bank_utils.add_python_path(project_dir="api_logic_server", my_file=__file__)

import database.models as models
from logic import declare_logic
from logic_bank.logic_bank import LogicBank
LogicBank.activate(session=db.session, activator=declare_logic)

appbuilder = AppBuilder(app, db.session)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import views
