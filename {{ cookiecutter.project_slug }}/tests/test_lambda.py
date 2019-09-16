from django.test import Client, TestCase
from django.urls import reverse
from unittest.mock import patch
import json


class TestSkill(TestCase):

    def setUp(self):
        self.client = Client()

    def get_response(self, filename):
        with open(f'tests/input_data/{filename}', 'r') as f:
            payload = json.load(f)
            res = self.client.post(
                reverse("alexa_skill"), data=json.dumps(payload), content_type="json")
            return res

    def test_launch_intent(self):
        res = self.get_response("example_launch_intent.json")
        self.assertIn(
            "Ciao",
            res.json()['response']['outputSpeech']['ssml']
        )
        self.assertEqual(res.status_code, 200)
