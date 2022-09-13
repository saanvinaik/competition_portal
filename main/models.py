from distutils.command.upload import upload
from django.db import models
from django.utils.html import mark_safe
# Create your models here.
class slider(models.Model):
    img = models.ImageField(upload_to = "slider_imgs")
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = '1. sliders'

    def image_tag(self):
        return mark_safe('<img src="%s" width ="50" height ="50" />' % (self.img.url))


    def __str__(self):
        return self.alt_text

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "cat_imgs/")

    class Meta:
        verbose_name_plural = '2. Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width = "50" height = "50" />' % (self.image.url))

    def __str__(self):
        return self.title

class Branch(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "branch_imgs/")

    class Meta:
        verbose_name_plural = '3. Branches'

    def image_tag(self):
        return mark_safe('<img src="%s" width = "100" />' % (self.image.url))

    def __str__(self):
        return self.title


class Year(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "year_imgs/")

    class Meta:
        verbose_name_plural = '4. Years'

    def image_tag(self):
        return 

    def __str__(self):
        return self.title


class Domain(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "domain_imgs/")

    class Meta:
        verbose_name_plural = '5. Domains'

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
    is_featured = models.BooleanField(default= False)


    class Meta:
        verbose_name_plural = '6. Competitions'

    def __str__(self):
        return self.title
    

# Competition Attributes
class CompetitionAttribute(models.Model):
    competition = models.ForeignKey(Competition,on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    # reg_fee = models.ForeignKey(Competition, on_delete=models.CASCADE , related_name='reg_fees')
    reg_fee=models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = '7. CompetitionAttribute'

    def __str__(self):
        return self.competition.title 