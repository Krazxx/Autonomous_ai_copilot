from agents.chat_agent import ChatAgent
from agents.rag_agent import RAGAgent
from agents.decision_agent import DecisionAgent
from agents.automation_agent import AutomationAgent   


class AgentRouter:

    def __init__(self):
        self.chat = ChatAgent()
        #self.browser = BrowserAgent()
        self.rag = RAGAgent()
        self.decision = DecisionAgent()
        self.automation = AutomationAgent()   

    def route(self, message: str) -> str:

        agent_type = self.decision.decide(message)

        print("ROUTED TO:", agent_type)  # debug

        if agent_type == "rag":
            return self.rag.respond(message)

        if agent_type == "automation":
            return self.automation.respond(message)   
        
        if agent_type == "browser":
            return "⚠️ Browser automation not supported in deployed version"

        return self.chat.respond(message)