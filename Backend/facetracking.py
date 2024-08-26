# import cv2
# from cvzone.FaceDetectionModule import FaceDetector

# # Initialize webcam
# cap = cv2.VideoCapture(0)
# ws, hs = 1280, 720
# cap.set(3, ws)
# cap.set(4, hs)

# if not cap.isOpened():
#     print("Camera couldn't Access!!!")
#     exit()

# detector = FaceDetector()

# while True:
#     success, img = cap.read()
#     img, bboxs = detector.findFaces(img, draw=False)

#     if bboxs:
#         for bbox in bboxs:
#             x, y, w, h = bbox["bbox"]
#             fx = x + w // 2
#             fy = y + h // 4
#             pos = [fx, fy]
#             cv2.circle(img, (fx, fy), 80, (0, 0, 255), 2)
#             cv2.putText(img, str(pos), (fx + 15, fy - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
#             cv2.line(img, (0, fy), (ws, fy), (0, 0, 0), 2)
#             cv2.line(img, (fx, hs), (fx, 0), (0, 0, 0), 2)
#             cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED)

#         num_heads = len(bboxs)
#         cv2.putText(img, f'Targets Locked: {num_heads}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
#     else:
#         cv2.putText(img, "NO TARGET", (880, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
#         cv2.circle(img, (640, 360), 80, (0, 0, 255), 2)
#         cv2.circle(img, (640, 360), 15, (0, 0, 255), cv2.FILLED)
#         cv2.line(img, (0, 360), (ws, 360), (0, 0, 0), 2)
#         cv2.line(img, (640, hs), (640, 0), (0, 0, 0), 2)

#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
from cvzone.FaceDetectionModule import FaceDetector
import tkinter as tk
from PIL import Image, ImageTk

# Initialize webcam
cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()

detector = FaceDetector()

# Track faces and manage eliminations
tracked_faces = []
terminate_count = 0

def terminate_target():
    global terminate_count
    if tracked_faces:
        terminate_count += 1  # Mark one face as eliminated

# Setting up the GUI using Tkinter
root = tk.Tk()
root.title("Face Tracker with Terminate Button")

# Create a label to display the video feed
video_label = tk.Label(root)
video_label.pack()

terminate_button = tk.Button(root, text="Terminate", command=terminate_target)
terminate_button.pack()

def update_frame():
    global tracked_faces, terminate_count

    # Read frame from webcam
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        return

    # Detect faces
    img, bboxs = detector.findFaces(img, draw=False)

    # Adjust the tracked faces list based on eliminated faces
    if bboxs:
        tracked_faces = bboxs[:len(bboxs) - terminate_count]
    else:
        tracked_faces = []

    # Draw bounding boxes and other visual elements
    if tracked_faces:
        for bbox in tracked_faces:
            x, y, w, h = bbox["bbox"]
            fx = x + w // 2
            fy = y + h // 4
            pos = [fx, fy]
            cv2.circle(img, (fx, fy), 80, (0, 0, 255), 2)
            cv2.putText(img, str(pos), (fx + 15, fy - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            cv2.line(img, (0, fy), (ws, fy), (0, 0, 0), 2)
            cv2.line(img, (fx, hs), (fx, 0), (0, 0, 0), 2)
            cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED)

        num_heads = len(tracked_faces)
        cv2.putText(img, f'Targets Locked: {num_heads}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    else:
        cv2.putText(img, "NO TARGET", (880, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.circle(img, (640, 360), 80, (0, 0, 255), 2)
        cv2.circle(img, (640, 360), 15, (0, 0, 255), cv2.FILLED)
        cv2.line(img, (0, 360), (ws, 360), (0, 0, 0), 2)
        cv2.line(img, (640, hs), (640, 0), (0, 0, 0), 2)

    # Convert the image to RGB (Tkinter requires it)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(image=img_pil)

    # Update the video label with the new image
    video_label.img_tk = img_tk
    video_label.config(image=img_tk)

    # Call the function again after 10ms to create a loop
    video_label.after(10, update_frame)

# Start the video loop
update_frame()

# Run the Tkinter main loop
root.mainloop()

# Release the resources
cap.release()
cv2.destroyAllWindows()
