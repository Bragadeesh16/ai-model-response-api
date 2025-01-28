from celery import shared_task
import google.generativeai as genai
import os
from .models import AiResponse
import time


@shared_task
def get_ai_response(prompt):
    start_time = time.time() 
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
            {"role": "user", "parts": ["hii\n"]},
            {"role": "model", "parts": ["Hi there! How can I help you today?\n"]},
            {"role": "user", "parts": ["write some python code\n"]},
            {"role": "model", "parts": ["What kind of Python code would you like me to write? I can do many things, such as:\n\n..."]},
        ]
    )

    try:
        response = chat_session.send_message(prompt)
        end_time = time.time()
        time_taken = end_time - start_time
        print(time_taken)

        if response and response.text:
            data = {
                 "response": response.text,
                 "time_taken": time_taken
            }
            return {"status": "success","data":data}
        else:
            return {"status": "error", "message": "No response text received."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
