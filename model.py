from nltk.sentiment import SentimentIntensityAnalyzer
import random

sia = SentimentIntensityAnalyzer()

positive_words = ["happy","good","great","awesome","love","excited","fine","okay"]
negative_words = ["sad","bad","depressed","angry","stress","tired","upset","hate","nothing"]

def analyze_emotion(text):
    text_lower = text.lower()

    # 🔥 Strong rules
    if "nothing is going good" in text_lower or "not going well" in text_lower:
        return "negative"

    if "i am fine" in text_lower or "i am okay" in text_lower:
        return "neutral"

    score = sia.polarity_scores(text)
    compound = score['compound']

    pos = sum(word in text_lower for word in positive_words)
    neg = sum(word in text_lower for word in negative_words)

    final = compound + (pos * 0.2) - (neg * 0.3)

    if final >= 0.3:
        return "positive"
    elif final <= -0.2:
        return "negative"
    else:
        return "neutral"


def get_response(emotion, text):

    positive = [
        "😄 That's great! Keep going!",
        "🔥 Awesome vibe!",
        "✨ You're doing amazing!"
    ]

    negative = [
        "😔 Stay strong, things will improve.",
        "💔 I'm here for you.",
        "🌧️ Tough times pass."
    ]

    neutral = [
        "🙂 Okay, tell me more.",
        "🤔 I see.",
        "👍 Got it."
    ]

    if emotion == "positive":
        return random.choice(positive)
    elif emotion == "negative":
        return random.choice(negative)
    else:
        return random.choice(neutral)