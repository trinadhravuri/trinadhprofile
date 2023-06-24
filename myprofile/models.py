from django.db import models

# Create your models here.

class Skills(models.Model):
    skillname = models.CharField(max_length=50)
    skillimage= models.ImageField(upload_to='skillimages',null=True)
    skillquote = models.TextField(max_length=500)
    skilldescription = models.TextField(max_length=10000)
    def __str__(self):
        return self.skillname

    class Meta:
        verbose_name_plural = 'Skills'
    
class Projects(models.Model):
    projectname= models.CharField(max_length=100)
    projectimage = models.ImageField(upload_to='projectimages',null=True)
    teamsixze = models.IntegerField()
    projectquote = models.TextField(max_length=1000)
    projectroles = models.TextField(max_length=20000)
    projectskills = models.ManyToManyField(Skills)

    def __str__(self):
        return self.projectname
    class Meta:
        verbose_name_plural = 'Projects'

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact= models.BigIntegerField()
    message = models.CharField(max_length=1000)
    content = models.TextField(max_length=100000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Enquiries'

class downloadcv(models.Model):
    file = models.FileField(upload_to='files',null=True)
