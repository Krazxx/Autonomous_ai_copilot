from ninja import Router, Schema
from agents.chat_agent import ChatAgent
from agents.rag_agent import RAGAgent
from rag.vector_store import add_document
from orchestrator.agent_router import AgentRouter

router_engine = AgentRouter()


router = Router()

chat_agent = ChatAgent()
rag_agent = RAGAgent()


# ---------- Schema ----------
class ChatRequest(Schema):
    message: str


class UploadRequest(Schema):
    text: str


# ---------- Normal Chat ----------
@router.post("/chat")
def chat(request, payload: ChatRequest):

    message = payload.message
    response = chat_agent.respond(message)

    return {"response": response}


# ---------- RAG Chat ----------
@router.post("/rag")
def rag_chat(request, payload: ChatRequest):

    try:
        response = rag_agent.respond(payload.message)
        return {"response": response}

    except Exception as e:
        print("RAG ERROR:", str(e))   # 👈 see error in terminal
        return {"response": f"Backend error: {str(e)}"}


# ---------- Upload PDF ----------
@router.post("/upload")
def upload(request, payload: UploadRequest):   # ✅ FIXED HERE

    text = payload.text

    print("UPLOAD HIT")
    print("TEXT LENGTH:", len(text) if text else 0)

    if not text:
        return {"error": "No text received"}

    add_document(text)

    return {"status": "stored"}

@router.post("/copilot")
def copilot(request, payload: ChatRequest):

    try:
        response = router_engine.route(payload.message)
        return {"response": response}

    except Exception as e:
        print("COPILOT ERROR:", str(e))
        return {"response": f"Error: {str(e)}"}