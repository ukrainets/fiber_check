# fiber_check ⚡️ 🛜 ✅
A tool to check if the fiber internet is available at your address. 

## Setup 🛠️
`python -m venv .venv` make virtual environment  
`source .venv/bin/activate` activate virtual environment  
`pip install -r requirements.txt` install dependancies  
`playwright install` complete PlayWright installation  

## Run checks 🏃‍♀️
`pytest` Will run test files in the "isp" directory.  
`pytest tests/test_example.py` to check if PlayWright works ok.  

## Slack webhook notification setup
1. Open https://api.slack.com/apps in the same window where you logged in to Slack.
2. Click "Create an App" button
3. Select "From scratch"
4. Add the app name, like "fiber_check" and pick the workspace.
5. Click "Create App" button.
6. Go to Features → Incoming Webhooks in the left-side menu.
7. Toggle Activate Incoming Webhooks → On.
8. Click "Add New Webhook"
9. Pick a channel where you want messages to be posted.
10. Copy the webhook link and add it to .env

---

## ToDo 📋
- Add more ISPs
    - ✅ Ezee Fiber https://ezeefiber.com/
    - ✅ Ripple fiber - https://ripplefiber.com/availability-checker 
    - AT&T fiber - https://www.att.com/internet/fiber/
    - T-Mobile fiber - 
    - Astound - https://www.astound.com/chicago/internet/gig/
        (RCN, Grande, Wave, enTouch, and Digital West are now Astound)
- Add handling of positive scenario
    - Check which message each page shows when there is service.
- ✅ Add Slack notification. 
    - Or https://ntfy.sh/ for push notification.
- Add error handling that takes a screenshot if an error occurs.
- Add scheduled test run
    - Satup on the home desktop
- Containerize it 
    - Set up on RPI or NAS Docker container

---
### Issues 
- isp/test_ripple_fiber.py
    Fails if run in headless mode.

