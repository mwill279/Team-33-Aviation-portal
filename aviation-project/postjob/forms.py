from django import forms
#from django.forms import ModelForm
from .models import Jobform



# class PostingForm(forms.Form):
#     title = forms.CharField(label='Title', max_length=100)
#     description = forms.CharField(label='Description', max_length=100, widget=forms.Textarea)
#     jobtype = forms.ChoiceField(label='Job Type', choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Internship', 'Internship')])

class DateInput(forms.DateInput):
    input_type = "date"

class TimeInput(forms.TimeInput):
    input_type = "time"

class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class PostingForm(forms.ModelForm):

    #jobtype = forms.ModelChoiceField(queryset=Jobtype.objects, empty_label=None,  widget=forms.RadioSelect)
    class Meta:
        model = Jobform
        fields = "__all__"
        labels = {
            'title': 'Title', 
            'decription': 'Description', 
            'jobtype': 'Job Type', 
            'postdate': 'Post Date', 
            'deadlinedate': 'Deadline Date',
            'posttime': 'Post Time', 
            'deadlinetime': 'Deadline Time'
            }
        widgets = {
            'title': forms.TextInput(attrs={'size':150, 'placeholder': 'e.g. Senior Manager'}),
            'description': forms.Textarea(attrs={'rows':10, 'cols':150}),
            'zipcode': forms.TextInput(attrs={'size':150, 'placeholder': 'e.g. 11111'}),
            # 'post': DateTimeInput(),
            # 'deadline': DateTimeInput(),
            'postdate': DateInput(),
            'posttime': TimeInput(),
            'deadlinedate': DateInput(),
            'deadlinetime': TimeInput(),
            }