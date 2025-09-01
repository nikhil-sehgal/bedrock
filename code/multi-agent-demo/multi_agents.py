class ResearchAgent:
    def act(self, topic):
        return f"Researched data about {topic}"

class WriterAgent:
    def act(self, content):
        return f"Wrote summary: {content}"

class CoordinatorAgent:
    def __init__(self):
        self.researcher = ResearchAgent()
        self.writer = WriterAgent()

    def run(self, topic):
        data = self.researcher.act(topic)
        return self.writer.act(data)

if __name__ == "__main__":
    coordinator = CoordinatorAgent()
    result = coordinator.run("Agentic AI")
    print(result)
