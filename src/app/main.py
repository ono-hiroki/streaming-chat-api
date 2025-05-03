from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from openai import OpenAI

client = OpenAI()
app = FastAPI()

def openai_stream_generator(messages: list[dict[str, str]]):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        stream=True,
        messages=messages,
    )
    for chunk in response:
        delta = chunk.choices[0].delta
        if hasattr(delta, "content") and delta.content:
            yield f"data: {delta.content}\n\n"

    yield "event: done\ndata: [DONE]\n\n"

@app.post("/v1/chat/stream", status_code=200)
async def chat_stream(request: Request):
    body = await request.json()
    messages = body.get("messages", [])

    generator = openai_stream_generator(messages)
    return StreamingResponse(generator, media_type="text/event-stream")