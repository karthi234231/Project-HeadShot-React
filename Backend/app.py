from flask import Flask, request, jsonify
import subprocess
import psutil
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variable to keep track of the running process
current_process = None

def terminate_process(process):
    if process:
        try:
            logger.info(f'Terminating process with PID: {process.pid}')
            parent = psutil.Process(process.pid)
            for child in parent.children(recursive=True):
                logger.info(f'Terminating child process with PID: {child.pid}')
                child.terminate()
            parent.terminate()
            parent.wait()  # Ensure the process is cleaned up
        except psutil.NoSuchProcess:
            logger.warning('Process not found or already terminated')

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
    else:
        return jsonify({"status": "Unknown script"}), 400

    return jsonify({"status": "Script started"}), 200

@app.route('/stop_script', methods=['POST'])
def stop_script():
    global current_process

    if current_process:
        terminate_process(current_process)
        current_process = None
        return jsonify({"status": "Script stopped"}), 200
    else:
        return jsonify({"status": "No script is running"}), 400

if __name__ == '__main__':
    app.run(debug=True)
