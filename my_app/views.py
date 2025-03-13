from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
#  for CBV import --Views
from .models import Postit, Catagory
#  for the reminder form in details 
from .forms import ReminderForm
#  auth import 
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin







def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('postit-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


class home(LoginView):
    template_name = 'home.html'

@login_required
def remove_catagory(request, postit_id, catagory_id):
    postit = Postit.objects.get(id=postit_id)
    postit.catagories.remove(catagory_id)
    return redirect('postit-detail', postit_id=postit_id)

@login_required
def associate_catagory(request, postit_id, catagory_id):
    Postit.objects.get(id=postit_id).catagories.add(catagory_id)
    return redirect('postit-detail', postit_id=postit_id)


class CatagoryUpdate(LoginRequiredMixin, UpdateView):
    model = Catagory
    fields = '__all__'

class CatagoryDelete(LoginRequiredMixin, DeleteView):
    model = Catagory
    success_url = '/catagories'

class CatagoryList(ListView):
    model = Catagory

class CatagoryDetail(LoginRequiredMixin, DetailView):
    model = Catagory


class CatagoryCreate(LoginRequiredMixin, CreateView):
    model = Catagory
    fields = '__all__'

@login_required
def add_reminder(request, postit_id):
    form = ReminderForm(request.POST)
    if form.is_valid():
        new_reminder = form.save(commit=False)
        new_reminder.postit_id = postit_id
        new_reminder.save()
    return redirect('postit-detail', postit_id=postit_id)


class PostitUpdate(LoginRequiredMixin, UpdateView):
    model = Postit
    fields = ['text', 'color', 'importance']

class PostitDelete(LoginRequiredMixin, DeleteView):
    model = Postit
    success_url = '/postits/'

class PostitCreate(LoginRequiredMixin, CreateView):
    model = Postit
    fields = ['title', 'text', 'color', 'importance']

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

@login_required
def postit_detail(request, postit_id):
    postit = Postit.objects.get(id=postit_id)
    # find all the catagories 
    # pass then to the template 
    # catagories = Catagory.objects.all()

    #  now only get the catagories the post it doesn't have 
    catagories_not_tagged = Catagory.objects.exclude(id__in = postit.catagories.all().values_list('id'))

    # instantiate ReminderForm to be rendered in the details tempalte 
    reminder_form = ReminderForm() 
     
    return render(request, 'postits/detail.html', {'postit': postit, 'reminder_form': reminder_form, 'catagories': catagories_not_tagged})

@login_required
def postit_index(request):
    postits = Postit.objects.filter(user=request.user)
    return render(request, 'postits/index.html', {'postits': postits})


