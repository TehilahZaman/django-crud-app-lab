from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Catagory(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    def get_absolute_url (self):
        return reverse('catagory-detail', kwargs={'pk': self.id})
    

class Postit(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=250)
    color = models.CharField(max_length=100)
    importance = models.IntegerField()
    catagories = models.ManyToManyField(Catagory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
         return reverse('postit-detail', kwargs={'postit_id': self.id})
    
TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Reminder(models.Model):
    date = models.DateField('Reminder Date')
    time_of_day = models.CharField(max_length=1, 
        choices=TIMES,
        default=TIMES[0][0] )
    todo = models.CharField(max_length=50)

    # foreign key on the many side 
    #  renider belongs to a post it and must hold the id of the post it object it belongs to
    #  the on_delete ensures that the reminders are deleted too if the post it is deleted
    postit = models.ForeignKey(Postit, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.get_time_of_day_display()} on {self.date} "
    
    class Meta:
        ordering = ['-date']



