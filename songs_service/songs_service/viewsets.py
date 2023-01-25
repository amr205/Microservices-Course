
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class ChildModelViewset(ModelViewSet):
    parent_model = None
    child_model = None
    parent_to_child_rel = ""

    def get_queryset(self, *args, **kwargs):
        parent_pk = self.kwargs.get("parent_pk")
        try:
            parent = self.parent_model.objects.get(pk=parent_pk)
        except self.parent_model.DoesNotExist as e:
            raise self.parent_model.DoesNotExist(e)
        return getattr(parent, self.parent_to_child_rel).all()

    def perform_create(self, serializer):
        parent_pk = self.kwargs.get("parent_pk")
        try:
            parent = self.parent_model.objects.get(pk=parent_pk)
        except self.parent_model.DoesNotExist as e:
            raise self.parent_model.DoesNotExist(e)
        
        instance = serializer.save()
        getattr(parent, self.parent_to_child_rel).add(instance)
    

    def modify(self, request, *args, **kwargs):
        action = request.data['action']
        obj_id = self.child_model.objects.get(id=request.data['id'])
        parent_pk = self.kwargs.get("parent_pk")
        try:
            parent = self.parent_model.objects.get(pk=parent_pk)
        except self.parent_model.DoesNotExist as e:
            raise self.parent_model.DoesNotExist(e)
        
        if action == 'add':
            getattr(parent, self.parent_to_child_rel).add(obj_id)
        else:
            getattr(parent, self.parent_to_child_rel).remove(obj_id)
        return Response(request.data)