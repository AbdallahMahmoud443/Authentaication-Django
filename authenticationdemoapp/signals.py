from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(pre_save,sender=User,dispatch_uid="identifier_signal_1")
def pre_save_user(sender,instance,**kwargs): # sender => model , instance => Object
    print(f'Pre-Save user:{instance}') #! Execute Before insert or updated

@receiver(post_save,sender=User,dispatch_uid="identifier_signal_2")
def post_save_user(sender,instance,created,**kwargs): # sender => model , instance => Object
    if created:
        print(f'Post-save user:{instance} created') #! Execute After insert 
    else:
         print(f'Post-save user:{instance} Updated') #! Execute After udapte 

@receiver(pre_delete,sender=User,dispatch_uid="identifier_signal_3")
def pre_delete_user(sender,instance,**kwargs): # sender => model , instance => Object
        print(f'Pre-delete user:{instance}') #! Execute Before delete 

@receiver(post_delete,sender=User,dispatch_uid="identifier_signal_4")
def post_delete_user(sender,instance,**kwargs): # sender => model , instance => Object
        print(f'post-delete user:{instance}') #! Execute after delete 
