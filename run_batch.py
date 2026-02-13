"""
Windows Batch Script Runner
Run this to execute the scraper from Windows Task Scheduler
"""

import subprocess
import sys
import os

# Change to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    """Run the scraper (called by batch file)"""
    
    print("PoE2 Data Scraper - Batch Runner")
    print("=" * 50)
    
    # Run price update
    print("Running price update...")
    result = subprocess.run(
        [sys.executable, "main.py", "--prices"],
        capture_output=False
    )
    
    if result.returncode == 0:
        print("✓ Update completed successfully")
        sys.exit(0)
    else:
        print("✗ Update failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
