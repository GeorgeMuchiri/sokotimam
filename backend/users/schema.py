
import graphene
from graphene_django import DjangoObjectType
import graphql_jwt
from django.core.mail import EmailMessage
from django.conf import settings

from .models import NewUser

class NewUserType(DjangoObjectType):
    class Meta:
        model = NewUser

class Query(graphene.ObjectType):
    users = graphene.List(NewUserType)
    user_details = graphene.Field(NewUserType)

    def resolve_users(self, info):
        return NewUser.objects.all()

    def resolve_user_details(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user


class CreateUsers(graphene.Mutation):
    id = graphene.Int()
    username = graphene.String()
    firstname = graphene.String()
    lastname = graphene.String()
    email = graphene.String()
    phone =  graphene.String()
    address = graphene.String()
    password = graphene.String()

    class Arguments:
        username = graphene.String()
        firstname = graphene.String()
        lastname = graphene.String()
        email = graphene.String()
        phone =  graphene.String()
        address = graphene.String()
        password = graphene.String()

    def mutate(self, info, email, username, firstname, lastname, phone, password):
        users  = NewUser.objects.create_user(email=email, username = username, firstname=firstname, lastname=lastname, phone=phone,
        password = password)
        users.set_password(password)
        users.is_active = True
        users.save()

        welcome = EmailMessage(
            'Activate your account',
            f'Hello There {username}, \n Welcome to SokoTimam. You can login to your account now, \n If have any Querries, go ahead and contact us on admin@sokotimam.com  \n\n Thank you, \n Sokotimam Admin',
            settings.EMAIL_HOST_USER,
            [email],
        )
        welcome.fail_silently = False
        welcome.send()

        return CreateUsers(
            id=users.id,
            email=users.email,
            username = users.username,
            firstname = users.firstname,
            lastname = users.lastname,
            phone = users.phone,
            password = users.password,
            #address = users.address
        )

class Mutation(graphene.ObjectType):
    create_users = CreateUsers.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


