###############################   date time filter ##############################
from datetime import datetime as dt
import datetime 
from django.conf import settings
from django.utils.timezone import make_aware

def get(self, request):
start_date= '2015-11-14'
end_date= '2015-11-16'

start_date= dt.strptime(request.GET.get('from'), '%Y-%m-%d').date()
start_date=make_aware(datetime.datetime.combine(start_date, datetime.time.min))
start_date.tzinfo

end_date= dt.strptime(request.GET.get('upto'), '%Y-%m-%d').date()
end_date = make_aware(datetime.datetime.combine(end_date, datetime.time.max))
end_date.tzinfo

order_list= order_list_data.filter(store= store_obj, created_at__range= (start_date, end_date)).order_by('-id')

