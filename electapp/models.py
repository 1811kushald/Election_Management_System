from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Election(models.Model):
    election_name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    created_date = models.DateField(default=timezone.now)
    end_date = models.DateTimeField(blank=True,null=True)
    is_ended = models.BooleanField(default=False)
    
    def endelection(self):
        self.end_date = timezone.now()
        self.is_ended = True
        self.save()

    def get_absolute_url(self):
        return reverse("election_detail",kwargs={"pk":self.pk})
    
    def __str__(self):
        return self.election_name


class Candidate(models.Model):
    election_name = models.ForeignKey("electapp.Election",related_name='candidates',on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=100)
    grade = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(8)])
    votes = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    photo = models.ImageField(upload_to='candidate_photos/',blank=True,null=True)

    def get_absolute_url(self):
        return reverse("election_detail",kwargs={"pk":self.election_name.pk})
    
    def __str__(self):
        return self.candidate_name