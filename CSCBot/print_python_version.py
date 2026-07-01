import sys

# Get Python version info
version_info = sys.version_info
version = f"{version_info.major}.{version_info.minor}.{version_info.micro}"

print(f"This script is running on Python version {version}")
