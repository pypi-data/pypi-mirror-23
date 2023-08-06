"""
Test ordering backend.
"""

from __future__ import absolute_import

import unittest

from django.core.management import call_command

from nine.versions import DJANGO_GTE_1_10

import pytest

from rest_framework import status

import factories

from .base import BaseRestFrameworkTestCase

if DJANGO_GTE_1_10:
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse

__title__ = 'django_elasticsearch_dsl_drf.tests.test_ordering'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'TestOrdering',
)


@pytest.mark.django_db
class TestOrdering(BaseRestFrameworkTestCase):
    """Test ordering."""

    pytestmark = pytest.mark.django_db

    @classmethod
    def setUpClass(cls):
        """Set up class."""
        cls.books = factories.BookWithUniqueTitleFactory.create_batch(20)

        call_command('search_index', '--rebuild', '-f')

    def _order_by_field(self, field_name, check_ordering=True):
        """Order by field."""
        self.authenticate()

        url = reverse('bookdocument-list', kwargs={})
        data = {}

        # Should contain 20 results
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Order should be descending
        filtered_response = self.client.get(
            url + '?ordering={}'.format(field_name),
            data
        )
        self.assertEqual(filtered_response.status_code, status.HTTP_200_OK)

        if check_ordering:
            item_count = len(filtered_response.data['results'])

            for counter, item in enumerate(filtered_response.data['results']):
                if (counter > 1) and (counter < item_count + 1):
                    self.assertGreater(
                        filtered_response.data['results'][counter-1]['id'],
                        filtered_response.data['results'][counter]['id']
                    )

    def test_order_by_field(self):
        """Order by field."""
        return self._order_by_field('-id')

    def test_order_by_non_existent_field(self):
        """Order by non-existent field."""
        return self._order_by_field('another_non_existent_field',
                                    check_ordering=False)


if __name__ == '__main__':
    unittest.main()
