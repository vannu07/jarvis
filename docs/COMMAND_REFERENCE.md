# Natural Language Parsing - Command Reference

This document describes the enhanced natural language parsing capabilities of Jarvis.

## Overview

Jarvis now supports flexible command recognition with:
- **Synonym support**: Multiple ways to phrase the same command
- **Fuzzy matching**: Handles common misspellings and typos
- **Natural variations**: Understands commands with extra words like "please", "can you", etc.

## Supported Commands

### 1. Time Queries (`get_time`)
Ask Jarvis for the current time using any of these phrases:
- "what time is it"
- "tell me the time"
- "time now"
- "current time"
- "what's the time"
- "show time"
- "time please"
- "give me the time"
- And more variations...

**Example misspellings handled**: "wat time is it", "tel me the time"

---

### 2. Date Queries (`get_date`)
Get today's date:
- "what's the date"
- "tell me the date"
- "date today"
- "today's date"
- "current date"
- "what date is it"
- And more variations...

---

### 3. Open YouTube (`open_youtube`)
Launch YouTube:
- "open youtube"
- "launch youtube"
- "start youtube"
- "youtube"
- "go to youtube"
- "take me to youtube"
- And more variations...

**Example misspellings handled**: "opne youtube", "launche youtube"

---

### 4. Open WhatsApp (`open_whatsapp`)
Launch WhatsApp:
- "open whatsapp"
- "launch whatsapp"
- "start whatsapp"
- "whatsapp"
- "go to whatsapp"

**Example misspellings handled**: "whatsaap", "open whatsup"

---

### 5. Open Calculator (`open_calculator`)
Launch the calculator:
- "open calculator"
- "launch calculator"
- "calculator"
- "calc"
- "open calc"

**Example misspellings handled**: "calculater"

---

### 6. Weather Queries (`get_weather`)
Get weather information:
- "what's the weather"
- "current weather"
- "weather report"
- "weather now"
- "tell me the weather"
- "how's the weather"
- "weather today"
- And more variations...

**Example misspellings handled**: "weatherr", "currrent weather"

---

### 7. Google Search (`search_google`)
Search on Google:
- "search for [query]"
- "google search [query]"
- "look up [query]"
- "search google [query]"
- And more variations...

---

### 8. Play Music (`play_music`)
Start music playback:
- "play music"
- "play some music"
- "start music"
- "music please"
- "play songs"
- And more variations...

**Example misspellings handled**: "plaay music"

---

### 9. Get News (`get_news`)
Get latest news:
- "news"
- "tell me the news"
- "what's the news"
- "news today"
- "latest news"
- "current news"
- And more variations...

**Example misspellings handled**: "newws"

---

### 10. Open Browser (`open_browser`)
Launch web browser:
- "open browser"
- "launch browser"
- "start browser"
- "open web browser"

---

### 11. Take Screenshot (`take_screenshot`)
Capture the screen:
- "take a screenshot"
- "screenshot"
- "capture screen"
- "screen capture"
- "snap screen"

---

### 12. Shutdown (`shutdown`)
Shutdown the system:
- "shutdown"
- "shut down"
- "power off"
- "turn off computer"
- "shutdown computer"

---

### 13. Restart (`restart`)
Restart the system:
- "restart"
- "reboot"
- "restart computer"
- "reboot computer"

---

## Technical Details

### Fuzzy Matching Threshold
- The parser uses a similarity threshold of **60%** for fuzzy matching
- This allows for common misspellings while avoiding false positives
- Uses `fuzzywuzzy` library with `token_sort_ratio` scoring

### Testing
The command parser has been thoroughly tested with:
- 78 unit tests covering exact matches, synonyms, misspellings, case sensitivity, whitespace handling, and edge cases
- All tests passing with 100% success rate
- Integration tests confirming proper interaction with the feature module

### Adding New Commands

To add a new command:

1. Edit `backend/nlp/command_parser.py`
2. Add a new entry to the `command_map` dictionary:
   ```python
   "your_intent_name": [
       "phrase 1",
       "phrase 2",
       "phrase 3",
       # Add more variations
   ],
   ```
3. Update `backend/feature.py` to handle the new intent in `handle_user_text()`
4. Add tests in `testing/test_command_parser.py`

### Example Usage

```python
from backend.nlp.command_parser import parse_command

# Parse a command
intent = parse_command("what time is it")
print(intent)  # Output: "get_time"

# Handles variations
intent = parse_command("tel me the time")  # typo
print(intent)  # Output: "get_time"

# Case insensitive
intent = parse_command("OPEN YOUTUBE")
print(intent)  # Output: "open_youtube"
```

## Requirements

The natural language parsing feature requires:
- `fuzzywuzzy==0.18.0`
- `python-Levenshtein==0.21.1` (for faster matching)

These are included in the `requirements.txt` file.
