from flask import Flask, render_template, request 
from post_details import PostDetails
from fallback_generator import CaptionGenerator
from openrouter_service import OpenRouterService
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv() 
fallback = CaptionGenerator()
api_key = os.getenv("OPENROUTER_API_KEY")
ai_service = OpenRouterService(api_key=api_key)

@app.route("/")
def home():
    return render_template("Fd.html")


@app.route("/generate", methods=["POST"])
def generate():
    topic = request.form.get("topic")
    platform = request.form.get("platform")
    tone = request.form.get("tone")

    # Create Post Object
    post = PostDetails(topic, platform, tone)

    try:
        # Try AI first
        caption = ai_service.generate_caption(post)

        if not caption:
            raise Exception("Empty AI response")

        source = "AI"

    except Exception as e:
        print("AI Error:", e)

        # Fallback if AI fails
        caption = fallback.generate_caption(post)
        source = "Fallback"

    # Send result back to HTML
    return render_template("Fd.html", caption=caption, source=source)


if __name__ == "__main__":
    app.run(debug=True)