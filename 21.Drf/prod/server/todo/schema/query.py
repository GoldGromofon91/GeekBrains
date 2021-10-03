import graphene

from todo.models import Project, Todo
from todo.schema.type import ProjectType, TodoType


class TodoQueryProject(graphene.ObjectType):
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))
    all_todo = graphene.List(TodoType)

    def resolve_project_by_id(self, info, id):
        try:
            inst = Project.objects.get(id=id)
        except:
            return None
        return inst

    def resolve_all_todo(self, info):
        return Todo.objects.all()
