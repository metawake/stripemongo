import json
from pymongo import Connection
from django.conf import settings 

def stripemongo(fn):
	"""
	Wrap Stripe view into logger function
	"""
	def wrap(request, *args, **kwargs):
	    
		try:
			raw_data = json.loads(request.raw_post_data)
			
			db = getattr(settings, 'MONGO_DBNAME', 'test')
			host = getattr(settings, 'MONGO_HOSTNAME', 'localhost')
			port = getattr(settings, 'MONGO_PORT', 27017)


			connection = Connection(host, port)
			db = connection[db]
			db.events.insert(raw_data)
			db[raw_data['data']['object']['object']].insert(raw_data['data']['object'])
		except Exception as e:
			#TODO implement exception handling, e.g. email admins or log
			print "Exception: %s" % e

		return fn(request, *args, **kwargs)
	return wrap