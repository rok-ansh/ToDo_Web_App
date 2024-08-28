FILEPATH = 'todos.txt'


def web_get_todos(filepath=FILEPATH):
    with open("todos.txt", 'r') as file:
        local_todos = file.readlines()
    return local_todos


def web_write_todos(todos_arg, filepath=FILEPATH):
    with open("todos.txt", 'w') as file:
        write_todos = file.writelines(todos_arg)

# print()