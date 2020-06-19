from django.shortcuts import render
from .forms import PostingForm
# Create your views here.

def posting(request):
    if request.method == 'POST':
        filled_form = PostingForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = '%s Posting submitted!!' %(filled_form.cleaned_data['title'],)
            new_form = PostingForm()
            return render(request, 'posting.html', {'postingform':new_form, 'note':note})
    else: 
        form = PostingForm()
        return render(request, 'posting.html', {'postingform':form})



