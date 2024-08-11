from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from accounts.models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver (sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('userprofile created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            #create user profile if not exist
            UserProfile.objects.create(user=instance)
            print('profile wasnt there but created one')

        print('User is updated')
# another way is ==== post_save.connect(post_save_create_profile_receiver, sender=User)
    


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'this user is being saved')
        