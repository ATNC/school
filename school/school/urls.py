"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^children/', include([
        url(r'^$', views.ChildrenView.as_view(), name='child_list_or_create'),
        url(r'^(?P<pk>[0-9]+)/', include([
            url(r'^$', views.ChildrenEditInfoView.as_view(), name='children_edit_info'),
            url(r'^add-parents/', views.ChildrenAddParentsView.as_view(), name='children_add_parents'),
        ])),
    ])),
    url(r'^journal/', include([
        url(r'^$', views.JournalAddRecord.as_view(), name='journal_add_record'),
        url(r'^(?P<pk>[0-9]+)/', views.JournalEditRecord.as_view(), name='journal_edit_record')

    ])),

]
