import psutil
import time
import pygetwindow as gw
import re

# Function to monitor browser activity
def monitor_browser_activity():
    browsers = ["chrome.exe", "firefox.exe", "msedge.exe", "brave.exe", "safari.exe"]  # Add other browser names if needed
    
    while True:
        active_window = gw.getActiveWindow()
        if active_window:
            window_title = active_window.title.lower()
            process_name = active_window.title.split()[-1].lower()  # Extract process name
            
            if any(browser in process_name for browser in browsers):
                print(f"Browser Active: {process_name}")
                print(f"Window Title: {window_title}")
                
                # Extract URL if it's visible in the window title (common for Chrome and Firefox)
                url = extract_url_from_title(window_title)
                if url:
                    print(f"Detected URL: {url}")
        
        time.sleep(2)  # Check every 2 seconds

# Function to extract URLs from window titles
def extract_url_from_title(title):
    url_pattern = re.compile(r'https?://[^\s]+')
    match = url_pattern.search(title)
    if match:
        return match.group(0)
    return None

if __name__ == "__main__":
    monitor_browser_activity()

