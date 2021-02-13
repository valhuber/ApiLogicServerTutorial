
# ApiLogicServer - enable flask run
import logic_bank_utils.util as logic_bank_utils
logic_bank_utils.add_python_path(project_dir="api_logic_server", my_file=__file__)

from app import app

app.run(host="0.0.0.0", port=8080, debug=True)
