import platform
import os

# Get OS name and version
os_name = platform.system()
os_version = platform.version()
os_release = platform.release()
os_details = platform.uname()

print(f"OS Name: {os_name}")
print(f"OS Version: {os_version}")
print(f"OS Release: {os_release}")
print(f"Detailed OS Information: {os_details}")
