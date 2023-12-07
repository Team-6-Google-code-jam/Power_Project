import psutil
import time

start_time = None
end_time = None
import getpass
import os
USER_NAME = getpass.getuser()



# Sample values for the idle and max power (just for reference)
# idle_power = 20
# max_power = 80

# Assumes linear relationship between cpu usage and wattage
def get_power(idle_power, max_power):
    cpu_usage = psutil.cpu_percent() / 100
    # linear interpolation from idle to max power using the cpu percentage as the factor
    estimated_power = idle_power + cpu_usage * (max_power - idle_power)
    return estimated_power

# run this function to store the start time, and to dump it into the file
def initialise():
    start_time = time.time()
    with open('timestamp.txt', 'w') as f:
        f.write(str(start_time))

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(
            os.path.realpath(__file__)
            )
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(
        bat_path + '\\' + "open.bat", "w+"
        ) as bat_file:
        bat_file.write(
            r'start "" "%s"' % file_path
            )

if __name__ == '__main__':
    initialise()
