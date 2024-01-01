#Bismillah



import Modulescripts.functionsforMain as function
import time

print("it is",time.strftime("%dth %b %Y: %H:%M:%S"))

#from functionsforMain import *

while True:
     User_Decision = input("Wanna add, show/display, config, remove or exit the list? : \n ")
     User_Decision = User_Decision.strip()


     if User_Decision.startswith("add") :
          todo = User_Decision[4:]

          todo_List = function.get_todos()

          todo_List.append(todo + "\n")

          function.write_todos(todo_List)



     elif User_Decision.startswith("show"):
          print("\n")

          todo_List = function.get_todos()


          for i, item in enumerate(todo_List):
               print(f"{i + 1}.{item.title()}")
          print("\n")
          print(f"The lengh of the List is: ", len(todo_List))
          print(type(todo_List))

     elif User_Decision.startswith("config"):
          try:
               x = int(User_Decision[7:]) - 1
               print(type(x))

               newtodo = input("Please Enter your new Todo: \n")

               todo_List = function.get_todos()

               todo_List[x] = newtodo

               file = open("TextFiles/My_todo_list.txt", "w")
               file.writelines(todo_List)
               file.close()

          except ValueError:
               print("Please write the index-Number")
               continue
          except IndexError:
               print("You do not have that many Todos")
               continue

     elif User_Decision.startswith("exit") :
          break

     elif User_Decision.startswith("remove"):
          try:
               index = int(User_Decision[7:]) - 1

               todo_List = function.get_todos()

               removedtodo = todo_List.pop(index)

               function.write_todos(todo_List)

               message = f"Todo '{removedtodo}' was removed from the list!"
               print(message.strip("\n"))

          except ValueError:
               print("Please type an Number")
               continue
     else:
          print("Falsche Eingabe.")





print("Bye!")
