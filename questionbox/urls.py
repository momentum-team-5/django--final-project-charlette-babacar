"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("registration.backends.simple.urls")),
    path('', views.question_list, name="question_list"),
    path('questions/<int:pk>', views.question_details, name='question_details'),
    path('question/add', views.add_question, name="add_question"),
    path('questions/<int:pk>/add_answer/', views.add_answer, name='add_answer'),
    path('questions/<int:pk>/edit/', views.edit_question, name='edit_question'),
    path('questions/<int:pk>/delete/', views.delete_question, name='delete_question'),
    path('questions/<int:pk>/delete_answer/', views.delete_answer, name='delete_answer'),
    path('questions/search/', views.search, name='question_search'),
    path('questions/<int:pk>/add_favorite/', views.add_favorite, name='add_favorite'),
    path('contact/', views.contact_us, name='contact_us'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
