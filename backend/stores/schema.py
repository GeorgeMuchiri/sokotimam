from dataclasses import fields
from pydoc import describe

import graphene
from graphene_django import DjangoObjectType
from users.models import NewUser

from .models import Products, Store
#from graphene_file_upload.scalars import Upload

class ProductsType(DjangoObjectType):
    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'description', 'owner',)

    # def resolve_image(self, info):
    #     if self.image:
    #         self.image = info.context.build_absolute_uri(self.image.url)
    #     return self.image

    # def resolve_image_2(self, info):
    #     if self.image_2:
    #         self.image_2 = info.context.build_absolute_uri(self.image_2.url)
    #     return self.image_2



class StoreType(DjangoObjectType):
    class Meta:
        model = Store
        fields =('id', 'name', 'description', 'owner')


class Query(graphene.ObjectType):
    store_details = graphene.Field(StoreType, id=graphene.ID())
    store_products = graphene.List(ProductsType, owner=graphene.ID())
    all_product = graphene.List(ProductsType)


    def resolve_store_details(root, info, id):
        return Store.objects.get(id=id)


    def resolve_store_products(root, info, owner):
        return Products.objects.filter(owner=owner)

    def resolve_all_product(root, info):
        return Products.objects.all()


class Createprods(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    price = graphene.String()
    #owner = graphene.String()
   
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        price = graphene.String()
        owner = graphene.String()
        

    def mutate(self, info,  name, description, price):

        
        prods  = Products(name=name, description=description, price=price, )
        
        prods.save()

        

        return Createprods(
            id=prods.id,
            name = prods.name,
            description = prods.description,
            price = prods.price,
        )

class Mutation(graphene.ObjectType):
    create_products = Createprods.Field()