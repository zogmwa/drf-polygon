from django.test import TestCase
from rest_framework.test import APIClient

from apps.polygons.constants import POLYGONS_3_20

# You've found the tests! you can quickly check your work by running these.
class PolygonTestCase(TestCase):

    def test_polygon_descending_view(self):
        client = APIClient()
        res = client.get('/polygons/descending/')
        expected = POLYGONS_3_20
        expected.reverse()
        self.assertEqual(res.data, expected)

    def test_polygon_post_view(self):
        client = APIClient()
        to_sum = ['triangle', 'square', 'pentagon']
        res = client.post('/polygons/total_sides/', {'to_sum': to_sum}, format='json')
        self.assertEquals(3 + 4 + 5, res.data)

        to_sum = []
        res = client.post('/polygons/total_sides/', {'to_sum': to_sum}, format='json')
        self.assertEquals(0, res.data)

        to_sum = ['triangle', 'pentagon']
        res = client.post('/polygons/total_sides/', {'to_sum': to_sum}, format='json')
        self.assertEquals(3 + 5, res.data)
