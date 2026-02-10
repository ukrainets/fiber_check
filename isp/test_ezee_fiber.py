"""
Check if Ezee Fiber ISP has services at a specific address
pytest -vs isp/test_ezee_fiber.py
"""

from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
from utils.notify import notify_slack

load_dotenv()  
SERVICEA_ADDRESS = os.getenv("SERVICE_ADDRESS")

def test_ezeeFiber(page: Page):
    # page.set_default_timeout(10000)

    page.goto("https://ezeefiber.com/")
    
    expect(page.get_by_role("textbox", name="Enter your address").first).to_be_visible()
    
    page.get_by_role("textbox", name="Enter your address").first.click()
    
    page.get_by_role("textbox", name="Enter your address").first.fill(SERVICEA_ADDRESS)
    
    page.get_by_role("textbox", name="Enter your address").first.press("Enter")
    
    page.get_by_text("Not yet!").wait_for(state="visible")

    if page.get_by_text("Not yet!").is_visible():
        notify_slack(f"🙁 Ezee Fiber not available yet at: {SERVICEA_ADDRESS}")
    else:
        notify_slack(f"😎 Ezee Fiber might be available at: {SERVICEA_ADDRESS}")