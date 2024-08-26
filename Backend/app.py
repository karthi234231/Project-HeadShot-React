from flask import Flask, request, jsonify
import subprocess
import psutil
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Global variable to keep track of the running process
current_process = None

def terminate_process(process):
    if process:
        try:
            parent = psutil.Process(process.pid)
            for child in parent.children(recursive=True):
                child.terminate()
            parent.terminate()
        except psutil.NoSuchProcess:
            pass

@app.route('/run_script', methods=['POST'])
def run_script():
    global current_process
    data = request.get_json()
    script_name = data.get('script')

    # Terminate any running process before starting a new one
    if current_process:
        terminate_process(current_process)
        current_process = None

    if script_name == 'face_detection':
        current_process = subprocess.Popen(['python', 'facedetection.py'])
    elif script_name == 'face_tracking':
        current_process = subprocess.Popen(['python', 'facetracking.py'])
    elif script_name == 'tracking_system':
        current_process = subprocess.Popen(['python', 'MotionDetection.py'])

    return jsonify({"status": "Script started"}), 200

@app.route('/stop_script', methods=['POST'])
def stop_script():
    global current_process

    if current_process:
        terminate_process(current_process)
        current_process = None

    return jsonify({"status": "Script stopped"}), 200

if __name__ == '__main__':
    app.run(debug=True)


import cv2

# Open the camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Using DirectShow backend as an example

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break  # Exit the loop if no frame is captured

    # Process the frame (e.g., display or perform face detection)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()