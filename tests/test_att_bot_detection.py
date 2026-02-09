"""
Quick diagnostic test
pytest -vs tests/test_att_bot_detection.py
"""

from playwright.sync_api import Page
import json

def test_detect_bot_protection(page: Page):
    """Diagnostic: Check for common bot detection indicators"""
    
    page.goto("https://www.att.com/internet/fiber/")
    
    # 1. Check navigator.webdriver property
    is_webdriver = page.evaluate("() => navigator.webdriver")
    print(f"navigator.webdriver exposed: {is_webdriver}")
    
    # 2. Check for automation-related properties
    checks = page.evaluate("""() => ({
        webdriver: navigator.webdriver,
        languages: navigator.languages,
        plugins_length: navigator.plugins.length,
        chrome_runtime: typeof window.chrome !== 'undefined',
        permissions: typeof navigator.permissions !== 'undefined'
    })""")
    print(f"Browser fingerprint: {json.dumps(checks, indent=2)}")
    
    # 3. Check response headers for bot protection services
    response = page.goto("https://www.att.com/internet/fiber/")
    headers = response.headers
    
    bot_indicators = ['cf-ray', 'x-datadome', 'x-px', 'akamai']
    for header in headers:
        if any(ind in header.lower() for ind in bot_indicators):
            print(f"Bot protection header found: {header}")