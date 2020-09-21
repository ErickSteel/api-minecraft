import graphene
import graphql_jwt
from apps.aplicaciones import schema

class Query(schema.Query, graphene.ObjectType):
    pass

class Mutation(schema.Mutation, graphene.ObjectType):
	pass

schema = graphene.Schema(query=Query, mutation=Mutation)