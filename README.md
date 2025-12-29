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

---

## ToDo 📋
- Add more ISPs
    - ✅ Ezee Fiber https://ezeefiber.com/
    - ✅ Ripple fiber - https://ripplefiber.com/availability-checker 
    - AT&T fiber - 
    - T-Mobile fiber - 
    - Astound - https://www.astound.com/chicago/internet/gig/
        (RCN, Grande, Wave, enTouch, and Digital West are now Astound)
- Add handling of positive scenario
    - Check which message each page shows when there is service.
- Add Slack notification. 
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