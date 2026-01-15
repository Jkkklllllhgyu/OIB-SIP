from flask import Flask, render_template, request, jsonify
import datetime
import webbrowser
import requests
import spacy

app = Flask(__name__)


WEATHER_API_KEY = "6aeba540d4d1c10e451e48bf35550a33"


nlp = spacy.load("en_core_web_sm")


context = {
    "last_site": None
}


SITES = {
    "youtube": "https://www.youtube.com",
    "github": "https://www.github.com",
    "google": "https://www.google.com",
    "linkedin": "https://www.linkedin.com",
    "gmail": "https://mail.google.com"
}


def detect_intent(text):
    doc = nlp(text)

    if any(t.lemma_ in ["bye", "exit", "quit"] for t in doc):
        return "exit"

    if any(t.lemma_ == "open" for t in doc):
        return "open_site"

    if "weather" in text:
        return "weather"

    if any(t.lemma_ == "time" for t in doc):
        return "time"

    if any(t.lemma_ in ["date", "day"] for t in doc):
        return "date"

    if "who is" in text or "what is" in text or "tell me about" in text:
        return "wiki"

    if "how are you" in text:
        return "status"

    
    for ent in doc.ents:
        if ent.label_ == "GPE":
            return "weather"

    return "unknown"



def extract_city(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "GPE":
            return ent.text

    words = text.split()
    if "in" in words:
        idx = words.index("in")
        if idx + 1 < len(words):
            return words[idx + 1].title()

    return None


def extract_site(text):
    for site in SITES:
        if site in text:
            return site
    return None



def open_site(site):
    webbrowser.open(SITES[site])
    context["last_site"] = site
    return f"Opening {site.capitalize()}."


def get_weather(city):
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params=params
    )
    data = response.json()

    
    if data.get("cod") != 200:
        params["q"] = f"{city},IN"
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params=params
        )
        data = response.json()

    if data.get("cod") != 200:
        return "I couldn't find weather information for that city."

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"The weather in {city} is {desc} with {temp}°C."


def get_wikipedia_summary(query):
    query = query.strip().replace(" ", "_")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"

    headers = {
        "User-Agent": "VoiceAssistant/1.0 (educational project)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()

        if "extract" in data:
            return data["extract"]

        if data.get("type") == "https://mediawiki.org/wiki/HyperSwitch/errors/not_found":
            return "I couldn't find information on that topic."

        return "I couldn't find information on that topic."

    except requests.exceptions.RequestException as e:
        print("WIKI ERROR:", e)
        return "Wikipedia service is currently unavailable."




@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    text = request.json["command"].lower()
    intent = detect_intent(text)

    
    if intent == "exit":
        return jsonify(reply="Alright. Take care.")

   
    if intent == "open_site":
        site = extract_site(text)

        if site:
            return jsonify(reply=open_site(site))

        if "again" in text and context["last_site"]:
            return jsonify(reply=open_site(context["last_site"]))

        return jsonify(reply="Which site should I open?")

    
    if intent == "weather":
        city = extract_city(text)
        if not city:
            return jsonify(reply="Please tell me the city name.")
        return jsonify(reply=get_weather(city))

    
    if intent == "time":
        return jsonify(
            reply=datetime.datetime.now().strftime("It’s %I:%M %p.")
        )

    
    if intent == "date":
        return jsonify(
            reply=datetime.datetime.now().strftime("Today is %d %B %Y.")
        )

    
    if intent == "wiki":
        query = (
            text.replace("who is", "")
                .replace("what is", "")
                .replace("tell me about", "")
                .strip()
        )

        if not query:
            return jsonify(reply="Please tell me what you want to know about.")

        return jsonify(reply=get_wikipedia_summary(query))

    
    if intent == "status":
        return jsonify(reply="I'm doing well. Thanks for asking.")

    
    return jsonify(
        reply="I can open websites, tell weather, answer questions, and give time updates."
    )


if __name__ == "__main__":
    app.run(debug=True)
