from django.shortcuts import render_to_response
from django.template import RequestContext
from events.models import Event

# Create your views here.

def tonight(request):
	events = Event.objects.today().filter(latest=True)
	context = {
		'events' : events,
	}
	return render_to_response(
		'events/tonight.html',
		context,
		context_instance = RequestContext(request),
	)
