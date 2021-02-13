from safrs import SAFRSAPI

# FIXME from .json_encoder import SAFRSJSONEncoderExt
from database import models

"""
ApiLogicServer Generate From Model 01.04.05

Using Python: 3.8.6 (default, Oct 27 2020, 21:11:31) 
[Clang 12.0.0 (clang-1200.0.32.27)]

At: 2021-02-12 10:48:11.228636

"""

def expose_models(app, HOST="localhost", PORT=5000, API_PREFIX="/api"):
    """this is called by api / __init__.py"""

    api = SAFRSAPI(app, host=HOST, port=PORT)
    api.expose_object(models.Category)
    api.expose_object(models.CustomerCustomerDemo)
    api.expose_object(models.OrderDetail)
    api.expose_object(models.Order)
    api.expose_object(models.OrderZ)
    api.expose_object(models.Customer)
    api.expose_object(models.CustomerDemographic)
    api.expose_object(models.EmployeeAudit)
    api.expose_object(models.EmployeeTerritory)
    api.expose_object(models.Employee)
    api.expose_object(models.Product)
    api.expose_object(models.Region)
    api.expose_object(models.Shipper)
    api.expose_object(models.Supplier)
    api.expose_object(models.Territory)
