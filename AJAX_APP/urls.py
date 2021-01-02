from django.urls import path
from .views import CrudView,CreateCrudUser,UpdateCrudUser,DeleteCrudUser

urlpatterns = [
    path('', CrudView.as_view(), name="crud_ajax"),
    path('create', CreateCrudUser.as_view(), name="create"),
    path('update', UpdateCrudUser.as_view(), name="update"),
    path('delete', DeleteCrudUser.as_view(), name="delete")
]