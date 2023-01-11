from profileapp.api.api import UserViewset

user_view = UserViewset.as_view({'post':'create', 'get': 'list'})
user_items_view = UserViewset.as_view({'get':'retrieve', 'put': 'update', 'delete': 'delete'})