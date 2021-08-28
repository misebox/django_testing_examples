
from tests.test_admin import BaseAdminTest


class AdminPackagesTest(BaseAdminTest):
    def test_spider_admin(self):
        admin_pages = [
            "/admin/packages/package/",
            "/admin/packages/packagecombo/",
            "/admin/packages/packagecomposition/",
            "/admin/packages/programminglanguage/",
        ]
        super()._spider_admin(admin_pages)