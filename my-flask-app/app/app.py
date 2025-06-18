from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
deployment = "gpt-3.5-turbo"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        question = request.form.get("question", "")
        prompt = f"""
You are an expert on the python language.

Whenever certain questions are asked, you need to provide response in below format.

- Concept
- Example code showing the concept implementation
- explanation of the example and how the concept is done for the user to understand better.

Provide answer for the question: {question}
"""
        messages = [{"role": "user", "content": prompt}]
        completion = client.chat.completions.create(model=deployment, messages=messages,temperature=1.0, max_completion_tokens=500)
        answer = completion.choices[0].message.content
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)