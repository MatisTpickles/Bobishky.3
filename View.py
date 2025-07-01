from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

@csrf_exempt
def ask_bobishky(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            message = data.get("message", "")

            if not message:
                return JsonResponse({"error": "Aucun message reçu."}, status=400)

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tu es Bobishky.3, une IA sarcastique et drôle."},
                    {"role": "user", "content": message}
                ]
            )
            answer = response.choices[0].message.content.strip()
            return JsonResponse({"response": answer})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Méthode non autorisée."}, status=405)
