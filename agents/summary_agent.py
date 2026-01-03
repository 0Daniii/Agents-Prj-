class SummaryAgent:
    def run(self, key_points):
        return "\n".join(f"- {point}." for point in key_points)