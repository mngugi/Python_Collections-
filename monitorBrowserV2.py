import psutil
import subprocess
import socket
import re
import time

browsers = ["chrome", "firefox", "msedge", "brave", "safari"]

def get_network_connections(pid):
    """Retrieve network connections for a given PID."""
    try:
        # Use lsof to list open network connections
        result = subprocess.check_output(f"lsof -Pan -p {pid} -i", shell=True, encoding='utf-8')
        connections = []
        for line in result.splitlines():
            if "TCP" in line:
                parts = line.split()
                local_address = parts[-2]
                remote_address = parts[-1]
                connections.append((local_address, remote_address))
        return connections
    except subprocess.CalledProcessError:
        return []

def monitor_browser_activity():
    while True:
        for process in psutil.process_iter(['pid', 'name']):
            try:
                if any(browser in process.info['name'].lower() for browser in browsers):
                    print(f"\nBrowser Detected: {process.info['name']} (PID: {process.info['pid']})")
                    
                    # Fetch and display network connections
                    connections = get_network_connections(process.info['pid'])
                    if connections:
                        for local, remote in connections:
                            print(f"Local: {local}, Remote: {remote}")
                    else:
                        print("No active network connections found.")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    monitor_browser_activity()

