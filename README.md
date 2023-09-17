# Fire Detection with YOLO

This project uses the YOLO (You Only Look Once) architecture from Ultralytics to detect fires in video streams. The detections are displayed in real-time and can optionally be saved to a text file or an annotated video.

## Requirements:

- Python version: 3.10.2
- To install the necessary packages, run: 

```
pip install -r requirements.txt
```

## Usage:

### Basic Command:


```bash
python detect_fire.py
```


This command will start the fire detection on the default camera source (usually your webcam).

### Optional Arguments:

- `--save_txt`: If provided, the detections will be saved to a txt file in a directory named `labels`.
  
- `--save_res`: If provided, the video stream with the annotated detections will be saved in a directory named `pred_result`.

Example:

```bash
python detect_fire.py --save_txt --save_res
```


## Output:

- If `--save_txt` is provided, a text file named `result.txt` will be created in the `labels` directory. Each line of the file will contain the detection label and the timestamp.

- If `--save_res` is provided, a video file named `video_result_X.mp4` (where X is an incrementing number) will be saved in the `pred_result` directory.

## Notes:

- The detection will run indefinitely until stopped by the user. You can stop the detection by pressing `Ctrl+C` in the terminal.

- The code calculates and displays the Frames Per Second (FPS) every 3 frames.

- For custom sources other than the default camera, modify the `source` argument in the `detect_fire` function call.

## Contributing:

Feel free to raise issues or submit pull requests. Your contributions are always welcome!





# FRONTEND APP: Fire Detection using YOLO

This application uses the Ultralytics YOLO model to detect fire in uploaded videos. 

## Features

- **Upload Video**: Users can upload videos in formats like `.mp4`, `.mov`, and `.avi`.
- **Fire Detection**: The application processes the video and uses the YOLO model to check for fire occurrences.
- **Results**: After processing, the application provides feedback on whether a fire was detected in the uploaded video.

## How it Works

1. **Video Upload**: A user uploads a video via the Streamlit interface.
2. **Video Processing**: Each frame of the uploaded video is processed using the pretrained YOLO model to detect fire.
3. **Results Display**: The application provides feedback based on the detection results.

## Demo

![Demo](./videos/demo.gif)
## Code Overview

- `fire_detected(result)`: This function checks if fire is detected in the given result.
- `process_frame(frame, model)`: Processes each frame of the video to detect fire.
- `main()`: Main function that manages the Streamlit interface and video processing.

## Usage

To run the application:

```bash
streamlit run fte.py
```
