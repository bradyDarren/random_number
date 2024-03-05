class Tasks:

    def __init__(self, task_name, description, due_date, completion_status):
        self.task_name = task_name
        self.description = description
        self.due_date = due_date
        self.completion_status = completion_status

    def add_task(self, task_name, description, due_date, completions_status):
        print("Task", task_name, "has been added with the following attributes:"
                               "\n Description:", description,
                               "\n Due Date:", due_date,
                               "\n Completion Status:", completions_status + ".")

    def remove(self, task_name):
        print("Task", task_name, "has been removed")

    def update(self):
        pass

    def display(self, task_name):
        print("Task:", task_name, "\n Description:", self.description, "\n Due Date:", self.due_date,
              "\n Completion Status:", self.completion_status)


