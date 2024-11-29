import psutil
import time

browsers = ["chrome", "firefox", "msedge", "brave", "safari"]

def monitor_browser_processes():
    while True:
        found = False
        for process in psutil.process_iter(['pid', 'name']):
            if any(browser in process.info['name'].lower() for browser in browsers):
                print(f"Browser detected: {process.info['name']} (PID: {process.info['pid']})")
                found = True
        
        if not found:
            print("No browsers detected.")
        time.sleep(5)

if __name__ == "__main__":
    monitor_browser_processes()

