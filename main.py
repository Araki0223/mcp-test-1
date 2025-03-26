from fastapi import FastAPI, HTTPException
from schemas import MCPRequest, MCPResponse
from context_manager import update_context
from model_adapter import call_openai

app = FastAPI()

@app.post("/mcp", response_model=MCPResponse)
def mcp_endpoint(request: MCPRequest):
    try:
        # 文脈更新（履歴に新しいメッセージを追加）
        messages = update_context(request.thread_id, request.messages)

        # モデル呼び出し
        temperature = request.context.get("temperature", 0.7)
        result = call_openai(messages, temperature=temperature)

        return MCPResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
