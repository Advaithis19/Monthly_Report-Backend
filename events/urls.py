from django.urls import path, re_path
from .views import EventList

app_name = 'events'

urlpatterns = [
    path('', EventList.as_view(), name='listevent'),
    # path('<int:pk>/', GrantDetail.as_view(), name='detailgrant'),
    # path('create/', CreateGrant.as_view(), name='creategrant'),
    # path('edit/<int:pk>/', EditGrant.as_view(), name='editgrant'),
    # path('delete/<int:pk>/', DeleteGrant.as_view(), name='deletegrant'),
    # re_path(r'filter/date/(?P<start_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})/',
    #         GrantListDateFilter.as_view(), name='filtergrant'),
]
