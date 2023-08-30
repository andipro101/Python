#To-Do List: Develop a console-based to-do list application that allows users to add tasks, mark them as completed, and remove tasks from the list.

Tasks = []
TasksComplete = []
Run = "Yes"

while Run == "Yes":
    Task = input("Enter Task: ")
    Tasks.append(Task)
    TaskComplete = input("Is the task Completed: ")
    if TaskComplete == "Yes":
        TasksComplete.append(": Complete")
    else:
        TasksComplete.append(": Not Complete")
    
    Run = input("\nIf you want to enter another type Yes: ")


res = "\n".join("{} {}".format(x, y) for x, y in zip(Tasks, TasksComplete))
print ("\nThis are your Tasks")
print (res)

do_remove = input("\nDo you want to remove a task:")

if do_remove == "Yes":
    while do_remove == "Yes":
        Removed_Task = input("Which task do you want removed: ")
        Tasks.remove(Removed_Task)
        do_remove = input("Do you want to remove another task:\n")

res = "\n".join("{} {}".format(x, y) for x, y in zip(Tasks, TasksComplete))
print ("\nThis are your Tasks")
print (res)




