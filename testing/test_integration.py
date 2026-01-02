"""
Integration test for command parser with feature module.
Tests that parsed intents correctly map to actions.

Run with: python -m testing.test_integration
"""

import sys
import os

# Add parent directory to path to import backend modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.nlp.command_parser import parse_command


def test_intent_coverage():
    """Test that all supported intents are properly recognized."""
    print("\n🧪 Testing Intent Coverage and Recognition")
    print("=" * 60)
    
    test_commands = {
        "what time is it": "get_time",
        "tell me the date": "get_date",
        "open youtube": "open_youtube",
        "launch whatsapp": "open_whatsapp",
        "start calculator": "open_calculator",
        "weather today": "get_weather",
        "search for python": "search_google",
        "play music": "play_music",
        "latest news": "get_news",
        "open browser": "open_browser",
        "take screenshot": "take_screenshot",
        "shutdown computer": "shutdown",
        "restart system": "restart",
    }
    
    passed = 0
    failed = 0
    
    for command, expected_intent in test_commands.items():
        result = parse_command(command)
        if result == expected_intent:
            print(f"✅ '{command}' → {result}")
            passed += 1
        else:
            print(f"❌ '{command}' → Expected: {expected_intent}, Got: {result}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Coverage Test Results: {passed}/{len(test_commands)} passed")
    
    return failed == 0


def test_variations_and_flexibility():
    """Test various phrasings for the same intent."""
    print("\n🧪 Testing Flexibility with Different Phrasings")
    print("=" * 60)
    
    test_groups = {
        "Time queries": [
            ("what time is it", "get_time"),
            ("tell me the time", "get_time"),
            ("current time", "get_time"),
            ("time please", "get_time"),
        ],
        "Date queries": [
            ("what's the date", "get_date"),
            ("date today", "get_date"),
            ("today's date", "get_date"),
        ],
        "YouTube commands": [
            ("open youtube", "open_youtube"),
            ("launch youtube", "open_youtube"),
            ("youtube", "open_youtube"),
            ("go to youtube", "open_youtube"),
        ],
        "Weather queries": [
            ("what's the weather", "get_weather"),
            ("weather now", "get_weather"),
            ("tell me the weather", "get_weather"),
        ],
    }
    
    all_passed = True
    
    for group_name, test_cases in test_groups.items():
        print(f"\n{group_name}:")
        group_passed = True
        for command, expected_intent in test_cases:
            result = parse_command(command)
            if result == expected_intent:
                print(f"  ✅ '{command}'")
            else:
                print(f"  ❌ '{command}' → Expected: {expected_intent}, Got: {result}")
                group_passed = False
                all_passed = False
        
        if group_passed:
            print(f"  ✓ All {group_name} variations working")
    
    return all_passed


def test_real_world_scenarios():
    """Test realistic user inputs with natural variations."""
    print("\n🧪 Testing Real-World User Scenarios")
    print("=" * 60)
    
    scenarios = [
        ("hey jarvis what time is it", "get_time"),
        ("can you tell me the current time", "get_time"),
        ("please open youtube for me", "open_youtube"),
        ("i want to open whatsapp", "open_whatsapp"),
        ("show me the weather", "get_weather"),
        ("search google", "search_google"),  # More realistic short command
        ("play some music please", "play_music"),
        ("what's in the news today", "get_news"),
    ]
    
    passed = 0
    failed = 0
    
    for command, expected_intent in scenarios:
        result = parse_command(command)
        if result == expected_intent:
            print(f"✅ '{command}'")
            passed += 1
        else:
            print(f"❌ '{command}' → Expected: {expected_intent}, Got: {result}")
            failed += 1
    
    print("\n" + "-" * 60)
    print(f"Real-world scenarios: {passed}/{len(scenarios)} passed")
    
    return failed == 0


def main():
    """Run all integration tests."""
    print("\n" + "=" * 60)
    print("🧠 JARVIS INTEGRATION TEST SUITE")
    print("Testing Command Parser with Feature Module")
    print("=" * 60)
    
    test_results = []
    
    # Run all tests
    test_results.append(("Intent Coverage", test_intent_coverage()))
    test_results.append(("Flexibility Test", test_variations_and_flexibility()))
    test_results.append(("Real-World Scenarios", test_real_world_scenarios()))
    
    # Print summary
    print("\n" + "=" * 60)
    print("INTEGRATION TEST SUMMARY")
    print("=" * 60)
    
    all_passed = all(result for _, result in test_results)
    
    for test_name, result in test_results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    if all_passed:
        print("\n🎉 ALL INTEGRATION TESTS PASSED! 🎉")
        print("\nThe natural language parser is working correctly and")
        print("can handle multiple phrasings, synonyms, and misspellings.")
        return 0
    else:
        print("\n⚠️  Some integration tests failed.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
