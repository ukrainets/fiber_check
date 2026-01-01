"""
Check if T-Mobile Fiber ISP has services at a specific address
pytest -vs isp/test_tmobile_fiber.py
"""

from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
from utils.notify import notify_slack

load_dotenv()  
SERVICEA_ADDRESS = os.getenv("SERVICE_ADDRESS")
ISP_URL = "https://fiber.t-mobile.com/check-address"
TEXT_TO_CHECK = "T-Mobile Fiber isn't currently available at your location but you are eligible for T-Mobile 5G Home Internet."

def test_rippleFiber(page: Page):
    # page.set_default_timeout(10000)
    page.set_viewport_size({"width": 1280, "height": 1000})
    
    page.goto(ISP_URL)
    
    expect(page.locator("h1", has_text="Check availability")).to_be_visible()
    
    expect(page.get_by_test_id("fpe-fiber-input")).to_be_visible()

    if page.get_by_role("button", name="Accept").is_visible():
        page.get_by_role("button", name="Accept").click()
    
    page.get_by_test_id("fpe-fiber-input").click()
    
    page.get_by_test_id("fpe-fiber-input").fill(SERVICEA_ADDRESS)
    
    page.get_by_test_id("fpe-fiber-input").press("Enter")
    page.get_by_test_id("fpe-fiber-input").press("Enter")
    
    if page.get_by_role("button", name="Accept").is_visible():
        page.get_by_role("button", name="Accept").click()
    
    if page.get_by_role("button", name="Next").is_visible:
        page.get_by_role("button", name="Next").is_enabled()
        page.get_by_role("button", name="Next").click()
    
    page.get_by_text(TEXT_TO_CHECK).wait_for(state="visible")
    
    # page.wait_for_timeout(3000)
    
    if page.get_by_text(TEXT_TO_CHECK).is_visible():
        notify_slack(f"🙁 T-Mobile Fiber not available yet at: {SERVICEA_ADDRESS}")
    else:
        notify_slack(f"😎 T-Mobile Fiber might be available at: {SERVICEA_ADDRESS}")