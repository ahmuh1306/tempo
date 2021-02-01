import django
import os
import sys
import stripe

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settingsprod")
django.setup()
from django.conf import settings

from apps.team.models import Team, Plan

stripe.api_key = settings.STRIPE_SECRET_KEY

for team in Team.objects.all():
    sub = stripe.Subscription.retrieve(team.stripe_subscription_id)

    if sub.status == 'cancelled':
        plan_default = Plan.objects.get(is_default=True)
        team.plan = plan_default
        team.plan_status = Team.PLAN_CANCELLED
        team.save()