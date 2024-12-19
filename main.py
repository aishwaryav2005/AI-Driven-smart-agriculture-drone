from image_capture import capture_image
from image_analysis import send_image_to_ai
from feedback_processing import process_feedback

# Capture an image
image_path = capture_image()

# Send the image to the AI API
analysis = send_image_to_ai(image_path)

# Process and display feedback
process_feedback(analysis)
