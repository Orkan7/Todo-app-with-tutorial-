#Bismillah



import Modulescripts.functionsforMain as Functions
import PySimpleGUI as GUI

label = GUI.Text("Type in a to-do")
input_box = GUI.InputText(tooltip="Enter todo")
Button = GUI.Button("Add")

Window = GUI.Window("My To-Do App", layout=[[[label], input_box, Button]])
Window.read()
Window.close()
