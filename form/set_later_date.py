from django.utils import timezone
from datetime import date, timedelta

def set_plan_ends_to_30_days_later():

  today = date.today()

  return today + timedelta(days=30)



plan_ends = forms.DateField(
    widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'type': 'date',  
        }
    ),
    initial=set_plan_ends_to_30_days_later(),
)
