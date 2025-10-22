# backend/nlp/command_parser.py
from fuzzywuzzy import fuzz, process

# 🧠 Define your intent → phrase mappings
command_map = {
    "get_time": [
        "what time is it", "tell me the time", "time now", "current time",
        "what's the time", "show time"
    ],
    "open_youtube": [
        "open youtube", "launch youtube", "start youtube", "play youtube", "youtube"
    ],
    "open_whatsapp": [
        "open whatsapp", "launch whatsapp", "start whatsapp","whatsapp"
    ],
    "open_calculator": [
        "open calculator", "launch calculator", "start calculator"
    ],
    "get_weather": [
        "what's the weather", "current weather", "weather report", "weather now"
    ]
}

# Flatten all phrases for global matching
all_phrases = {phrase: intent for intent, phrases in command_map.items() for phrase in phrases}

def parse_command(user_input):
    """
    Matches user input to the most likely intent using fuzzy matching.
    Returns the best intent if similarity > threshold, else None.
    """
    user_input = user_input.lower().strip()

    # Find best match among all phrases
    best_match, score = process.extractOne(user_input, all_phrases.keys(), scorer=fuzz.token_sort_ratio)

    if score > 70:  # Adjust threshold based on testing
        return all_phrases[best_match]

    return None
