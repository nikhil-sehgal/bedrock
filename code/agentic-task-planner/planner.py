import datetime

class AgenticPlanner:
    def __init__(self):
        self.tasks = []

    def add_task(self, goal, deadline):
        self.tasks.append({"goal": goal, "deadline": deadline})

    def show_plan(self):
        for task in self.tasks:
            print(f"🎯 {task['goal']} (Deadline: {task['deadline']})")

if __name__ == "__main__":
    planner = AgenticPlanner()
    planner.add_task("Research GenAI use cases", datetime.date(2025, 9, 1))
    planner.add_task("Write blog on Agentic AI", datetime.date(2025, 9, 3))
    planner.show_plan()
