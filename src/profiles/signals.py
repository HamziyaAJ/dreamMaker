from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Relationship


#create a profile automatically whenever a user is created. 
@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    #print('sender', sender)
    #print('instance',instance)
    if created:
        Profile.objects.create(user = instance)

#whenever a user accepted friends invitation, the user will be included in the friends list.
@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender_ =instance.sender
    receiver_ = instance.receiver
    if instance.status == 'accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()