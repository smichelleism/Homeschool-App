from django import forms
from .models import HomeschoolApplication

class HomeschoolApplicationModelForm(forms.ModelForm):
	class Meta:
		model = HomeschoolApplication
		fields = (
			'first_name', 
			'last_name', 
			'email', 
			'street_address', 
			'city',  
			'zipcode', 
			'phone_cell', 
			'phone_land', 
			'occupation',
			'hh_income',
			'own_cats',
			'other_pets',
			'date_found',
			'est_age',	
			'num_found',
			'location',
			'seen_mom',
			'seen_other_strays',
			'notes_public')
