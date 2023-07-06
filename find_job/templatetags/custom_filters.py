from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def days_ago(timestamp):
    posted_date = datetime.fromtimestamp(timestamp / 1000)  # Convert to datetime object
    current_date = datetime.now()
    days_ago = (current_date - posted_date).days
    return days_ago
