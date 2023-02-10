from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.test import SimpleTestCase

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): # new
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self): # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self): # new
        response = self.client.get(reverse("about_us"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): # new
        response = self.client.get(reverse("about_us"))
        self.assertTemplateUsed(response, "about_us.html")

    def test_template_content(self): # new
        response = self.client.get(reverse("about_us"))
        self.assertContains(response, "<h1>About page</h1>")