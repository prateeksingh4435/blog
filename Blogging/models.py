from django.db import models

# Create your models here.
class Blog(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    email = models.EmailField(max_length=30)
    member = models.CharField(max_length=10,null='off')
    query = models.CharField(max_length=30)
    concern = models.TextField(max_length=100)

class signupdata(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50,null=True)
    password1= models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)


class WriteTechnologyBlog(models.Model):
    name = models.CharField(max_length = 60) 
    email = models.CharField(max_length = 60)
    topic = models.CharField(max_length = 150)
    write = models.TextField(max_length = 8000)
    date = models.DateField()
    
    def __str__(self):
        return self.topic

class WriteRoboticsBlog(models.Model):
    name = models.CharField(max_length = 60) 
    email = models.CharField(max_length = 60)
    topic = models.CharField(max_length = 150)
    write = models.TextField(max_length = 8000)
    date = models.DateField()
    
    def __str__(self):
        return self.topic
    

class WriteWebBlog(models.Model):
    name = models.CharField(max_length = 60) 
    email = models.CharField(max_length = 60)
    topic = models.CharField(max_length = 150)
    write = models.TextField(max_length = 8000)
    date = models.DateField()
    
    def __str__(self):
        return self.topic    

class WriteBlockchainBlog(models.Model):
    name = models.CharField(max_length = 60) 
    email = models.CharField(max_length = 60)
    topic = models.CharField(max_length = 150)
    write = models.TextField(max_length = 8000)
    date = models.DateField()
    
    def __str__(self):
        return self.topic
    
    
class BlogByUser(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    category = models.CharField(max_length = 20)
    topic = models.CharField(max_length = 100)
    blog = models.TextField(max_length = 10000)
    
    
    def __str__(self):
        return self.topic
    
    
    
    
