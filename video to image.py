import cv2

# Open the video file
video = cv2.VideoCapture("video2.mp4")

# Get the video frame rate
frame_rate = video.get(cv2.CAP_PROP_FPS)

# Get the total number of frames in the video
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Extract 24 frames per second and save them as images
frame_number = 0
while True:
    success, frame = video.read()
    if not success:
        break
    if frame_number % int(frame_rate / 24) == 0:
        cv2.imwrite("frame_{}.jpg".format(frame_number), frame)
    frame_number += 1

# Release the video file
video.release()