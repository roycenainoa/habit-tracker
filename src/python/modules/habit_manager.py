class HabitManager:
    def __init__(self):
        self.habits = []

    def add_habit(self, name):
        self.habits.append(name)

    def list_habits(self):
        return self.habits
