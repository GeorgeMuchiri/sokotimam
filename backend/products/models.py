from django.db import models


class Category(models.Model):
    name  = models.CharField(max_length=250)
    img = models.ImageField(upload_to='./images/', default="./images/default_image.png")

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
        

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    product_uuid = models.CharField(max_length=250, null=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory  = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="./images", default="./images/default_image.png")


    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    pass

class ProductSpecification(models.Model):
    pass


class ProductType(models.Model):
    pass

