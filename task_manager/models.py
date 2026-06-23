from datetime import date


class Task:
    def __init__(self ,title , priority = "Medium", due_date = None):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.done = False

    def to_dict(self):
        return{
            "title" : self.title,
            "priority" : self.priority,
            "done" : self.done,
            "due_date" : self.due_date
        }
