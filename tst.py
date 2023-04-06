import multiprocessing
import subprocess
import os
import time

def run_detect():
    # Define the command to run detect.py
    command = ["python", "detect.py", "--source", "0", "--weights", "yolov5s.pt", "--img", "416", "--save-txt"]

    # Use subprocess module to run the command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check for q key press every 1 second
    while True:
        time.sleep(1)
        if os.path.isfile('quit.txt'):
            # Terminate the process
            process.terminate()

            # Reset the dangers.txt file
            open('dangers.txt', 'w').close()
            print("detect.py process terminated and dangers.txt file reset.")
            break

    # Print the output and error messages (if any)
    output, error = process.communicate()
    print("detect.py output:\n", output.decode())
    print("detect.py errors:\n", error.decode())

def run_alert():
    # Define the command to run alert.py
    command = ["python", "alert.py", "--arg1", "value1", "--arg2", "value2"]

    # Use subprocess module to run the command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check for q key press every 1 second
    while True:
        time.sleep(1)
        if os.path.isfile('quit.txt'):
            # Terminate the process
            process.terminate()
            print("alert.py process terminated.")
            break

    # Print the output and error messages (if any)
    output, error = process.communicate()
    print("alert.py output:\n", output.decode())
    print("alert.py errors:\n", error.decode())

if __name__ == '__main__':
    # Create two processes to run the scripts
    p1 = multiprocessing.Process(target=run_detect)
    p2 = multiprocessing.Process(target=run_alert)

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the q key press to terminate the processes and reset the dangers.txt file
    while True:
        quit_input = input("Press q to quit: ")
        if quit_input == 'q':
            # Create the quit.txt file to signal the processes to terminate
            open('quit.txt', 'w').close()

            # Wait for the processes to terminate
            p1.join()
            p2.join()
            break

    # Remove the quit.txt file
    os.remove('quit.txt')
