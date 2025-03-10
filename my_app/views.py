from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#  for CBV import --Views
from .models import Postit
#  for the reminder form in details 
from .forms import ReminderForm



# Create your views here.

def add_reminder(request, postit_id):
    form = ReminderForm(request.POST)
    if form.is_valid():
        new_reminder = form.save(commit=False)
        new_reminder.postit_id = postit_id
        new_reminder.save()
    return redirect('postit-detail', postit_id=postit_id)



# CBV

class PostitUpdate(UpdateView):
    model = Postit
    fields = ['text', 'color', 'importance']

class PostitDelete(DeleteView):
    model = Postit
    success_url = '/postits/'

class PostitCreate(CreateView):
    model = Postit
    fields = '__all__'


def postit_detail(request, postit_id):
    postit = Postit.objects.get(id=postit_id)

    # instantiate ReminderForm to be rendered in the details tempalte 
    reminder_form = ReminderForm() 
     
    return render(request, 'postits/detail.html', {'postit': postit, 'reminder_form': reminder_form})

def postit_index(request):

    postits = Postit.objects.all()
    return render(request, 'postits/index.html', {'postits': postits})

def home(request):
    return HttpResponse('<h1>This is the home page</h1>')


# class Postit:
#     def __init__(self, header, color, text):
#         self.header = header
#         self.color = color
#         self.text = text

# postits = [
#     Postit( 'todo', 'blue', 'blaaaaaaaa'),
#     Postit( 'notes', 'red', 'bla bla bla'),
#     Postit( 'appointments', 'yellow', 'bloooooo'),
#     Postit('doodles', 'pink', 'blooo blooo')
# ]
