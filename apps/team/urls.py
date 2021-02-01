# Imports
from django.urls import path
from .views import add, team, edit, activate_team, invite, plans, plans_thankyou
from .api import create_checkout_session, stripe_webhook

app_name = 'team'

urlpatterns = [
    path('add/', add, name='add'),
    path('edit/', edit, name='edit'),
    path('invite/', invite, name='invite'),
    path('plans/', plans, name='plans'),
    path('plans/thank_you/', plans_thankyou, name='plans_thankyou'),
    path('activate_team/<int:team_id>/', activate_team, name='activate_team'),
    path('<int:team_id>/', team, name='team'),

    # API

    path('api/stripe_webhook/', stripe_webhook, name='stripe_webhook'),
    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
]