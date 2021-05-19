import django_tables2 as tables
from django.test import TestCase, RequestFactory

TEST_TABLE_DATA = [{"name": y} for y in range(100)]


class BulmaTableTest(TestCase):

    class DummyTable(tables.Table):
        name = tables.Column()

        class Meta:
            template_name = "django-tables2/bulma.html"

    def setUp(self):
        self.test_table_data = TEST_TABLE_DATA
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.table = self.DummyTable(self.test_table_data)
        self.request = self.factory.get('/')

    # Test that table renders without error
    def test_table_render(self):
        self.table.as_html(self.request)

    # Test that table includes pagination if: #data > per_page
    def test_table_paginate(self):
        self.table.paginate(page=1, per_page=1)
        html = self.table.as_html(self.request)
        self.assertIn('pagination', html)

    # Test that table includes pagination if: #data <= per_page
    def test_table_no_paginate(self):
        self.table.paginate(page=1, per_page=len(self.test_table_data))
        html = self.table.as_html(self.request)
        self.assertNotIn('pagination', html)
