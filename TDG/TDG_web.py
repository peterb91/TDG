import os
import sys
sys.path.insert(0, os.path.abspath('../'))
from TDG.web_app.model_control import app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
