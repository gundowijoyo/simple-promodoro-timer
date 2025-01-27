import time

def pomodoro_timer():
    while True:
        print("Work for 25 minutes!")
        time.sleep(25 * 60)  # 25 menit
        print("Take a 5-minute break!")
        time.sleep(5 * 60)  # 5 menit

if __name__ == "__main__":
    pomodoro_timer()
    
