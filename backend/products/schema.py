import graphene
from graphene_django import DjangoObjectType
from .models import Product, Category, Subcategory

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image')

    def resolve_image(self, info):
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image


class CategoryType(DjangoObjectType):
    class  Meta:
        model = Category
        fields = ('id', 'name',  'img')

    def resolve_img(self, info):
        if self.img:
            self.img = info.context.build_absolute_uri(self.img.url)
        return self.img

class SubcategoryType(DjangoObjectType):
    class Meta:
        model = Subcategory
        fields = ('id', 'name')

        
class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_search = graphene.List(ProductType, name=graphene.String())
    all_categories  = graphene.List(CategoryType)
    product_details = graphene.Field(ProductType, id=graphene.ID())

    def resolve_all_products(root, info):
        return Product.objects.all()


    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_search(root, info, name):
        return Product.objects.filter(name__icontains=name)
    
    def resolve_product_details(root, info, id):
        return Product.objects.get(id=id)

        