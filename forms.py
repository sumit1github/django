#passing user to form.py from views


context={
  'form': OpportunityForm(instance= opportunity_obj ,user= request.user)
}


from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class OpportunityEditForm(forms.ModelForm):

    STAGES = utils.OPPORTUNITY_STAGES

    CURRENCY_CODES = utils.CURRENCY_CODES

    class CustomMMCFu(forms.ModelMultipleChoiceField):
        def label_from_instance(self, assigned_to):
            return "%s" % assigned_to.email
     


    def __init__(self, *args, **kwargs):
       
        user = kwargs.pop('user')

        super(UpdateOpportunityForm,self).__init__(*args, **kwargs)
        if user:
            self.fields['assigned_to'].queryset = User.objects.filter(org=user.org)
            self.fields['contact'].queryset = Contact.objects.filter(org= user.org)
            self.fields['account'].queryset = Account.objects.filter(org= user.org)
            

    name = forms.CharField(max_length=255, label='Opportunity Name')
    name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Name',"required":"required"})
    
    file= forms.FileField(required= False)
    file.widget.attrs.update({'class': 'form-control','type':'file',,"required":"required"})

    note = forms.CharField(required=False, label='Add Some Extra Information' , widget=forms.Textarea(attrs={"class":"form-control","rows":"2"}))
    note.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Description'})

    assigned_to = CustomMMCFu(required=False, queryset=User.objects.none())
    assigned_to.widget.attrs.update({'class': 'form-control','type':'text'})

    contact = forms.ModelChoiceField(required=False, queryset=Contact.objects.none())
    contact.widget.attrs.update({'class': 'form-control','type':'text'})

    account = forms.ModelChoiceField(queryset=Account.objects.none())
    account.widget.attrs.update({'class': 'form-control','type':'text','required':'required'})

    stage = forms.ChoiceField(choices=STAGES)
    stage.widget.attrs.update({'class': 'form-control','type':'text',"required":"required"})

    business_type = forms.ChoiceField(choices= utils.OPPORTUNITY_TYPE)
    business_type.widget.attrs.update({'class': 'form-control','type':'text',"required":"required"})

    currency = forms.ChoiceField(choices=CURRENCY_CODES, initial= 'USD')
    currency.widget.attrs.update({'class': 'form-control','type':'text',"required":"required"})

    potential_amount = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    potential_amount.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Amount',"required":"required"})

    probability = forms.IntegerField(label='Probability (Enter from 0 to 100)')
    probability.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Probability',"required":"required"})


    class Meta:
        model = Opportunity
        fields = [
            'name','stage','business_type','currency','potential_amount','probability','note','assigned_to',
            'contact','account'
            
        ]
