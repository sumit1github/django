#passing user to form.py from views


context={
  'form': OpportunityForm(instance= opportunity_obj ,user= request.user)
}


from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator, MaxFileSizeValidator, MinFileSizeValidator
from django.utils import timezone

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

            
    category = forms.ModelChoiceField(queryset = common_models.Category.objects.all())
    category.widget.attrs.update({'class': 'form-control','type':'text'})

    name = forms.CharField(max_length=255, label='Opportunity Name')
    name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Name',"required":"required"})
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    file= forms.ImageField(required=False, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif','pdf'])])
    file.widget.attrs.update({'class': 'form-control','type':'file',,"required":"required"})
    
    image = forms.FileField(validators=[FileExtensionValidator(['jpg', 'png']), MaxFileSizeValidator(20*1024)]) # 20 = kb

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
  

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',  
            }
        ),
        initial=timezone.now(),
    )

  date_time = forms.DateTimeField(label='My Date and Time Field', widget=forms.DateTimeInput(attrs={'type': 'datetime-local','class':'form-control'}))
  time = forms.TimeField(label='Start Time', widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder':"Start Time"}))

    class Meta:
        model = Opportunity
        fields = [
            'name','stage','business_type','currency','potential_amount','probability','note','assigned_to',
            'contact','account'
            
        ]
        
    def clean(self):
        if self.cleaned_data['email'] and self.cleaned_data['contact_number']:
            if User.objects.filter(Q(email=self.cleaned_data['email'].lower()) or Q(contact_number=self.cleaned_data['contact_number'])).exists()==True:
                raise forms.ValidationError("Email or Contact is already present.")

        else:
            raise forms.ValidationError("Email and Contact Number is Needed.")
