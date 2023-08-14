# -------------------code optimize-------------
`original code`
if filter_by == "uid":
    recharge_list = self.model.objects.filter(
        uid = query
    )
elif filter_by == "contact":
    recharge_list = self.model.objects.filter(
        customer__contact_number = query
    )
elif filter_by == "status":
    recharge_list = self.model.objects.filter(
        status = query
    )
else:
    recharge_list=[]

`optimize code 1`

query_conditions = {
    "uid": Q(uid=query),
    "contact": Q(customer__contact_number=query),
    "status": Q(status=query),
}

recharge_list = self.model.objects.filter(query_conditions.get(filter_by, Q())).order_by('-id')

paginaed_data = utils.paginate(request,recharge_list, 50)

`query_conditions.get(filter_by, Q())`

--> Q() -if there is no key matching filter, then the default filter


`optimize code 2`

from django.db.models import Q

if filter_by == "uid":
    query_condition = Q(uid=query)
elif filter_by == "contact":
    query_condition = Q(customer__contact_number=query)
elif filter_by == "status":
    query_condition = Q(status=query)
else:
    query_condition = Q()  # Empty condition to return an empty queryset

recharge_list = self.model.objects.filter(query_condition)


