# ---------------------------------- forms ---------------------------------
class PlansForm(forms.ModelForm):

    name = forms.CharField(max_length=255, label='Plan Name')
    name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Name',"required":"required"})

    amount = forms.IntegerField()
    amount.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Amount',"required":"required"})

    validity = forms.IntegerField()
    validity.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter validity',"required":"required"})

    class Meta:
        model = models.DataPlans
        fields = ['name',"amount","validity"]


# ------------------------------------- views.py-----------------------------------
from django.http import JsonResponse

@method_decorator(utils.super_admin_only, name='dispatch')
class PlanUpdate(View):
    model = common_models.DataPlans
    form_class = common_forms.PlansForm 

    def get(self, request, plan_pk):
        plan = self.model.objects.filter(id = plan_pk).values_list('id','name','amount','validity')
        plan=list(plan)
        return JsonResponse(plan, safe=False)
    
    def post(self, request, plan_pk):
        plan = self.model.objects.get(id = plan_pk)
        form = self.form_class(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, "Plan is updated")
        else:
            
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
        
        return redirect('admin_dashboard:paln_list')
    
# -------------------------------------urls.py --------------------------------
    path('plans/plan_update/<str:plan_pk>', views.PlanUpdate.as_view(), name="plan_update"),