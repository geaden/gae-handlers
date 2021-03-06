Google App Engine Base Handlers
===============================

.. image:: https://travis-ci.org/geaden/gae-handlers.svg?branch=master
    :target: https://travis-ci.org/geaden/gae-handlers

Base handlers for `Google App Engine <https://code.google.com/p/googleappengine/>`_.

Template engine `Jinja2 <http://jinja.pocoo.org/docs/>`_.

Usage:

Clone it into your project by ``git clone <gae-handlers-repo> gae_handlers``, then:

.. code-block:: python

	from gae_handlers.core import BaseHandler

	class MainHandler(BaseHandler):
		template_name = "index.html"


	app = webapp2.WSGIApplication([
	    ('/', MainHandler),
	], debug=conf.DEBUG)


Prerequisites
-------------

Provide additional configuration for your project by creating module conf

Sample ``conf.py``:

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
	ADMIN_BASE_URL = '/admin/'

	# Media url
	MEDIA_URL = '/media/'


For developers
--------------

* Set up enviroinment (preferebly use `virtualenv`)
* Run tests by executing ``./test.sh``
* To check coverage run ``./coverage_run.sh``
* To see results run ``./coverage_report.sh``

Make sure you provide correct path to GAE ``dev_appserver.py``




