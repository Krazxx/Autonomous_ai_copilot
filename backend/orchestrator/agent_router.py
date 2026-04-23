from agents.chat_agent import ChatAgent
from agents.rag_agent import RAGAgent
from agents.decision_agent import DecisionAgent
from agents.automation_agent import AutomationAgent
import urllib.parse


class AgentRouter:

    def __init__(self):
        self.chat = ChatAgent()
        self.rag = RAGAgent()
        self.decision = DecisionAgent()
        self.automation = AutomationAgent()

    # ✅ music function (FIXED)
    def play_song_web(self, query: str):
        q = urllib.parse.quote_plus(query)
        return {
            "type": "music",
            "url": f"https://www.youtube.com/results?search_query={q}"
        }

    def route(self, message: str):

        agent_type = self.decision.decide(message)

        print("ROUTED TO:", agent_type)

        if agent_type == "rag":
            return self.rag.respond(message)

        if agent_type == "automation":
            return self.automation.respond(message)

        # ✅ NEW: music routing
        if agent_type == "music":
            return self.play_song_web(message)

        if agent_type == "browser":
            return "⚠️ Browser automation not supported in deployed version"
        print("ROUTED TO:", agent_type)

        return self.chat.respond(message)
       