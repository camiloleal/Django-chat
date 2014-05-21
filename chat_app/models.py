from django.db import models
from django.contrib.auth.models import User

class ChatProfile(models.Model):
	user = models.ForeignKey(User, unique=True, blank=True, null=True)
	state = models.BooleanField("connected")
	success_url = ('/login/')

	def __unicode__(self):
		return self.user.username

class Room(models.Model):
	roomname = models.CharField(max_length=20)
	users = models.ManyToManyField(User)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['roomname']

class Message(models.Model):
	room = models.ForeignKey(Room)
	user = models.ForeignKey(User)
	content = models.TextField()	
	datetime = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s - %s' % (self.user, self.content)



