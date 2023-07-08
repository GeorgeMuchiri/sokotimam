import graphene
import graphql_jwt

import users.schema
import adverts.schema
import products.schema
import stores.schema



class Query(stores.schema.Query, products.schema.Query, users.schema.Query, adverts.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, stores.schema.Mutation, graphene.ObjectType):
    token_auth  =  graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token  = graphql_jwt.Refresh.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()

    # Long running refresh tokens
    delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)