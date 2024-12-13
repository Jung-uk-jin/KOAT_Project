from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import openai


openai.api_key = 'sk-...4WgA'  # 여기에 API 키를 넣어주세요.

@csrf_exempt
def chatbot_reply(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')

            if not user_message:
                return JsonResponse({"error": "No message provided"}, status=400)

            # OpenAI API 호출
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}]
            )

            bot_reply = response['choices'][0]['message']['content']
            return JsonResponse({"reply": bot_reply})

        except Exception as e:
            return JsonResponse({"error": f"Error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)



def chat_page(request):
    return render(request, 'chat.html')
