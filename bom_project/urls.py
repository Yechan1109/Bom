from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from bom_user.views import main, logout, DB, UserList, UserListDetail, UserInfo
from bom_user.views import IndexView, SetPlanView, GetPlanView, DangerView, UserView, PerformanceView, ToadminView 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', IndexView.as_view(), name='index'),
    path('', main, name='index'),
    path('main/', main, name='main'),
    path('logout/', logout, name='logout'),
    path('setplan/', SetPlanView.as_view(), name='setplan'),
    path('getplan/', GetPlanView.as_view(), name='getplan'),
    path('initial/', UserView.as_view(), name='initial'),
    path('danger/', DangerView.as_view(), name='danger_cf'),
    path('perfor/', PerformanceView.as_view(), name='perfor'),
    path('adminactions/', include('adminactions.urls')),
    path('userlist/', UserList.as_view(), name='userlist'),
    path('userlist/<int:pk>/', UserListDetail.as_view(), name='userlist_detail'),
    path('toadmin/', ToadminView.as_view(), name='toadmin'),
    path('db/', DB, name='db'),
    path('first/', UserInfo, name='userinfo')
    # path('getplan/search/', SearchResultsView.as_view(), name='search_results')

]

import adminactions.actions as actions
actions.add_to_site(admin.site)