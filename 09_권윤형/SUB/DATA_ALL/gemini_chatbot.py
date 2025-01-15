import os
import google.generativeai as genai

genai.configure(api_key="API_KEY")

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
  ]
)

while True:
    user_input = input("질문을 입력하세요 (종료하려면 '종료' 입력): ")
    if user_input.lower() == "종료":
        break

    response = chat_session.send_message(user_input)
    print("Gemini:", response.text)