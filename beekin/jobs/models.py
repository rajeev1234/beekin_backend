from django.db import models

# Create your models here.
class Jobs(models.Model):
    company = models.CharField(max_length=200 , blank=True, null= True)
    logo = models.CharField(max_length=200, blank=True, null= True)
    new = models.CharField(max_length=200, blank=True, null= True)
    featured = models.CharField(max_length=200, blank=True, null= True)
    position = models.CharField(max_length=200, blank=True, null= True)
    role = models.CharField(max_length=200, blank=True, null= True)
    level = models.CharField(max_length=200, blank=True, null= True)
    postedAt = models.CharField(max_length=200, blank=True, null= True)
    contract = models.CharField(max_length=200, blank=True, null= True)
    location = models.CharField(max_length=200, blank=True, null= True)
    languages = models.CharField(max_length=200, blank=True, null= True)
    tools = models.CharField(max_length=200, blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company
    


class AppliedJob(models.Model):
    job = models.ForeignKey(Jobs, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200 , blank=True, null= True)
    email = models.CharField(max_length=200 , blank=True, null= True)
    gender = models.CharField(max_length=200 , blank=True, null= True)
    phone = models.CharField(max_length=200 , blank=True, null= True)
    resume = models.CharField(max_length=1000 , blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name