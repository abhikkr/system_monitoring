
# Importing the library
import psutil
import time
import os
import sys
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import shutil
def monitor_cpu_usage():
            return psutil.cpu_percent(1)

def monitor_ram_percent():
       return(psutil.virtual_memory()[2])
    # Getting usage of virtual_memory in GB ( 4th field)
def ram_usage():
        return(psutil.virtual_memory()[3]/1000000000)
        time.sleep(1)
def file_system_monitor():
    if __name__ == "__main__":
        # Set the format for logging info
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
    
        # Set format for displaying path
        path = sys.argv[1] if len(sys.argv) > 1 else '.'
    
        # Initialize logging event handler
        event_handler = LoggingEventHandler()
    
        # Initialize Observer
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
    
        # Start the observer
        observer.start()
        try:
            while True:
                # Set the thread sleep time
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
        return observer
def file_sys_space():
    sys_path = os.getcwd()
    value = psutil.disk_usage(os.getcwd())
    # print('value',value)
    return value[3]
# print(file_sys_space())