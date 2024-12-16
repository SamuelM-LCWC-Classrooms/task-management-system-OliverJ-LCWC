class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority):
        self.tasks.append({
            'title': title,
            'description': description,
            'priority': priority,
            'status': 'Incomplete'
        })

    def remove_task(self, title):
        task_found = False
        for task in self.tasks:
            if task["title"] == title:
                self.tasks.remove(task)
                task_found = True
                print(f"The task '{title}' has been removed.")
                break
        if not task_found:
            print(f"Task with title '{title}' does not exist.")

    def mark_complete(self, title):
        task_found = False
        for task in self.tasks:
            if task['title'] == title:
                task['status'] = 'Complete'
                task_found = True
                print(f"Task '{title}' has been marked as complete.")
                break
        
        if not task_found:
            print(f"Task '{title}' not found.")
    
    def view_tasks(self, sort_by="priority"):
        exit
    
    def search_task(self, title):
        exit