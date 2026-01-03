class ReviewAgent:
    def run(self, summary):
        return summary.replace("..", ".").strip()