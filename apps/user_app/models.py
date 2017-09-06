from __future__ import unicode_literals
from django.db import models
import bcrypt, re
EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class UserManager(models.Manager):
    def create_user(self, data):
        errors = {}
        if not data['first_name'] or len(data['first_name']) < 2 or not data['last_name'] or len(data['last_name']) < 2:
            errors['name'] = 'Enter a valid name'
        if not data['email'] or not EMAIL_REGEX.match(data['email']):
            errors['email'] = 'Enter a valid email'
        if self.filter(email=data['email']):
            errors['email_exist'] = 'Email already exist'
        if not data['password'] or len(data['password']) < 6:
            errors['password'] = 'Enter a password of 8  xters or up'
        if not data['confirm_password'] or data['confirm_password'] != data['password']:
            errors['confirm_password'] = 'Enter a matching password'
        if len(errors):
            return errors
        else:
            hash_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            return self.create(first_name=data['first_name'], last_name=data['last_name'], user_type=False, email=data['email'], password=hash_password)

    def validate_user(self, data):
        errors = {}
        if self.filter(email=data['email']):
            user = self.get(email=data['email'])
            hash_password = bcrypt.hashpw(data['password'].encode(), user.password.encode())
            if (hash_password == user.password):
                return user
            else:
                errors['password'] = 'Invalid Password'
        else:
            errors['email'] = 'Invalid Email'
        return errors

    def update_info(self, data, user_id):
        errors = {}
        if not data['first_name'] or len(data['first_name']) < 2 or not data['last_name'] or len(data['last_name']) < 2:
            errors['name'] = 'Enter a valid name'
        if not data['email'] or not EMAIL_REGEX.match(data['email']):
            errors['email'] = 'Enter a valid email'
        if self.exclude(id=user_id).filter(email=data['email']):
            errors['email_exist'] = 'Email already exist'
        if len(errors):
            return errors
        else:
            return self.filter(id=user_id).update(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])

    def update_password(self, data, user_id):
        errors = {}
        if not data['password'] or len(data['password']) < 6:
            errors['password'] = 'Enter a password of 8  xters or up'
        if not data['confirm_password'] or data['confirm_password'] != data['password']:
            errors['confirm_password'] = 'Enter a matching password'
        if len(errors):
            return errors
        else:
            hash_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            return self.filter(id=user_id).update(password=hash_password)

    def update_description(self, data, user_id):
        error = {}
        if not len(data['description']):
            error['description'] = 'Field can not be empty'
            return error
        else:
            return self.filter(id=user_id).update(description=data['description'])

    def delete_user(self, user_id):
        return self.filter(id=user_id).delete()        


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    description = models.TextField(max_length=1000, default='')
    user_type = models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = UserManager()
