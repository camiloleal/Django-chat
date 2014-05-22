from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	state = models.BooleanField('Conected')
	#friends = models.ManyToManyField(User)

	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance, state=False)

	post_save.connect(create_user_profile, sender=User)
	
	def __unicode__(self):
		return self.user.username

class Room(models.Model):
	roomname = models.CharField(max_length=20)
	#users = models.ManyToManyField(User)

	def __unicode__(self):
		return self.roomname

	class Meta:
		ordering = ['roomname']

class Message(models.Model):
	room = models.ForeignKey(Room)
	user = models.ForeignKey(User)
	content = models.TextField()	
	datetime = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s - %s' % (self.user, self.content)



