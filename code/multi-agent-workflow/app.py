class Agent:
    def __init__(self, name):
        self.name = name

    def run(self, task):
        return f"{self.name} executed: {task}"

class Workflow:
    def __init__(self):
        self.agents = [
            Agent("Research Agent"),
            Agent("Analysis Agent"),
            Agent("Visualization Agent"),
            Agent("Coordinator Agent")
        ]

    def execute(self, tasks):
        results = []
        for agent, task in zip(self.agents, tasks):
            results.append(agent.run(task))
        return results

if __name__ == "__main__":
    workflow = Workflow()
    tasks = [
        "Collect data from news sites",
        "Summarize insights",
        "Create charts",
        "Coordinate final report"
    ]
    print("\n".join(workflow.execute(tasks)))
