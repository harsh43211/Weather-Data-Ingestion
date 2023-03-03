from .models import Weather, Stats
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class WeatherTestCase(APITestCase):
    """
    Test Weather Endpoints
    """

    def test_get_weather(self):
        Weather.objects.create(
            Station_ID="USC001278",
            Date="19830507",
            Maxtemp=45,
            Mintemp=10,
            Precipitation=50,
        )
        response = self.client.get(reverse("weather"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)
        self.assertEqual(response.data["count"], 1)


class StatsTestCase(APITestCase):
    """
    Test Stats Endpoints
    """

    def test_get_stats(self):
        Stats.objects.create(
            Date="2023-21-01",
            Station_ID="USC001278",
            AvgMaxtemp=30,
            AvgMintemp=7,
            TotalAccPrecipitation=120,
        )
        response = self.client.get(reverse("stats"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)
        self.assertEqual(response.data["count"], 1)
