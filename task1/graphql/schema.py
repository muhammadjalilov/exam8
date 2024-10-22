import graphene

from task1.graphql.mutations import Mutation
from task1.graphql.queries import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
