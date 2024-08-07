import time
from plyer import notification
import datetime
import random as rd


def return_time_periodically(interval_hours):
    while True:
        current_time = datetime.datetime.now()
        next_time = current_time + datetime.timedelta(hours=interval_hours)
        sleep_time = (next_time - current_time).total_seconds()
        time.sleep(sleep_time)
        title = rd.choice(titles)
        notification.notify(
            title=f'{title}',
            message=f'{sleep_time} hrs have passed',
            app_icon=None,  # Optional icon path
            timeout=10  # Notification duration in seconds
        )


interval = int(input("Enter after how much time you want the reminders "))
titles = ["Friendly Reminder", "It's Time to Drink Water", "Let's have a drink", "34", "324"]
return_time_periodically(interval)


