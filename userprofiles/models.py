from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('auth.User')

    @models.permalink
    def get_absolute_url(self):
        return 'profiles_profile_detail', (), {'username': self.user.username}
