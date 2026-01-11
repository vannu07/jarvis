"""
Unit tests for the feedback module
Tests colored output, status indicators, and timing functionality
"""

import unittest
import time
import sys
from io import StringIO
from backend.feedback import StatusIndicator, Timer, print_colored, print_status


class TestStatusIndicator(unittest.TestCase):
    """Test StatusIndicator class methods"""
    
    def setUp(self):
        """Capture stdout for testing"""
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output
    
    def tearDown(self):
        """Restore stdout"""
        sys.stdout = self.original_stdout
    
    def test_listening(self):
        """Test listening status indicator"""
        StatusIndicator.listening("Test listening")
        output = self.held_output.getvalue()
        self.assertIn("Test listening", output)
        self.assertIn("🎤", output)
    
    def test_processing(self):
        """Test processing status indicator"""
        StatusIndicator.processing("Test processing")
        output = self.held_output.getvalue()
        self.assertIn("Test processing", output)
        self.assertIn("⚙️", output)
    
    def test_done(self):
        """Test done status indicator without duration"""
        StatusIndicator.done("Test done")
        output = self.held_output.getvalue()
        self.assertIn("Test done", output)
        self.assertIn("✓", output)
    
    def test_done_with_duration(self):
        """Test done status indicator with duration"""
        StatusIndicator.done("Test done", 1.23)
        output = self.held_output.getvalue()
        self.assertIn("Test done", output)
        self.assertIn("1.23s", output)
        self.assertIn("✓", output)
    
    def test_success(self):
        """Test success status indicator"""
        StatusIndicator.success("Test success")
        output = self.held_output.getvalue()
        self.assertIn("Test success", output)
        self.assertIn("✓", output)
    
    def test_error(self):
        """Test error status indicator"""
        StatusIndicator.error("Test error")
        output = self.held_output.getvalue()
        self.assertIn("Test error", output)
        self.assertIn("✗", output)
    
    def test_info(self):
        """Test info status indicator"""
        StatusIndicator.info("Test info")
        output = self.held_output.getvalue()
        self.assertIn("Test info", output)
        self.assertIn("ℹ", output)
    
    def test_warning(self):
        """Test warning status indicator"""
        StatusIndicator.warning("Test warning")
        output = self.held_output.getvalue()
        self.assertIn("Test warning", output)
        self.assertIn("⚠", output)
    
    def test_command(self):
        """Test command status indicator"""
        StatusIndicator.command("Test command")
        output = self.held_output.getvalue()
        self.assertIn("Test command", output)
        self.assertIn("»", output)
    
    def test_response(self):
        """Test response status indicator"""
        StatusIndicator.response("Test response")
        output = self.held_output.getvalue()
        self.assertIn("Test response", output)
        self.assertIn("«", output)


class TestTimer(unittest.TestCase):
    """Test Timer class"""
    
    def test_timer_basic(self):
        """Test basic timer functionality"""
        with Timer() as timer:
            time.sleep(0.1)
        elapsed = timer.elapsed()
        self.assertGreaterEqual(elapsed, 0.1)
        self.assertLess(elapsed, 0.2)
    
    def test_timer_with_name(self):
        """Test timer with operation name"""
        # Redirect stdout to capture timer output
        held_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = held_output
        
        with Timer("Test operation"):
            time.sleep(0.1)
        
        output = held_output.getvalue()
        sys.stdout = original_stdout
        
        self.assertIn("Test operation", output)
        self.assertIn("Completed in", output)
    
    def test_timer_elapsed(self):
        """Test elapsed time calculation"""
        timer = Timer()
        with timer:
            time.sleep(0.1)
        elapsed = timer.elapsed()
        self.assertGreater(elapsed, 0.0)
        self.assertGreaterEqual(elapsed, 0.1)


class TestHelperFunctions(unittest.TestCase):
    """Test helper functions"""
    
    def setUp(self):
        """Capture stdout for testing"""
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output
    
    def tearDown(self):
        """Restore stdout"""
        sys.stdout = self.original_stdout
    
    def test_print_status_listening(self):
        """Test print_status with listening type"""
        print_status('listening', 'Test message')
        output = self.held_output.getvalue()
        self.assertIn("Test message", output)
    
    def test_print_status_processing(self):
        """Test print_status with processing type"""
        print_status('processing', 'Test message')
        output = self.held_output.getvalue()
        self.assertIn("Test message", output)
    
    def test_print_status_done(self):
        """Test print_status with done type"""
        print_status('done', 'Test message')
        output = self.held_output.getvalue()
        self.assertIn("Test message", output)
    
    def test_print_status_invalid(self):
        """Test print_status with invalid type"""
        print_status('invalid', 'Test message')
        output = self.held_output.getvalue()
        self.assertIn("Test message", output)


if __name__ == '__main__':
    unittest.main()
