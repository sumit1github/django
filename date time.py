import datetime
from datetime import date

todays_date = date.today()  # today's date
month_num = todays_date.month
year = todays_date.year


time = datetime.datetime.now().strftime('%H:%M:%S')

************************************** using timezone **************************
works for django as well

#3333 ceate this class at helper.py ########

from django.conf import settings
from datetime import datetime
from pytz import timezone
from datetime import timedelta


class GetDateTime:
    def __init__(self):
        time_zone = timezone(settings.TIME_ZONE)
        self.today = datetime.now(time_zone)
        
    def get_day(self):
        
        data = self.today.date()

        return data.day
    
    def get_month(self):
        return self.today.month
    
    def get_year(self):
        return self.today.year
    
    def get_date(self,format='yyyy-mm-dd'):
        if format == 'dd-mm-yyyy':
            return self.today.strftime('%d-%m-%Y')
        else:
            return self.today.date()
    
    def date_delta(self, step_day):
        delta = timedelta(days=int(step_day))
        new_date = self.today + delta
        return new_date.date()
    
    def get_time(self):
        data = str(self.today).split()
        return data[1][:8]



##### views.py #####
class MarkAttendence(APIView):
    model=Attendence

    def post(self, request):

        date_time_instance = GetDateTime()
        todays_date = date_time_instance.get_date() # default : dd-mm-yyyy  option: date_time_instance.get_date('dd-mm-yyyy')
        day = date_time_instance.get_day()
        month_num = date_time_instance.get_month()
        year = date_time_instance.get_year()
        time = date_time_instance.get_time()





