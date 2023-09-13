from django.urls import path, include
from . import views



urlpatterns = [
    path('home/', views.home),
    path('home/UZB/', views.uzb, name='UZB'),
    path('home/RUS/', views.rus, name='RUS'),
    path('home/ENG/', views.eng, name='ENG'),
    path('home/uzb_test/<int:user_id>', views.uzb_test, name='uzb_test'),
    path('home/eng_test/<int:user_id>', views.eng_test, name='eng_test'),
    path('home/rus_test/<int:user_id>', views.rus_test, name='rus_test'),
    path('home/score/<int:work_id>', views.result_view, name='calculate'),
    path('home/login', views.UserInfo, name='uzb_login'),
    path('home/login/rus', views.UserInfoRus, name='rus_login'),
    path('home/login/eng', views.UserInfoEng, name='eng_login'),


]