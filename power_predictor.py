import psutil
import time

start_time = None
end_time = None

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

if __name__ == '__main__':
    initialise()
