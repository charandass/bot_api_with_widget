from .views import AddBotInformation,GetAllBots,EditBotInformation,DeleteBotInformation,AddIndustries,GetWidget,EditWidget
from django.urls import path

urlpatterns = [
    path('add_bot_information/', AddBotInformation.as_view(),name='add_bot_information'),
    path('get_all_bot_information/', GetAllBots.as_view(),name='get_all_bot_information'),
    path('edit_bot_information/<bot_uuid>', EditBotInformation.as_view(),name='edit_bot_information'),
    path('delete_bot_information/<bot_uuid>', DeleteBotInformation.as_view(),name='delete_bot_information'),
    path('add_industries/', AddIndustries.as_view(),name='add_industries'),
    path('get_widget/<bot_uuid>/', GetWidget.as_view(),name='get_widget'),
    path('edit_widget/<widget_uuid>/', EditWidget.as_view(),name='edit_widget'),
   
]
