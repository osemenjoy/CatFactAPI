from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timezone

class ProfileAPI(APIView):
    """
    A simple API to return profile information and random facts
    """

    def get(self, request):
        try:
            resp = requests.get("https://catfact.ninja/fact", timeout=5)
            fact = resp.json().get("fact", "No fact found")
        except requests.RequestException as e:
            fact = f"Could not retrieve a fact at this time: {e}"


        data = {
            "status": "success",
            "user": {
                "email": "osemenjoy448@gmail.com",
                "name": "Osemen Esezobor",
                "stack": "Python/Django",
            },
            "date": datetime.now(timezone.utc).isoformat(),
            "fact": fact
        }
        return Response(
            data,
            status=status.HTTP_200_OK
        )