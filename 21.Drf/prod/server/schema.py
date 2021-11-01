import graphene

from creator.schema.query import CreatorQueryProject
from creator.schema.mutation import CreatorMutationProject
from todo.schema.query import TodoQueryProject


class Mutation(CreatorMutationProject, graphene.ObjectType):
    pass


class Query(CreatorQueryProject,TodoQueryProject, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
