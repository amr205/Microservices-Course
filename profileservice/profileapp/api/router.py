from profileapp.api.api import UserViewset

user_view = UserViewset.as_view({'get':'test'})