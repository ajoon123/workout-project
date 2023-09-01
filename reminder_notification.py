from datetime import datetime, timedelta
from plyer import notification

class FitnessTracker:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, message, time):
        self.reminders.append((message, time))

    def check_reminders(self):
        current_time = datetime.now()

        for reminder in self.reminders:
            message, time = reminder
            if current_time >= time:
                self.show_notification(message)
                self.reminders.remove(reminder)

    def show_notification(self, message):
        notification.notify(
            title="Fitness Tracker Reminder",
            message=message,
            timeout=10  
        )

def main():
    tracker = FitnessTracker()

    tracker.add_reminder("Time for a workout!", datetime.now() + timedelta(seconds=10))
    tracker.add_reminder("Drink water!", datetime.now() + timedelta(seconds=20))

    while True:
        tracker.check_reminders()

if __name__ == "__main__":
    main()
