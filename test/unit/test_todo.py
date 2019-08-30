from todo import Todo

def test_build(todo):
    assert isinstance(todo, Todo)
    assert isinstance(todo.name, str)
