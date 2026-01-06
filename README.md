# fiber_check ⚡️🛜 ✅
A tool to check if the fiber internet is available at your address.  
It primarily checks the ISPs that are available in the Greater Chicago area.  

**Supported ISPs**:  
- [T-Mobile fiber](https://fiber.t-mobile.com/check-address)
- [Ezee Fiber](https://ezeefiber.com/)
- [Ripple fiber](https://ripplefiber.com/availability-checker)
- [Astound](https://www.astound.com/chicago/internet/gig/)
- WIP:[AT&T](https://www.att.com/internet/fiber/)

---

## Setup 🛠️
1. `python -m venv .venv` - make virtual environment  
2. `source .venv/bin/activate` - activate virtual environment  
3. `pip install -r requirements.txt` - install dependancies  
4. `playwright install` - complete PlayWright installation
5. Create `.env` file and populate it with your address. See `.env.example`

## Run checks 🏃‍♀️
`pytest tests/test_example.py` To check if PlayWright works correctly.  
`pytest` Will run test files in the "isp" directory.  
`python scheduler.py` To start scheduler. 


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

# Roadmap 🗺️
Project ToDo list and issue - [todo_and_issues.md](todo_and_issues.md)


