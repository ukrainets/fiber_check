## ToDo 📋
- Add more ISPs
    - ✅ Ezee Fiber https://ezeefiber.com/
    - ✅ Ripple fiber - https://ripplefiber.com/availability-checker 
    - ✅ T-Mobile fiber - https://fiber.t-mobile.com/check-address
    - ✅ Astound - https://www.astound.com/chicago/internet/gig/
        (RCN, Grande, Wave, enTouch, and Digital West are now Astound)
    - ⚠️ AT&T fiber - https://www.att.com/internet/fiber/
- Test repo setup and check runs on separate hardware. 
- Refactor to run tests in parallel
- Add better handling for the cookie pop-up (T-Mobile)
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
- AT&T block automation activity `isp/test_att_fiber.py`. 
- `isp/test_ripple_fiber.py` and `isp/test_tmobile_fiber.py`
    Fails if run in headless mode.