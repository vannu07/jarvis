# in root dir, run -> python -m testing.text_test

from backend.nlp.command_parser import parse_command

if __name__ == "__main__":
    print("🧠 Jarvis Text Parser Test Mode")
    print("Type your command (or 'exit' to quit)")
    print("-" * 40)

    while True:
        cmd = input("You: ")
        if cmd.lower() in ["exit", "quit"]:
            print("Exiting test mode.")
            break

        intent = parse_command(cmd)
        if intent:
            print(f"✅ Recognized intent: {intent}")
        else:
            print("❌ Could not recognize intent.")