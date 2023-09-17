# Fire Detection with YOLO

This project uses the YOLO (You Only Look Once) architecture from Ultralytics to detect fires in video streams. The detections are displayed in real-time and can optionally be saved to a text file or an annotated video.

## Dependencies:

- `supervision`
- `ultralytics`
- `numpy`
- `datetime`
- `time`
- `cv2`
- `os`
- `argparse`

## Usage:

### Basic Command:


```
python detect_fire.py
```


This command will start the fire detection on the default camera source (usually your webcam).

### Optional Arguments:

- `--save_txt`: If provided, the detections will be saved to a txt file in a directory named `labels`.
  
- `--save_res`: If provided, the video stream with the annotated detections will be saved in a directory named `pred_result`.

Example:

```
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




