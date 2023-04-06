import multiprocessing
import subprocess

def run_detect():
    # Define the command to run detect.py
    command = ["python", "detect.py", "--source", "0", "--weights", "yolov5s.pt", "--img", "416", "--save-txt"]

    # Use subprocess module to run the command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Print the output and error messages (if any)
    print("detect.py output:\n", output.decode())
    print("detect.py errors:\n", error.decode())

def run_alert():
    # Define the command to run alert.py
    command = ["python", "alert.py", "--arg1", "value1", "--arg2", "value2"]

    # Use subprocess module to run the command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Print the output and error messages (if any)
    print("alert.py output:\n", output.decode())
    print("alert.py errors:\n", error.decode())

if __name__ == '__main__':
    # Create two processes to run the scripts
    p1 = multiprocessing.Process(target=run_detect)
    p2 = multiprocessing.Process(target=run_alert)

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the processes to finish
    p1.join()
    p2.join()
