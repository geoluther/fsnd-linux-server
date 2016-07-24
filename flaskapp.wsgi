#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp")

from Catalog import app as application
application.secret_key = 'this is a not-so-secret key'
