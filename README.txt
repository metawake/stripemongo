===========
StripeMongo
===========

StripeMongo is a helper module for those using Stripe(payment gateway) with Django. 
StripeMongo allows to log incoming HTTP POST requests coming from Stripe to your
view which handles Stripe request. The requests are saved into MongoDB, which is
a natural fit for json data.

The purpose behind package is ability to quickly make various searches across
financial data locally to identify/prevent/detect problems or various patterns/situations.

The data goes into mongo db under collections named after Stripe objects,
e.g. customer, event, invoice.

Typical usage
often looks like this::

	@csrf_exempt
	@stripemongo
	def index(request):
		#your handler for stripe requests go here
		return HttpResponse(status=200)

Remember to set up configuration variables in settings.py,
or defaults will be used:

	MONGO_DBNAME' = 'test'
	MONGO_HOSTNAME = localhost'
	MONGO_PORT = 27017

Also, naturally, an account at Stripe.com is needed, where
you would configure your app's url for incoming http requests.

Package contains a sample Django app in demo folder, all you need
is Stripe account and external domain(or use proxy like pagekite for Stripe requests).
