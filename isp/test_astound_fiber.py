"""
Check if Astound ISP has services at a specific address
pytest -vs isp/test_astound_fiber.py
"""

from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
from utils.notify import notify_slack
# import pytest

load_dotenv()  
SERVICEA_ADDRESS = os.getenv("SERVICE_ADDRESS")
ISP_URL = "https://www.astound.com/chicago/internet/gig/"

# @pytest.mark.skip(reason="Temporarily disabled - WIP")
def test_astoundFiber(page: Page):
    # page.set_default_timeout(10000)
    
    page.set_viewport_size({"width": 1280, "height": 1200})
    
    page.goto(ISP_URL)
    
    # expect(page.get_by_text("button", name="Check for service at your address")).to_be_visible()
    expect(page.get_by_text("Check for service at your address")).to_be_visible
    
    page.get_by_text("Check for service at your address").click()
    
    page.get_by_role("textbox", name="Street Address").click()
    
    expect(page.get_by_text("To get started, enter your")).to_be_visible()
    
    page.get_by_role("textbox", name="Street Address").click()
    
    page.get_by_role("textbox", name="Street Address").fill(SERVICEA_ADDRESS)
    page.wait_for_timeout(500) # ToDo: find a way to awoid it
    
    page.keyboard.press("ArrowDown")
    page.wait_for_timeout(500) # ToDo: find a way to awoid it
    
    page.keyboard.press("Enter")
    
    page.get_by_role("button", name="Check for Service", exact=True).click()
    
    page.get_by_text("Check Another Address").wait_for(state="visible")
    
    # page.wait_for_timeout(3000)
    
    if page.get_by_text("Outside the Astound Service").is_visible():
        notify_slack(f"🙁 Astound Fiber not available yet at: {SERVICEA_ADDRESS}")
    else:
        notify_slack(f"😎 Astound Fiber might be available at: {SERVICEA_ADDRESS}")