from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserLink(models.Model):
	from_user = models.ForeignKey(User, related_name = 'following_set')
	to_user = models.ForeignKey(User, related_name = 'follower_set')
	date_added = models.DateTimeField(default=datetime.now)
	
	def __unicode__(self):
		return "%s is following %s" %(self.from_user.username, self.to_user.username)
	
	def save(self,*args, **kwargs):
		if self.from_user == self.to_user:
			raise ValueError("Cannot follow yourself.")
		super(UserLink, self).save(**kwargs)

	class Meta:
		unique_together = (('to_user','from_user'),)
