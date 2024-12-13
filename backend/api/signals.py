from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(social_account_added)
def save_google_user_data(sender, request, sociallogin, **kwargs):
    if sociallogin.account.provider == 'google':
        user = sociallogin.user
        extra_data = sociallogin.account.extra_data 

        user.first_name = extra_data.get('given_name') 
        user.last_name = extra_data.get('family_name') 
        user.email = extra_data.get('email')
        user.google_id = extra_data.get('id')
        user.profile_picture = extra_data.get('picture')
        
        if not user.username:
            user.username = extra_data.get('name', user.email.split('@')[0])

        user.save()
