FILEPATH = "/Users/ronaldleon/PycharmProjects/todo-app/Main_app_code/todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file  and return list of
    to - do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in a text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


def enumerate_todos():
    for index, item in enumerate(todos, start=1):
        """enumerate and capitalizes all to dos"""
        item = item.capitalize()
        item = item.strip('\n')
        print(f"{index}- {item}")