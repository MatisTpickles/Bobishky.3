from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form.get("message")
    
    if not user_message:
        return "Aucun message reçu.", 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es Bobishky.3, un assistant sarcastique, drôle mais utile."},
                {"role": "user", "content": user_message}
            ]
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        return f"Erreur de l'IA : {e}", 500
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx

