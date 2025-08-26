class List:

    def __init__(self,name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


    def delete_task_by_index(self,index):

        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            return removed_task.name
        return None

    def list_tasks(self):
        return [f"{task.name}" for task in self.tasks]

class Task:
    def __init__(self,name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other,Task):
            return self.name == other.name
        return False



def main():
    to_do_list = List("To Do List by Hüseyin Yeter")
    is_running = True
    while is_running:
        print("*" * 30)
        print(to_do_list.name)
        print("*" * 30)
        print("1.Add Task")
        print("2.Delete Task")
        print("3.List Tasks")
        print("4.Exit")
        choice = input("What is your choice ? : ")

        if choice == "1":

            while True:

                task = input("Enter a task # to back to main menu 'menu': ")
                if task.lower() != "menu":
                    task_class = Task(task)
                    to_do_list.add_task(task_class)
                    print(f"✓ {task_class.name} has successfully added")
                elif task.lower() == "menu":
                    break


        elif choice == "2":
            while True:

                if not to_do_list.tasks:
                    print("The list is empty!")
                    break

                else:
                    print("\nCurrent tasks:")
                    for i,task in enumerate(to_do_list.tasks,1):
                        print(f"{i}.{task.name}")

                task_number = input("Enter a task number you want to delete # for back 'menu': ")
                if task_number.lower() != "menu":
                    deleted_task = to_do_list.delete_task_by_index(int(task_number)-1)
                    if deleted_task:
                        print(f" {deleted_task} has been successfully deleted")
                    else:
                        print(f"Invalid task number. Please enter a number between 1-{len(to_do_list.tasks)}")
                else:
                    break

        elif choice == "3":
            if to_do_list.tasks:

                for i,task in enumerate(to_do_list.list_tasks(),1):
                    print(f"{i}.{task}")

                print()
            else:
                print("The list is empty")
                print()

        elif choice == "4":
            print("Closed")
            break

        else:
            print("Invalid value.Please choose 1-4")


if __name__ == '__main__':
    main()





