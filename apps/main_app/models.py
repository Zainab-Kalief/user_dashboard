from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User

# Create your models here.
class MessageManager(models.Manager):
    def create_message(self, data, sender, recipient):
        error = {}
        if not data['message']:
            error['empty'] = 'Text field is empty'
            return error
        else:
            return self.create(sender=sender, recipient=recipient, message=data['message'])

class CommentManager(models.Manager):
    def create_comment(self, data, user, message):
        error = {}
        if not data['comment']:
            error['empty'] = 'Text field is empty'
            return error
        else:
            return self.create(comment=data['comment'], user=user, message=message)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages')
    recipient = models.ForeignKey(User, related_name='received_messages')
    message = models.TextField(max_length=2000)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = MessageManager()


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comments')
    message = models.ForeignKey(Message, related_name='message_comments')
    comment = models.TextField(max_length=2000)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = CommentManager()
