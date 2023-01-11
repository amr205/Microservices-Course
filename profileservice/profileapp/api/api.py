from rest_framework import viewsets
from rest_framework.response import Response
from db_utils import get_db_handle, format_json

class UserViewset(viewsets.ViewSet):
    def test(self, request):
        db_handle, client = get_db_handle()

        db_handle.boxes.insert_one({
            'name': "shoes box",
            'number': 1
        })

        boxes = list(db_handle.boxes.find())
        return Response(format_json(boxes))