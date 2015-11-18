from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from socialgraph.util import get_people_user_follows, get_people_following_user
from socialgraph.util import get_mutual_followers
from socialgraph.models import UserLink
from django.template import RequestContext

# Create your views here.
FRIEND_FUNCTION_MAP={
	'followers':get_people_user_follows,
	'following':get_people_following_user,
	'mutual':get_mutual_followers,
}

def friend_list(request, list_type, username):
	user = get_object_or_404(User, username=username)
	context = {
		'list_type' : list_type,
		'friends' : FRIEND_FUNCTION_MAP[list_type](user),
	}
	return render_to_response(
		'socialgraph/friend_list.html',
		context,
		context_instance = RequestContext(request),
	)

