from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name= models.CharField(max_length=264, unique= True)

    def __str__(self):
        return self.top_name


class WebPage(models.Model):
    topic= models.ForeignKey(Topic)
    name= models. CharField(max_length= 264, unique = True)
    url=models.CharField(unique= True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name= model.ForeignKey(WebPage)
    date= models.DateField()

    def __str__(self):
        return str(self.date)
