# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:19:35 2024

@author: iamrs
"""

import time
import sys

def main():
    light_seconds_per_hour = 3600
    light_seconds_per_minute = 60
    
    sys.stdout.write("Current time (light hours): ")
    sys.stdout.flush()
    total_light_seconds = 0

    while True:
        hours = total_light_seconds // light_seconds_per_hour
        minutes = (total_light_seconds % light_seconds_per_hour) // light_seconds_per_minute
        seconds = total_light_seconds % light_seconds_per_minute

        sys.stdout.write("\r{:02}:{:02}:{:02}".format(hours, minutes, seconds))
        sys.stdout.flush()
        time.sleep(1)  # Update every second
        total_light_seconds += 1

if __name__ == "__main__":
    main()
