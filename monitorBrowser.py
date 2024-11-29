import subprocess
import re
import time

# List of browser process names to monitor
browsers = ["chrome", "firefox", "msedge", "brave", "safari"]

def monitor_browser_activity():
    while True:
        try:
            # Execute wmctrl command to get active window details
            result = subprocess.check_output(["wmctrl", "-lp"], encoding='utf-8')
            active_window = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"], encoding='utf-8').strip()
            
            for browser in browsers:
                if browser in active_window.lower():
                    print(f"Active Browser: {browser.capitalize()}")
                    print(f"Window Title: {active_window}")
                    
                    # Extract URL from the window title
                    url = extract_url_from_title(active_window)
                    if url:
                        print(f"Detected URL: {url}")
                    
            time.sleep(2)
        
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

def extract_url_from_title(title):
    url_pattern = re.compile(r'https?://[^\s]+')
    match = url_pattern.search(title)
    if match:
        return match.group(0)
    return None

if __name__ == "__main__":
    monitor_browser_activity()

