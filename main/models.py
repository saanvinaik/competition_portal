from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "cat_imgs/")

    def __str__(self):
        return self.title

class Branch(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "branch_imgs/")

    def __str__(self):
        return self.title

class Year(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "year_imgs/")

    def __str__(self):
        return self.title


class Domain(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "domain_imgs/")

    def __str__(self):
        return self.title

class Competition(models.Model):
    title = models.CharField(max_length=200)
    image=models.ImageField(upload_to = "competition_imgs/")
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specifications=models.TextField()
    # reg_fee=models.PositiveIntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class slider(models.Model):
    img = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=300)

# Competition Attributes
class CompetitionAttribute(models.Model):
    competition = models.ForeignKey(Competition,on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    # reg_fee = models.ForeignKey(Competition, on_delete=models.CASCADE , related_name='reg_fees')
    reg_fee=models.PositiveIntegerField()

    def __str__(self):
        return self.competition.title 