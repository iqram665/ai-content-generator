import json
import os
from datetime import datetime

from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY", "")
SAVE_FILE = "saved_results.json"


def load_saved_results():
    if not os.path.exists(SAVE_FILE):
        return []
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return []


def save_result(entry):
    items = load_saved_results()
    items.insert(0, entry)
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=2)


@app.route("/", methods=["GET", "POST"])
def index():
    title = ""
    description = ""
    prompt = ""
    language = "english"
    result = ""
    status = ""
    saved = load_saved_results()

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        prompt = request.form.get("prompt", "").strip()
        language = request.form.get("language", "english")

        if not title or not prompt:
            status = "Title and topic are required to generate content."
        else:
            try:
                content_prompt = (
                    f"Write a detailed, engaging article titled '{title}'. "
                    f"Description: {description}. " if description else ""
                )
                content_prompt += f"Topic: {prompt}."
                if language == "bengali":
                    content_prompt += " Write the content in Bengali (বাংলা)."

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful AI content writer."},
                        {"role": "user", "content": content_prompt},
                    ],
                    max_tokens=800,
                    temperature=0.7,
                )
                result = response.choices[0].message["content"].strip()
                saved_entry = {
                    "title": title,
                    "description": description,
                    "prompt": prompt,
                    "language": language,
                    "content": result,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
                save_result(saved_entry)
                status = "Content generated and saved successfully."
                saved = load_saved_results()
            except Exception as error:
                result = f"Error generating content: {error}"
                status = "There was an error while generating content."

    return render_template(
        "index.html",
        title=title,
        description=description,
        prompt=prompt,
        language=language,
        result=result,
        status=status,
        saved=saved,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
