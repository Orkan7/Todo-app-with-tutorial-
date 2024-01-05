# Bismillah



FILEPATH = "TextFiles/My_todo_list.txt"

def get_todos(filepath=FILEPATH):
    """
     :param filepath: Has the FILEPATH Variable (which containts the Filepath) as a default Argument
     :return: returns a List with the Items in My_todo_list.txt (as default, you can give other filepaths as Arguments).
     """
    with open(filepath, "r") as file_local:
        todo_List = file_local.readlines()
    return todo_List


def write_todos(todos_arg, filepath=FILEPATH):
    """
     :param todos_arg: todo to write in the My_todo_List.txt file
     :param filepath: Has the "TextFiles/My_todo_list.txt" filepath as an default Argument (as default, you can give other filepaths as Arguments)
     :return:
     """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
    print(__name__)
