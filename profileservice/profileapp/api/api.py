from rest_framework import viewsets
from rest_framework.response import Response
from db_utils import get_db_handle, format_json, format_str_json
from profileapp.api.serializer import ProfileSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
from bson.objectid import ObjectId
from sbus_utils import send_message
import json

class UserViewset(viewsets.ViewSet):
    def create(self, request):
        data = request.data
        serializer = ProfileSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        data = serializer.validated_data
        db_handle, client = get_db_handle()
        db_handle.profiles.insert_one(data)

        message_data = {
            'action': 'create',
            'profile': format_json(data)
        }
        send_message(json.dumps(message_data))
        return Response(message_data, status=HTTP_200_OK)
    
    def list(self, request):
        db_handle, client = get_db_handle()
        profiles = list(db_handle.profiles.find())
        return Response(format_json(profiles))
    
    def retrieve(self, request, pk=None):
        db_handle, client = get_db_handle()
        profile = db_handle.profiles.find_one(ObjectId(pk))

        if profile is None:
            return Response('Profile not found', status=HTTP_404_NOT_FOUND)

        return Response(format_json(dict(profile)))
    
    def delete(self, request, pk=None):
        db_handle, client = get_db_handle()
        db_handle.profiles.delete_one({'_id': ObjectId(pk)})

        return Response('')
    
    def update(self, request, pk=None):
        data = request.data
        serializer = ProfileSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        data = serializer.validated_data
        db_handle, client = get_db_handle()
        db_handle.profiles.update_one({'_id': ObjectId(pk)}, {"$set": data})
        data['_id'] = str(pk)

        message_data = {
            'action': 'update',
            'profile': format_json(data)
        }
        send_message(json.dumps(message_data))
        return Response(format_json(data), status=HTTP_200_OK)