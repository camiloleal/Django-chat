from django.db import models


class ChatUser(models.Model):
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=15)
	email = models.EmailField('e-mail', blank=True)
	state = models.BooleanField("conected")


	def __unicode__(self):
		return self.username

class Room(models.Model):
	roomname = models.CharField(max_length=20)
	users = models.ManyToManyField(ChatUser)

	def __unicode__(self):
		return self.name

class Message(models.Model):
	room = models.ForeignKey(Room)
	user = models.ForeignKey(ChatUser)
	content = models.TextField()	
	datetime = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s - %s' % (self.user, self.content)

