Google App Engine Base Handlers
===============================

Base handlers for google app engine.

Usage:

.. code-block:: python

	from gae-handlers import BaseHandler

	class MainHandler(BaseHandler):
		template_name = "index.html"


	app = webapp2.WSGIApplication([
	    ('/', MainHandler),
	], debug=conf.DEBUG)


Prerequisites
-------------

Provide additional configuration for your project by creating module conf

Sample conf.py:

.. code-block:: python

	import os

	import jinja2


	def root(*args):
	    """
	    Get directory path from root
	    """
	    return os.path.abspath(
	        os.path.join(
	            os.path.dirname(__file__),
	            *args))


	# Template root folder
	TEMPLATE_ROOT = root('..', 'templates')

	# Jinja2 Environment
	JINJA_ENVIRONMENT = jinja2.Environment(
	    loader=jinja2.FileSystemLoader(TEMPLATE_ROOT),
	    extensions=['jinja2.ext.autoescape'],
	    autoescape=True)

	# Default email address to send message
	DEFAULT_EMAIL_ADDRESS = ''

	# debug mode
	DEBUG = True

	# Admin base url
	ADMIN_BASE_URL = '/sd-admin/'

	# Media url
	MEDIA_URL = '/media/'


For developers
--------------

Set up enviroinment (preferebly use `virtualenv`)
Run tests by executin `./test.sh`
To check coverage run `./coverage_run.sh`
To see results run `./coverage_report.sh`

Make sure you provide correct path to GAE `dev_appserver.py`




