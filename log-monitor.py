import os
import logging
import time
import signal
import sys

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='\n%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Reads keywords from ./keywords.txt to search for in the log file
with open('keywords.txt', 'r') as file:
    keywords_to_monitor = [line.strip() for line in file.readlines()]

# Dictionary to store counts of each keyword
keyword_counts = {keyword: 0 for keyword in keywords_to_monitor}

# Clear Screen
os.system('clear')

# Function to monitor log file
def monitor_log(log_file_path):
    try:
        with open(log_file_path, 'r') as log_file:
            log_file.seek(0, 2)
            while True:
                new_line = log_file.readline()
                if new_line:
                    for keyword in keywords_to_monitor:     # Check if the keyword is found in the log output
                        if keyword.lower() in new_line.lower():
                            keyword_counts[keyword] += 1
                    logger.info(f"[+] New log entry: {new_line.strip()}")
                time.sleep(0.1)
    except FileNotFoundError:
        logger.error(f"[x] Log file '{log_file_path}' not found. Exiting.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"[?] Error occurred: {e}")
        sys.exit(1)

def generate_summary_report():
    print()
    print("[+] Summary Report:\n")
    sorted_keyword_counts = dict(sorted(keyword_counts.items(), key=lambda item: item[1], reverse=True)) # Sorted to show top keywords
    for keyword, count in sorted_keyword_counts.items():
        print(f"\t[*] {keyword.title()}: {count}")
    print()

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 log-monitor.py <log_file_path>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logger.info(f"[+] Monitoring -> {log_file_path}. Press Ctrl+C to stop.")

    try:
        monitor_log(log_file_path)
    except KeyboardInterrupt:
        logger.info("[!] Monitoring Stopped.")
        generate_summary_report() # Generate summary report at the end of logging
