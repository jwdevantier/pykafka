import logging
import coloredlogs
from app import app

if __name__ == '__main__':
    coloredlogs.install(level=logging.DEBUG, show_hostname=False)
    app.run(debug=True)