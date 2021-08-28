from django.test import TestCase, Client
from django.contrib.auth.models import User


class BaseAdminTest(TestCase):
    def setUp(self):
        self.username = "test_admin"
        self.password = User.objects.make_random_password()
        user, _ = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user

    def _spider_admin(self, admin_pages):
        client = Client()
        client.login(username=self.username, password=self.password)
        for page in admin_pages:
            resp = client.get(page)
            assert resp.status_code == 200
            assert b"<!DOCTYPE html>" in resp.content
            assert b"test_admin" in resp.content


class AdminAuthTest(BaseAdminTest):
    def test_spider_admin(self):
        admin_pages = [
            "/admin/",
            "/admin/auth/",
            "/admin/auth/group/",
            "/admin/auth/group/add/",
            "/admin/auth/user/",
            "/admin/auth/user/add/",
            "/admin/password_change/"
        ]
        super()._spider_admin(admin_pages)