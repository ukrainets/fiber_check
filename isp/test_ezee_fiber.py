"""
Docstring for isp.test_ezee_fiber
pytest -vs isp/test_ezee_fiber.py
"""

from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv

load_dotenv()  
SA = os.getenv("SERVICE_ADDRESS")

def test_ezeeFiber(page: Page):
    # page.set_default_timeout(10000)

    page.goto("https://ezeefiber.com/")
    
    expect(page.get_by_role("textbox", name="Enter your address")).to_be_visible()
    
    page.get_by_role("textbox", name="Enter your address").click()
    
    page.get_by_role("textbox", name="Enter your address").fill(SA)
    
    page.get_by_role("textbox", name="Enter your address").press("Enter")
    
    page.get_by_text("Not yet!").wait_for(state="visible")
    
    if page.get_by_text("Not yet!").is_visible():
        print("\n🙁\nEzee Fiber not evelable yet at location\n" + SA)
    else:
        print("\n😎\nEzee Fiber might be evelable at location\n" + SA)
