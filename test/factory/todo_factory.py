import factory
from todo import Todo

class TodoFactory(factory.Factory):

    class Meta:
        model = Todo

    name = "Charles Dickens"
