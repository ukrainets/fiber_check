"""
Check if Ripple Fiber ISP has services at a specific address
pytest -vs isp/test_ripple_fiber.py
"""

from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
from utils.notify import notify_slack

load_dotenv()  
SERVICEA_ADDRESS = os.getenv("SERVICE_ADDRESS")

def test_rippleFiber(page: Page):
    # page.set_default_timeout(10000)

    page.goto("https://ripplefiber.com/availability-checker")
    
    expect(page.locator("h1", has_text="Is Ripple Fiber available for my home?")).to_be_visible()
    
    page.get_by_role("textbox", name="Enter your street address").click()
    
    page.get_by_role("textbox", name="Enter your street address").fill(SERVICEA_ADDRESS)
    
    page.keyboard.press("ArrowDown")
    
    page.keyboard.press("Enter")
    
    page.get_by_role("button", name="CHECK AVAILABILITY").click()
    # Issue: fails on this step if run in headless
    
    page.get_by_text("Sorry,").wait_for(state="visible")
    
    # page.wait_for_timeout(3000)
    
    if page.get_by_text("Sorry,").is_visible():
        notify_slack(f"🙁 Ripple Fiber not available yet at: {SERVICEA_ADDRESS}")
    else:
        notify_slack(f"😎 Ripple Fiber might be available at: {SERVICEA_ADDRESS}")