"""
Simple test to verify internet contectivity and corectness ow Playwright installation
pytest -vs tests/test_example.py
"""
from playwright.sync_api import Page, expect

WEBSITE = "https://stuffilike.site/"
BLOG = "https://stuffilike.site/blog"

def test_stuffilike(page: Page):
    page.goto(WEBSITE)

    # Expect a h1 "to contain" a Stuff I Like.
    expect(page.locator("h1", has_text="Stuff I Like")).to_be_visible()
    # Expects page to have a url
    expect(page).to_have_url(WEBSITE)

def test_stuffilike_blog(page: Page):
    page.goto(BLOG)

    # Expect a h1 "to contain" a Blog.
    expect(page.locator("h1", has_text="Blog")).to_be_visible()

    # Expects page to have a url
    expect(page).to_have_url(BLOG)