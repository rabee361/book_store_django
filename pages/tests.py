from django.test import TestCase
from django.urls import reverse
from django.test import SimpleTestCase
from django.urls import resolve
from . import views


class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self): # new
        self.assertContains(self.response, "Home")

    def test_homepage_does_not_contain_incorrect_html(self): # new
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve("/")
        self.assertEqual(view.func.__name__, views.HomePageView.as_view().__name__)



class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_homepage_does_not_contain_incorrect_html(self): # new
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, views.AboutView.as_view().__name__)
