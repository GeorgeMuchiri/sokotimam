



from django.db import models
from users.models import NewUser


class Category(models.Model):
    name  = models.CharField(max_length=250)
    img = models.ImageField(upload_to='./images/', default="./images/default_image.png")
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    

    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE)
   

    class Meta:
        verbose_name_plural = 'Stores'


    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.CharField(max_length=255) 
    owner = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    #subcategory  = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=True)
    # image = models.ImageField(upload_to="./images", default="./images/default_image.png")
    # image_2 = models.ImageField(upload_to="./images", null=True)
    # image_3 = models.ImageField(upload_to="./images", null=True)
    # image_4 = models.ImageField(upload_to="./images", null=True)
    # image_5 = models.ImageField(upload_to="./images", null=True)
    

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name



