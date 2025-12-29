# fiber_check
A tool to check if the fiber internet is available at your address. 

## Setup
`python -m venv .venv`
`source .venv/bin/activate`
`pip install -r requirements.txt`
`playwright install`

## Run checks
`pytest` Will run test files in the "isp" directory.
`pytest tests/test_example.py` to check if PlayWright works ok.

---

## ToDo
- Add more ISPs
    - ✅ Ezee Fiber https://ezeefiber.com/
    - Ripple fiber - https://ripplefiber.com/availability-checker 
    - AT&T fiber - 
    - T-Mobile fiber - 
    - Astound - https://www.astound.com/chicago/internet/gig/
        (RCN, Grande, Wave, enTouch, and Digital West are now Astound)
- Add Slack notification. 
- Add scheduled test run
    - Satup on the home desktop
- Containerize it 
    - Set up on RPI or NAS Docker container