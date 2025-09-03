class AutonomousAgent:
    def __init__(self, goal):
        self.goal = goal
        self.steps = []

    def plan(self):
        self.steps = [
            f"Step 1: Research {self.goal}",
            f"Step 2: Analyze data for {self.goal}",
            f"Step 3: Execute tasks to achieve {self.goal}"
        ]

    def execute(self):
        for step in self.steps:
            print(f"{step}")

if __name__ == "__main__":
    agent = AutonomousAgent("Plan a 3-day AI workshop")
    agent.plan()
    agent.execute()
