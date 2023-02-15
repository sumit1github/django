###############################   date time filter ##############################
from datetime import datetime as dt
import datetime 

def get(self, request):
start_date= '2015-11-14'
end_date= '2015-11-16'

start_date= dt.strptime(request.GET.get('from'), '%Y-%m-%d').date()
start_date=datetime.datetime.combine(start_date, datetime.time.min)

end_date= dt.strptime(request.GET.get('upto'), '%Y-%m-%d').date()
end_date = datetime.datetime.combine(end_date, datetime.time.max)

order_list= order_list_data.filter(store= store_obj, created_at__range= (start_date, end_date)).order_by('-id')

