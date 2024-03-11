# use CLI to set an auto screenshot of the work in progress
 
import os
import argparse
import pyautogui
import time

parser = argparse.ArgumentParser()

# Set the parameters on the CLI 
parser.add_argument("-p", "--path", help="absolute path to store screenshot.", default=r"./images")
parser.add_argument("-t", "--type", help="h (hour) m ( minutes) or s ( seconds)", default='h')
parser.add_argument("-f", "--frequency", help="frequency for taking screenshot per h/m/s.", default=1, type=int)

args = parser.parse_args()

sec = 0.0

if args.type == 'h':
    sec = 60 * 60 / args.frequency
elif args.type == 'm':
    sec = 60 / args.frequency

if sec < 1.0:
    sec = 1.0

if os.path.isdir(args.path) != True:
    os.mkdir(args.path)

try:
    while True:
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)
        file = current_time + ".jpg"
        image = pyautogui.screenshot(os.path.join(args.path,file))
        print(f"{file} saved successfully.\n")
        time.sleep(sec)

except KeyboardInterrupt:
    print("user interrupt")