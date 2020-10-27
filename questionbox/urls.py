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
from core import views as core_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("registration.backends.simple.urls")),
    path('', core_views.list_questions, name="list_questions"),
    path('question/add', core_views.add_question, name="add_question"),
    path('question/<int:pk>', core_views.ShowQuestion.as_view(), name="show_question"),
    path('question/<int:pk>/add_answer', core_views.AddAnswer.as_view(), name="add_answer"),
    path('answer/<int:pk>/delete', core_views.DeleteAnswer.as_view(), name="delete_answer"),
    path('question/<int:pk>/delete', core_views.DeleteQuestion.as_view(), name="delete_question"),
    path('user/<int:pk>', core_views.UserProfile.as_view(), name="user_profile"),
    path('question/<int:pk>/fave', core_views.ToggleFavoriteQuestion.as_view(), name="toggle_question_fave"),
    path('answer/<int:pk>/fave', core_views.ToggleFavoriteAnswer.as_view(), name="toggle_answer_fave"),
    path('answer/<int:pk>/correct', core_views.ToggleCorrectAnswer.as_view(), name="toggle_answer_correct"),
    path('questions/search_results', core_views.SearchQuestions.as_view(), name="search"),
    path('question/<int:pk>/edit', core_views.EditQuestion.as_view(), name="edit_question"),
    path('answer/<int:pk>/edit', core_views.EditAnswer.as_view(), name="edit_answer"),
    
   
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
