"""
Module for Slack notifications via webhook.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")


def send_slack_message(message: str) -> bool:
    """
    Send a message to Slack via webhook.
    Args:
        message: Text message to send        
    Returns:
        True if successful, False otherwise
    """
    if not SLACK_WEBHOOK:
        print("⚠️: SLACK_WEBHOOK not configured, skipping notification")
        return False
    
    try:
        response = requests.post(
            SLACK_WEBHOOK,
            json={"text": message},
            timeout=10
        )
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Failed to send Slack notification: {e}")
        return False


def notify_slack(message: str) -> None:
    """
    Print message to console AND send to Slack.
    """
    print(message)
    send_slack_message(message)