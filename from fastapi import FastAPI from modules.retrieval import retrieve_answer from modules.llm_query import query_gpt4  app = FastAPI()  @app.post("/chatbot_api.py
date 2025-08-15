from fastapi import FastAPI
from modules.retrieval import retrieve_answer
from modules.llm_query import query_gpt4

app = FastAPI()

@app.post("/chat")
def chat(query: str):
    # First try retrieval
    answer = retrieve_answer(query)
    if answer:
        return {"answer": answer, "source": "KB"}
    # Else use GPT-4
    answer = query_gpt4(query)
    return {"answer": answer, "source": "LLM"}
