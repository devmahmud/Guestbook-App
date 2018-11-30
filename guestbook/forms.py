from django import forms

class CommentForm(forms.Form):
    name = forms.CharField( max_length=25,
    widget=forms.TextInput( attrs={ 'id':"inputName" ,'class':"form-control", 'placeholder': "Name" }))

    comment = forms.CharField( widget=forms.Textarea( attrs={ 'class':"form-control", 'rows':"5", 'id':"comment", 'placeholder':"Comment" }))