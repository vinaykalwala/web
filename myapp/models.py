from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Jobs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    positions = models.IntegerField()

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    role = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name



class Bussiness(models.Model):
  name = models.CharField(max_length=100)
  mobile = models.CharField(max_length=15)
  email = models.EmailField()
  address = models.CharField(max_length=255, blank=True)
  message = models.TextField()
  
  def __str__(self):
        return self.name
