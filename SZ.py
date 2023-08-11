import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        remaining_time = end_time - time.time()
        minutes_remaining = int(remaining_time / 60)
        seconds_remaining = int(remaining_time % 60)
        
        print(f"Remaining Time: {minutes_remaining:02d}:{seconds_remaining:02d}", end="\r")
        time.sleep(1)
    
    print("Focus time is over. Take a break!")

# 设置专注时间为25分钟
focus_timer(25)
