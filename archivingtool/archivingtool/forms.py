from django import forms

class PostUrlForm(forms.Form):  
	url = forms.CharField(
		label='Post URL',
		# widget = forms.TextInput(attrs = {
		# 	"class" : "text",
        #     'style' : 'width: 500px; height: 80px; text-align: center; border-radius: 40px; box-shadow: 4px 6px 5px 0 rgba(0, 0, 0, 0.3); margin-top: 150px; margin-left: 200px; font-family: Poppins_bold; font-size: 40px;',
        #     'placeholder' : 'Event Name',
		# 	"name" : "fname",
		# }),
	)