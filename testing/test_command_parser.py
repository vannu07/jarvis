"""
Comprehensive test suite for the command parser.
Tests synonyms, fuzzy matching, and edge cases.

Run with: python -m testing.test_command_parser
"""

import sys
import os

# Add parent directory to path to import backend modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.nlp.command_parser import parse_command, get_all_intents, get_phrases_for_intent


class TestCommandParser:
    def __init__(self):
        self.tests_run = 0
        self.tests_passed = 0
        self.tests_failed = 0
        self.failed_tests = []

    def assert_equal(self, actual, expected, test_name):
        """Assert that actual equals expected."""
        self.tests_run += 1
        if actual == expected:
            self.tests_passed += 1
            print(f"✅ {test_name}")
            return True
        else:
            self.tests_failed += 1
            self.failed_tests.append(test_name)
            print(f"❌ {test_name}")
            print(f"   Expected: {expected}, Got: {actual}")
            return False

    def test_exact_matches(self):
        """Test exact phrase matching."""
        print("\n🧪 Testing Exact Matches")
        print("-" * 50)
        
        test_cases = [
            ("what time is it", "get_time"),
            ("open youtube", "open_youtube"),
            ("open whatsapp", "open_whatsapp"),
            ("open calculator", "open_calculator"),
            ("what's the weather", "get_weather"),
            ("what's the date", "get_date"),
            ("search google", "search_google"),
            ("play music", "play_music"),
            ("tell me the news", "get_news"),
            ("open browser", "open_browser"),
        ]
        
        for user_input, expected_intent in test_cases:
            result = parse_command(user_input)
            self.assert_equal(result, expected_intent, f"Exact match: '{user_input}'")

    def test_synonym_variations(self):
        """Test that synonyms map to the same intent."""
        print("\n🧪 Testing Synonym Variations")
        print("-" * 50)
        
        test_cases = [
            # Time variations
            ("tell me the time", "get_time"),
            ("time now", "get_time"),
            ("current time", "get_time"),
            ("show me the time", "get_time"),
            
            # Date variations
            ("date today", "get_date"),
            ("today's date", "get_date"),
            ("current date", "get_date"),
            
            # YouTube variations
            ("launch youtube", "open_youtube"),
            ("start youtube", "open_youtube"),
            ("go to youtube", "open_youtube"),
            
            # Weather variations
            ("weather now", "get_weather"),
            ("weather today", "get_weather"),
            ("tell me the weather", "get_weather"),
            
            # Calculator variations
            ("launch calculator", "open_calculator"),
            ("calc", "open_calculator"),
            ("open calc", "open_calculator"),
        ]
        
        for user_input, expected_intent in test_cases:
            result = parse_command(user_input)
            self.assert_equal(result, expected_intent, f"Synonym: '{user_input}'")

    def test_fuzzy_matching_misspellings(self):
        """Test fuzzy matching with common misspellings."""
        print("\n🧪 Testing Fuzzy Matching (Misspellings)")
        print("-" * 50)
        
        test_cases = [
            ("wat time is it", "get_time"),
            ("tel me the time", "get_time"),
            ("opne youtube", "open_youtube"),
            ("launche youtube", "open_youtube"),
            ("whatsaap", "open_whatsapp"),
            ("calculater", "open_calculator"),
            ("weatherr", "get_weather"),
            ("currrent weather", "get_weather"),
            ("plaay music", "play_music"),
            ("newws", "get_news"),
        ]
        
        for user_input, expected_intent in test_cases:
            result = parse_command(user_input)
            self.assert_equal(result, expected_intent, f"Misspelling: '{user_input}'")

    def test_case_insensitivity(self):
        """Test that matching is case insensitive."""
        print("\n🧪 Testing Case Insensitivity")
        print("-" * 50)
        
        test_cases = [
            ("WHAT TIME IS IT", "get_time"),
            ("Open YouTube", "open_youtube"),
            ("OPEN CALCULATOR", "open_calculator"),
            ("What's The WEATHER", "get_weather"),
            ("PLAY MUSIC", "play_music"),
        ]
        
        for user_input, expected_intent in test_cases:
            result = parse_command(user_input)
            self.assert_equal(result, expected_intent, f"Case insensitive: '{user_input}'")

    def test_extra_whitespace(self):
        """Test handling of extra whitespace."""
        print("\n🧪 Testing Extra Whitespace Handling")
        print("-" * 50)
        
        test_cases = [
            ("  what time is it  ", "get_time"),
            ("open   youtube", "open_youtube"),
            ("  tell  me  the  weather  ", "get_weather"),
            ("    play music    ", "play_music"),
        ]
        
        for user_input, expected_intent in test_cases:
            result = parse_command(user_input)
            self.assert_equal(result, expected_intent, f"Whitespace: '{user_input}'")

    def test_partial_matches(self):
        """Test partial phrase matching."""
        print("\n🧪 Testing Partial Matches")
        print("-" * 50)
        
        test_cases = [
            ("time", "get_time"),
            ("youtube", "open_youtube"),
            ("whatsapp", "open_whatsapp"),
            ("calculator", "open_calculator"),
            ("weather", "get_weather"),
            ("news", "get_news"),
            ("music", "play_music"),
        ]
        
        for user_input, expected_intent in test_cases:
            result = parse_command(user_input)
            self.assert_equal(result, expected_intent, f"Partial: '{user_input}'")

    def test_edge_cases(self):
        """Test edge cases."""
        print("\n🧪 Testing Edge Cases")
        print("-" * 50)
        
        # Empty input
        result = parse_command("")
        self.assert_equal(result, None, "Empty string input")
        
        # None input
        result = parse_command(None)
        self.assert_equal(result, None, "None input")
        
        # Very short input that doesn't match
        result = parse_command("x")
        self.assert_equal(result, None, "Single character that doesn't match")
        
        # Random gibberish
        result = parse_command("asdfghjkl")
        self.assert_equal(result, None, "Random gibberish")

    def test_multiple_word_variations(self):
        """Test variations with different word orders and structures."""
        print("\n🧪 Testing Multiple Word Variations")
        print("-" * 50)
        
        test_cases = [
            ("can you tell me the time", "get_time"),
            ("show me the time please", "get_time"),
            ("please open youtube", "open_youtube"),
            ("i want to open whatsapp", "open_whatsapp"),
            ("how's the weather today", "get_weather"),
            ("give me today's date", "get_date"),
        ]
        
        for user_input, expected_intent in test_cases:
            result = parse_command(user_input)
            self.assert_equal(result, expected_intent, f"Multi-word: '{user_input}'")

    def test_utility_functions(self):
        """Test utility functions."""
        print("\n🧪 Testing Utility Functions")
        print("-" * 50)
        
        # Test get_all_intents
        intents = get_all_intents()
        self.assert_equal(len(intents) >= 10, True, "At least 10 intents available")
        self.assert_equal("get_time" in intents, True, "get_time intent exists")
        self.assert_equal("open_youtube" in intents, True, "open_youtube intent exists")
        
        # Test get_phrases_for_intent
        time_phrases = get_phrases_for_intent("get_time")
        self.assert_equal(len(time_phrases) > 0, True, "get_time has phrases")
        self.assert_equal("what time is it" in time_phrases, True, "get_time includes 'what time is it'")
        
        # Test non-existent intent
        empty_phrases = get_phrases_for_intent("non_existent_intent")
        self.assert_equal(empty_phrases, [], "Non-existent intent returns empty list")

    def test_ten_common_commands(self):
        """Test the 10 most common commands as specified in the requirements."""
        print("\n🧪 Testing 10 Common Commands (Requirements)")
        print("-" * 50)
        
        test_cases = [
            ("what time is it", "get_time", "1. Time query"),
            ("what's the date", "get_date", "2. Date query"),
            ("open youtube", "open_youtube", "3. Open YouTube"),
            ("open whatsapp", "open_whatsapp", "4. Open WhatsApp"),
            ("open calculator", "open_calculator", "5. Open Calculator"),
            ("what's the weather", "get_weather", "6. Weather query"),
            ("search google", "search_google", "7. Google search"),
            ("play music", "play_music", "8. Play music"),
            ("tell me the news", "get_news", "9. Get news"),
            ("open browser", "open_browser", "10. Open browser"),
        ]
        
        for user_input, expected_intent, description in test_cases:
            result = parse_command(user_input)
            self.assert_equal(result, expected_intent, description)

    def run_all_tests(self):
        """Run all test suites."""
        print("\n" + "=" * 60)
        print("🧠 JARVIS COMMAND PARSER - COMPREHENSIVE TEST SUITE")
        print("=" * 60)
        
        self.test_exact_matches()
        self.test_synonym_variations()
        self.test_fuzzy_matching_misspellings()
        self.test_case_insensitivity()
        self.test_extra_whitespace()
        self.test_partial_matches()
        self.test_multiple_word_variations()
        self.test_utility_functions()
        self.test_edge_cases()
        self.test_ten_common_commands()
        
        # Print summary
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests Run: {self.tests_run}")
        print(f"✅ Passed: {self.tests_passed}")
        print(f"❌ Failed: {self.tests_failed}")
        
        if self.tests_failed > 0:
            print("\nFailed Tests:")
            for test_name in self.failed_tests:
                print(f"  - {test_name}")
        
        success_rate = (self.tests_passed / self.tests_run * 100) if self.tests_run > 0 else 0
        print(f"\nSuccess Rate: {success_rate:.1f}%")
        
        if self.tests_failed == 0:
            print("\n🎉 ALL TESTS PASSED! 🎉")
            return 0
        else:
            print(f"\n⚠️  {self.tests_failed} test(s) failed.")
            return 1


if __name__ == "__main__":
    tester = TestCommandParser()
    exit_code = tester.run_all_tests()
    sys.exit(exit_code)
