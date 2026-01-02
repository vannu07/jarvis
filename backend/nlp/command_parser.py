# backend/nlp/command_parser.py
from fuzzywuzzy import fuzz, process

# 🧠 Define your intent → phrase mappings
command_map = {
    "get_time": [
        "what time is it",
        "tell me the time",
        "time now",
        "current time",
        "what's the time",
        "show time",
        "time please",
        "give me the time",
        "what is the time",
        "can you tell me the time",
        "whats the current time",
        "show me the time",
    ],
    "get_date": [
        "what's the date",
        "what is the date",
        "tell me the date",
        "date today",
        "today's date",
        "current date",
        "what date is it",
        "show date",
        "give me the date",
        "date please",
    ],
    "open_youtube": [
        "open youtube",
        "launch youtube",
        "start youtube",
        "play youtube",
        "youtube",
        "go to youtube",
        "take me to youtube",
        "show me youtube",
        "open yt",
        "launch yt",
    ],
    "open_whatsapp": [
        "open whatsapp",
        "launch whatsapp",
        "start whatsapp",
        "whatsapp",
        "open whatsup",
        "launch whatsup",
        "go to whatsapp",
        "take me to whatsapp",
    ],
    "open_calculator": [
        "open calculator",
        "launch calculator",
        "start calculator",
        "calculator",
        "open calc",
        "launch calc",
        "start calc",
        "calc",
    ],
    "get_weather": [
        "what's the weather",
        "current weather",
        "weather report",
        "weather now",
        "tell me the weather",
        "how's the weather",
        "weather today",
        "weather forecast",
        "show weather",
        "weather conditions",
        "what is the weather",
        "weather outside",
    ],
    "search_google": [
        "search for",
        "google search",
        "look up",
        "find on google",
        "google for",
        "search google",
        "can you search",
        "look for",
        "find information about",
    ],
    "play_music": [
        "play music",
        "play some music",
        "start music",
        "music please",
        "play songs",
        "play a song",
        "listen to music",
        "put on music",
    ],
    "get_news": [
        "news",
        "tell me the news",
        "what's the news",
        "news today",
        "latest news",
        "current news",
        "news headlines",
        "show me the news",
        "read the news",
    ],
    "open_browser": [
        "open browser",
        "launch browser",
        "start browser",
        "open web browser",
        "launch web browser",
    ],
    "take_screenshot": [
        "take a screenshot",
        "screenshot",
        "capture screen",
        "screen capture",
        "take screenshot",
        "snap screen",
    ],
    "shutdown": [
        "shutdown",
        "shut down",
        "power off",
        "turn off computer",
        "shutdown computer",
        "shutdown system",
    ],
    "restart": [
        "restart",
        "reboot",
        "restart computer",
        "reboot computer",
        "restart system",
        "reboot system",
    ],
}

# Flatten all phrases for global matching
all_phrases = {
    phrase: intent for intent, phrases in command_map.items() for phrase in phrases
}


def parse_command(user_input):
    """
    Matches user input to the most likely intent using fuzzy matching.
    Returns the best intent if similarity > threshold, else None.
    
    Args:
        user_input (str): The user's command text
        
    Returns:
        str: The matched intent name, or None if no match found
    """
    if not user_input:
        return None
        
    user_input = user_input.lower().strip()

    # Find best match among all phrases
    best_match, score = process.extractOne(
        user_input, all_phrases.keys(), scorer=fuzz.token_sort_ratio
    )

    # Lower threshold to 65 for better fuzzy matching of misspellings
    if score >= 65:
        return all_phrases[best_match]

    return None


def get_all_intents():
    """
    Returns a list of all available intents.
    
    Returns:
        list: List of intent names
    """
    return list(command_map.keys())


def get_phrases_for_intent(intent):
    """
    Returns all phrases mapped to a specific intent.
    
    Args:
        intent (str): The intent name
        
    Returns:
        list: List of phrases for that intent, or empty list if not found
    """
    return command_map.get(intent, [])
