"""
Scheduler for running fiber internet availability checks.
python scheduler.py
"""

import subprocess
import schedule
import time
from utils.notify import notify_slack


def run_fiber_checks():
    """Execute pytest and notify results"""
    notify_slack("🔄 Running fiber internet availability checks...")
    
    result = subprocess.run(
        ["pytest"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        notify_slack("🤘 Fiber checks completed.")
    else:
        notify_slack(f"⚠️ Fiber checks finished with errors (exit code: {result.returncode})")


def main():
    notify_slack("🚀 Fiber internet check scheduler started.")
    
    # Run daily at 7:00 AM
    schedule.every().day.at("07:00").do(run_fiber_checks)
                        # use format hh:mm
    
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()