import graphene

class ProjectAdd(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    errors = graphene.String()

    @staticmethod
    def mutate(self, info, path, like):
        pass

class CreatorMutationProject(graphene.ObjectType):
    add_project = ProjectAdd.Field()