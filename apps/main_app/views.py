from django.shortcuts import render, redirect
from django.contrib import messages
from ..user_app.models import User
from .models import Message, Comment
from django.core.urlresolvers import reverse

# Create your views here.
def dashboard_admin(request):
    if User.objects.filter(id=request.session['user_id']):
        user = User.objects.get(id=request.session['user_id'])
        context = {'user': user, 'users': User.objects.all()}
    return render(request, 'main_app/dashboard_admin.html', context)


def dashboard_user(request):
    if User.objects.filter(id=request.session['user_id']):
        user = User.objects.get(id=request.session['user_id'])
        context = {'user': user, 'users': User.objects.all()}
    return render(request, 'main_app/dashboard.html', context)

def add_user(request):
    return render(request, 'main_app/add_user.html')

def create_user(request):
    entry = User.objects.create_user(request.POST)
    if not type(entry) is dict:
        return redirect('main:dashboard_admin')
    else:
        if 'name' in entry:
            messages.add_message(request, messages.INFO, entry['name'], extra_tags='sign_up')
        if 'email' in entry:
            messages.add_message(request, messages.INFO, entry['email'], extra_tags='sign_up')
        if 'password' in entry:
            messages.add_message(request, messages.INFO, entry['password'], extra_tags='sign_up')
        if 'confirm_password' in entry:
            messages.add_message(request, messages.INFO, entry['confirm_password'], extra_tags='sign_up')
        if 'email_exist' in entry:
            messages.add_message(request, messages.INFO, entry['email_exist'], extra_tags='sign_up')
        return redirect('main:add_user')

def edit_profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'main_app/edit_profile.html', context)

def edit_info(request, user_id):
    entry = User.objects.update_info(request.POST, user_id)
    if not type(entry) is dict:
        current_user = User.objects.get(id=request.session['user_id'])
        if current_user.user_type == True:
            return redirect('main:dashboard_admin')
        else:
            return redirect('main:dashboard_user')
    else:
        if 'name' in entry:
            messages.add_message(request, messages.INFO, entry['name'], extra_tags='edit_info')
        if 'email' in entry:
            messages.add_message(request, messages.INFO, entry['email'], extra_tags='edit_info')
        if 'email_exist' in entry:
            messages.add_message(request, messages.INFO, entry['email_exist'], extra_tags='sign_up')
        return redirect('main:edit_profile')


def change_password(request, user_id):
    entry = User.objects.update_password(request.POST, user_id)
    if not type(entry) is dict:
        current_user = User.objects.get(id=request.session['user_id'])
        if current_user.user_type == True:
            return redirect('main:dashboard_admin')
        else:
            return redirect('main:dashboard_user')
    else:
        if 'password' in entry:
            messages.add_message(request, messages.INFO, entry['password'], extra_tags='password')
        if 'confirm_password' in entry:
            messages.add_message(request, messages.INFO, entry['confirm_password'], extra_tags='password')
        return redirect('main:edit_profile')

def change_description(request, user_id):
    entry = User.objects.update_description(request.POST, user_id)
    print 'ON TOP', entry, 'GHGHJgd'
    if not type(entry) is dict:
        current_user = User.objects.get(id=request.session['user_id'])
        if current_user.user_type == True:
            return redirect('main:dashboard_admin')
        else:
            return redirect('main:dashboard_user')
    else:
        if 'description' in entry:
            messages.add_message(request, messages.INFO, entry['description'], extra_tags='description')
        return redirect('main:edit_profile')

def remove_page(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'main_app/delete.html', context)


def delete_this_user(request, user_id):
    print User.objects.delete_user(user_id)
    return redirect('main:dashboard_admin')


def view_user(request, user_id):
    user = User.objects.get(id=user_id)
    messages = Message.objects.filter(recipient=user).order_by('-created_at')
    context = {'user': user, 'messages': messages}
    return render(request, 'main_app/show_user.html', context)


def post_message(request, user_id):
    recipient = User.objects.get(id=user_id)
    sender = User.objects.get(id=request.session['user_id'])
    Message.objects.create_message(request.POST, sender, recipient)
    return redirect(reverse('main:view_user', kwargs={'user_id': user_id }))
