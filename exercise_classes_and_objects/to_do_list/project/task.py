class Task:
# This is the task class
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):

        if not self.name == new_name:
            self.name = new_name
            return self.name

        return "Name cannot be the same."

    def change_due_date(self, new_date):

        if not self.due_date == new_date:
            self.due_date = new_date
            return self.due_date

        return "Date cannot be the same."

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number, new_comment):

        if 0 <= comment_number <= len(self.comments) - 1:
            self.comments.pop(comment_number)
            self.comments.insert(comment_number, new_comment)

            return ', '.join([x for x in self.comments])

        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
