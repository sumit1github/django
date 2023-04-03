STANDARDS=(
("--","--"),
)
class ChoiceFieldNoValidation(forms.ChoiceField):
	def validate(self, value):
	    pass


standards = ChoiceFieldNoValidation(choices=STANDARDS, required=False)
price.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'price'})

