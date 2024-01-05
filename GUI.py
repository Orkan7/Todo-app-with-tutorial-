#Bismillah



import Modulescripts.functionsforMain as Functions
import PySimpleGUI as GUI

label = GUI.Text("Type in a to-do")
input_box = GUI.InputText(tooltip="Enter todo", key="todo")
Button = GUI.Button("Add")

Window = GUI.Window("My To-Do App",
                    layout=[[label], [input_box, Button]],
                    font=("Helvetica", 20))


while True:
    Event, value = Window.read()
    print(Event)
    print(value)
    match Event:
        case "Add":
            todos = Functions.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
        case GUI.WIN_CLOSED:
            break

Window.close()
