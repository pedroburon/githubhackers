from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.core.urlresolvers import reverse


PASSWORD = 'password'


class LogoutViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='foo', password=PASSWORD, email='foo@example.net')
        self.url = reverse('logout')

    def test_basic_logout(self):
        self.client.login(username=self.user.username, password=PASSWORD)

        response = self.client.get(self.url, follow=True)

        self.assertIsInstance(response.context['user'], AnonymousUser)

    def test_basic_logout_redirection(self):
        expected_redirection = reverse('home')
        self.client.login(username=self.user.username, password=PASSWORD)

        response = self.client.get(self.url)

        self.assertRedirects(response, expected_redirection)
