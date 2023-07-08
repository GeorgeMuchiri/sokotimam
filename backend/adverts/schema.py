from pyexpat import model
import graphene
from graphene_django import DjangoObjectType

from .models import ImageAdverts


class AdvertImageType(DjangoObjectType):
    class Meta:
        model = ImageAdverts
        field = ('id','image', 'name')

    def resolve_image(self, info):
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image



class Query(graphene.ObjectType):
    image_advert = graphene.List(AdvertImageType)


    def resolve_image_advert(self, info):
        return ImageAdverts.objects.all()
        