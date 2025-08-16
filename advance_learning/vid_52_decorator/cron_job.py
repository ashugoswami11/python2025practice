import time
from datetime import datetime

from pywin.Demos.app.customprint import PRINTDLGORD


def decorator(func):
    '''log the date and time of the function'''

    def wrapper_func():
        run_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        print("=======LOG ENTRY========")
        print(f"function name: {func.__name__}")
        print(f"function ran on: {run_time}")
        print("status :   STARTED")
        print("-------------------------")

        func()

        print("status :   FINISHED")
        print("=======END LOG========")
        print("\n\n")

    return wrapper_func


@decorator
def daily_cron():
    time.sleep(3)
    print("daily cron_job ran")

@decorator
def week_cron():
    time.sleep(5)
    print("weekly cron_job ran")

@decorator
def month_cron():
    time.sleep(8)
    print("monthly cron_job ran")

daily_cron()
week_cron()
month_cron()
daily_cron()
