class AnalysisAgent:
    def run(self, text):
        sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 30]
        return sentences
class AnalysisAgent:
    def run(self, text):
        sentences = text.split(".")
        key_points = [s.strip() for s in sentences if len(s.strip()) > 60]
        return key_points[:5]
