"""
Feedback Module for Jarvis AI Assistant
Provides colored console output and status indicators for better user experience
"""

import time
from colorama import Fore, Style, init
import re

# Initialize colorama for cross-platform colored output
init(autoreset=True)


def sanitize_log_message(message):
    """
    Best-effort sanitization of log messages to avoid printing sensitive data
    such as phone numbers in clear text.

    This masks long digit sequences (optionally starting with '+') that look
    like phone numbers, keeping only the last 2 digits visible.
    """
    text = str(message)

    # Mask phone-like patterns: optional '+' followed by 8 or more digits.
    def _mask_phone(match):
        value = match.group(0)
        # Keep last 2 characters, replace the rest with '*'
        if len(value) <= 2:
            return "*" * len(value)
        return "*" * (len(value) - 2) + value[-2:]

    phone_pattern = re.compile(r"\+?\d{8,}")
    text = phone_pattern.sub(_mask_phone, text)
    return text


class StatusIndicator:
    """Class to manage status indicators with colored output"""
    
    # Status colors
    LISTENING_COLOR = Fore.CYAN
    PROCESSING_COLOR = Fore.YELLOW
    SUCCESS_COLOR = Fore.GREEN
    ERROR_COLOR = Fore.RED
    INFO_COLOR = Fore.BLUE
    WARNING_COLOR = Fore.MAGENTA
    
    @staticmethod
    def listening(message="Listening..."):
        """Display listening status"""
        safe_message = sanitize_log_message(message)
        print(f"{StatusIndicator.LISTENING_COLOR}🎤 {safe_message}{Style.RESET_ALL}")
    
    @staticmethod
    def processing(message="Processing..."):
        """Display processing status"""
        safe_message = sanitize_log_message(message)
        print(f"{StatusIndicator.PROCESSING_COLOR}⚙️ {safe_message}{Style.RESET_ALL}")
    
    @staticmethod
    def done(message="Done.", duration=None):
        """Display completion status with optional duration"""
        if duration is not None:
            message = f"{message} (Completed in {duration:.2f}s)"
        safe_message = sanitize_log_message(message)
        print(f"{StatusIndicator.SUCCESS_COLOR}✓ {safe_message}{Style.RESET_ALL}")
    
    @staticmethod
    def success(message):
        """Display success message"""
        safe_message = sanitize_log_message(message)
        print(f"{StatusIndicator.SUCCESS_COLOR}✓ {safe_message}{Style.RESET_ALL}")
    
    @staticmethod
    def error(message):
        """Display error message"""
        safe_message = sanitize_log_message(message)
        print(f"{StatusIndicator.ERROR_COLOR}✗ {safe_message}{Style.RESET_ALL}")
    
    @staticmethod
    def info(message):
        """Display informational message"""
        safe_message = sanitize_log_message(message)
        print(f"{StatusIndicator.INFO_COLOR}ℹ {safe_message}{Style.RESET_ALL}")
    
    @staticmethod
    def warning(message):
        """Display warning message"""
        safe_message = sanitize_log_message(message)
        print(f"{StatusIndicator.WARNING_COLOR}⚠ {safe_message}{Style.RESET_ALL}")
    
    @staticmethod
    def command(message):
        """Display received command"""
        safe_message = sanitize_log_message(message)
        print(f"{Fore.WHITE}» {safe_message}{Style.RESET_ALL}")
    
    @staticmethod
    def response(message):
        """Display assistant response"""
        safe_message = sanitize_log_message(message)
        print(f"{Fore.LIGHTGREEN_EX}« {safe_message}{Style.RESET_ALL}")


class Timer:
    """Context manager for timing operations"""
    
    def __init__(self, operation_name=None):
        """
        Initialize timer
        
        Args:
            operation_name (str): Optional name of the operation being timed
        """
        self.operation_name = operation_name
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        """Start the timer"""
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop the timer and display duration"""
        self.end_time = time.time()
        if exc_type is None:
            # No exception occurred
            duration = self.elapsed()
            if self.operation_name:
                StatusIndicator.done(self.operation_name, duration)
        else:
            # Exception occurred
            if self.operation_name:
                StatusIndicator.error(f"{self.operation_name} failed")
        return False  # Don't suppress exceptions
    
    def elapsed(self):
        """
        Get elapsed time
        
        Returns:
            float: Elapsed time in seconds
        """
        if self.start_time is None:
            return 0.0
        end = self.end_time if self.end_time is not None else time.time()
        return end - self.start_time


def print_colored(message, color=Fore.WHITE, prefix=""):
    """
    Print a colored message with optional prefix
    
    Args:
        message (str): Message to print
        color (str): Color from colorama.Fore
        prefix (str): Optional prefix for the message
    """
    full_message = f"{prefix}{message}" if prefix else message
    print(f"{color}{full_message}{Style.RESET_ALL}")


def print_status(status_type, message):
    """
    Print a status message based on type
    
    Args:
        status_type (str): Type of status ('listening', 'processing', 'done', 'error', 'info', 'warning')
        message (str): Message to display
    """
    status_map = {
        'listening': StatusIndicator.listening,
        'processing': StatusIndicator.processing,
        'done': StatusIndicator.done,
        'success': StatusIndicator.success,
        'error': StatusIndicator.error,
        'info': StatusIndicator.info,
        'warning': StatusIndicator.warning,
        'command': StatusIndicator.command,
        'response': StatusIndicator.response,
    }
    
    handler = status_map.get(status_type.lower())
    if handler:
        handler(message)
    else:
        print(message)
