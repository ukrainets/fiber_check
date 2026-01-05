"""
Check if AT&T Fiber ISP has services at a specific address
pytest -vs isp/test_att_fiber.py
"""

from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
from utils.notify import notify_slack
import pytest

load_dotenv()  
SERVICEA_ADDRESS = os.getenv("SERVICE_ADDRESS")
ISP_URL = "https://www.att.com/internet/fiber/"

@pytest.mark.skip(reason="Temporarily disabled - WIP")
def test_ezeeFiber(page: Page):
    page.set_default_timeout(10000)
    
    page.set_viewport_size({"width": 1280, "height": 1200})
    
    page.goto(ISP_URL)
    # page.wait_for_timeout(60000)
    expect(page.get_by_label("addressInput")).to_be_visible()
    
    # page.mouse.wheel(0, 300)
    # page.wait_for_timeout(500)
    # page.mouse.wheel(0, 300)
    # page.wait_for_timeout(500)
    # page.mouse.wheel(0, -600)
    # page.wait_for_timeout(500)
    
    # expect(page.get_by_role("button", name="Opt out")).to_be_visible()
    # page.get_by_role("button", name="Opt out").click()
    
    page.wait_for_timeout(500)
    
    page.get_by_label("addressInput").click()
    
    page.get_by_label("addressInput").fill(SERVICEA_ADDRESS)
    
    expect(page.get_by_test_id("checkAvailabilityId")).to_be_visible()
    
    page.get_by_test_id("checkAvailabilityId").click()
# Issue: When running with Playwright, checking availability loads a different page than when doing the same steps manually.
# Most likely bot blocker 
    
    page.get_by_text("Add your plan").wait_for(state="visible")

    if page.get_by_text("Get a $100 reward card and stay updated on AT&T Fiber®").is_visible():
        notify_slack(f"🙁 AT&T Fiber not available yet at: {SERVICEA_ADDRESS}")
    else:
        notify_slack(f"😎 AT&T Fiber might be available at: {SERVICEA_ADDRESS}")