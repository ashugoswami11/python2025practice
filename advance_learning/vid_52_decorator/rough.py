"""
🧠 Practice Question (Beginner-Friendly)
Title: Reminder Manager with Auto Cleanup

Scenario:
You are building a small "Reminder Manager" app in Python.
This app does three things:

Reminds you about tasks at fixed intervals (like a cron job)

Uses a decorator to track how many times a reminder has been shown

Automatically deletes old/finished reminders from the list using del

🎯 Tasks:
1. Create a list of reminders
Example:

python
Copy
Edit
reminders = [
    {"task": "Drink Water", "times": 0},
    {"task": "Eye Exercise", "times": 0},
    {"task": "Stretch Body", "times": 0},
]
2. Create a decorator
Make a decorator named track_calls which increases the times count for each reminder every time it is shown.

3. Set up a loop (like a cron job)
Every 10 seconds, pick and show a reminder from the list.

4. Use del
If a reminder has already been shown 3 times, remove it using del.

5. Exit the program once all reminders are done.
📝 Hints:
Use time.sleep(10) to mimic cron job behavior.

Use random.choice() to pick a reminder randomly.

Use the decorator to update how many times the reminder was shown.

Use a loop to keep showing reminders until the list is empty.

Use del to remove reminders with 3 times.

🧪 Bonus Challenge (Optional):
Log when each reminder was shown (date and time).

Ask for user input to confirm “Done” for the task before deleting it.
"""




import time                          # STEP 1: Importing time module
import random                        # STEP 2: Importing random module
from datetime import datetime        # STEP 3: Importing datetime module





# 🎯 Step 1: List of reminders
reminders = [                        # STEP 4: Creating list of tasks with count
    {"task": "Drink Water", "times": 0},
    {"task": "Eye Exercise", "times": 0},
    {"task": "Stretch Body", "times": 0}
]





# 🎯 Step 2: Decorator to track how many times a task is shown
def track_calls(func):              # STEP 5: track_calls gets defined (not run yet)
    def wrapper(reminder):          # STEP 6: inner wrapper function defined
        reminder["times"] += 1      # STEP 10: increase count when wrapper is called
        return func(reminder)       # STEP 11: call the original show_reminder function
    return wrapper                  # STEP 7: wrapper is returned






@track_calls                        # STEP 8: decorator applied — show_reminder = track_calls(show_reminder)
def show_reminder(reminder):       # STEP 9: original show_reminder defined
    now = datetime.now().strftime("%H:%M:%S")  # STEP 12: get current time
    print(f"\n🔔 [{now}] Reminder: {reminder['task']} (Shown {reminder['times']} times)")  # STEP 13: print task
    input("✅ Press Enter after completing the task...")  # STEP 14: wait for user input






# 🎯 Step 4: Loop like a cron job
while reminders:                   # STEP 15: loop runs while reminders list is not empty
    reminder = random.choice(reminders)   # STEP 16: randomly pick a reminder
    show_reminder(reminder)              # STEP 17: call show_reminder (actually calls wrapper due to decorator)

    # 🎯 Step 5: Check if task was shown 3 times — then delete
    if reminder["times"] >= 3:           # STEP 18: check if reminder shown 3 times
        print(f"🗑️ Removing task: {reminder['task']} (done 3 times)")  # STEP 19: print removal message
        index = reminders.index(reminder)  # STEP 20: find index of reminder in list
        del reminders[index]               # STEP 21: delete reminder using del

    time.sleep(10)                         # STEP 22: wait 10 seconds before next loop





print("\n🎉 All reminders completed! Well done!")  # STEP 23: final message when loop ends

