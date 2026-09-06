"""
Alarm Clock
A simple console-based alarm clock. Set an alarm time (HH:MM:SS, 24-hour format)
and the program will alert you when the current time matches it.

Uses only built-in sound options — no external audio files needed:
- Windows: winsound.Beep() generates a tone directly
- Mac/Linux: repeated terminal bell characters
"""

import datetime
import time
import platform

IS_WINDOWS = platform.system() == "Windows"

if IS_WINDOWS:
    import winsound


def validate_time_format(alarm_time):
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        return True
    except ValueError:
        return False


def alert():
    print("⏰ Wake up! Alarm ringing! ⏰")
    if IS_WINDOWS:
        # frequency (Hz), duration (ms) — repeat a few times
        for _ in range(5):
            winsound.Beep(1000, 400)
            time.sleep(0.2)
    else:
        # Terminal bell, repeated so it's hard to miss
        for _ in range(5):
            print("\a", end="", flush=True)
            time.sleep(0.5)


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting...")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            alert()
            break
        time.sleep(1)


def main():
    print("=== Alarm Clock ===")
    print("Enter time in 24-hour format (HH:MM:SS)")

    while True:
        alarm_time = input("Set alarm time: ").strip()
        if validate_time_format(alarm_time):
            break
        print("Invalid format. Please use HH:MM:SS (e.g., 14:30:00).")

    set_alarm(alarm_time)


if __name__ == "__main__":
    main()

