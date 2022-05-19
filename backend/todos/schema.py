import graphene
from graphene_django import DjangoObjectType

from projects.models import Project
from todos.models import Todo
from users.models import User


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password',)


class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)

    def resolve_all_todos(self, info):
        return Todo.objects.all()

    all_users = graphene.List(UserType)

    def resolve_all_users(self, info):
        return User.objects.all()

    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(self, info):
        return Project.objects.all()

    todo_by_status = graphene.List(TodoType, status=graphene.String(required=False))

    def resolve_todo_by_status(self, info, status=None):
        if not status:
            return Todo.objects.all()
        return Todo.objects.filter(status=status)

    projects_by_user = graphene.List(ProjectType, username=graphene.String(required=False))

    def resolve_projects_by_user(self, info, username=None):
        projects = Project.objects.all()
        if username:
            projects = projects.filter(users__username=username)
        return projects


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, first_name, last_name, email):
        user = User(username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email)
        user.save()
        return cls(user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.Int(required=True)
        username = graphene.String(required=False)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        email = graphene.String(required=False)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, pk, username=None, first_name=None, last_name=None, email=None):
        user = User.objects.get(pk=pk)
        if username:
            user.username = username
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if username and first_name and last_name and email:
            user.save()
        return cls(user)


class Mutation(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
