import requests

class ResearchAgent:
    def run(self, topic):
        topic = topic.strip().replace(" ", "_").lower()

        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"

        headers = {
            "User-Agent": "AutomatedResearchAgent/1.0 (Academic Project)"
        }

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print("[ResearchAgent] Wikipedia request failed.")
            return ""

        data = response.json()

        extract = data.get("extract", "")
        if not extract:
            print("[ResearchAgent] No extract found.")
            return ""

        print("[ResearchAgent] Extract retrieved successfully.")
        return extract
import requests
from bs4 import BeautifulSoup

class ResearchAgent:
    def run(self, topic):
        query = topic.replace(" ", "_")
        url = f"https://en.wikipedia.org/wiki/{query}"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return "No data found."

        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.select("p")
        text = " ".join(p.get_text() for p in paragraphs[:5])
        return text
