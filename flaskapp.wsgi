#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/pro/python/FlaskApp/")

from FlaskApp import app as application
application.secret_key = 'secret key'
