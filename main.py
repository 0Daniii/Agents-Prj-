print(">>> UPDATED MAIN.PY IS RUNNING <<<")

from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.summary_agent import SummaryAgent
from agents.review_agent import ReviewAgent

def main():
    topic = input("Enter research topic: ")

    researcher = ResearchAgent()
    analyst = AnalysisAgent()
    summarizer = SummaryAgent()
    reviewer = ReviewAgent()

    raw_data = researcher.run(topic)
    print(f"[DEBUG] Raw data length: {len(raw_data)}")

    insights = analyst.run(raw_data)
    print(f"[DEBUG] Extracted insights: {len(insights)}")

    summary = summarizer.run(insights)
    final_output = reviewer.run(summary)

    print("\n=== FINAL SUMMARY ===\n")
    print(final_output if final_output else "⚠️ No summary generated.")

if __name__ == "__main__":
    main()
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.summary_agent import SummaryAgent
from agents.review_agent import ReviewAgent

def main():
    topic = input("Enter research topic: ")

    researcher = ResearchAgent()
    analyst = AnalysisAgent()
    summarizer = SummaryAgent()
    reviewer = ReviewAgent()

    raw_data = researcher.run(topic)
    insights = analyst.run(raw_data)
    summary = summarizer.run(insights)
    final_output = reviewer.run(summary)

    print("\n=== FINAL SUMMARY ===\n")
    print(final_output)

if __name__ == "__main__":
    main()
