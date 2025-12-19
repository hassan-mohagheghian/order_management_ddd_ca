from django.urls import path

from .views import CreateListOrderView, EditOrderView

urlpatterns = [
    path("", CreateListOrderView.as_view(), name="create_list_order"),
    path("/<uuid:order_id>", EditOrderView.as_view(), name="edit_order"),
]
