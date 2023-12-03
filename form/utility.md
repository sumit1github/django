## pass initial data from views

    initial_data = {'invitation_code':request.GET.get('ref_id', None)}
    context = {
        'form': self.form_class(initial= initial_data)
    }

## modify data in forms
modify data in forms.py then return the data to views.py

    from django.contrib.auth.hashers import make_password
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['confirm_password']:
            raise forms.ValidationError("Password Mismatched")
        else:
            hashed_password = make_password(cleaned_data['password'])
            cleaned_data['password'] = hashed_password

        if len(str(cleaned_data['contact']))!= 10:
            raise forms.ValidationError("Enter a ten digit contact number....")
        
        return cleaned_data