import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Hey ya!",
            message="You're doing Good. Keep going :)",
            app_icon= r"C:\Users\Neha\PycharmProjects\desktop notifier\icon.ico",
            timeout=10
        )
        time.sleep(3600)