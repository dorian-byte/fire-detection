import supervision as sv
from ultralytics import YOLO
import numpy as np
import datetime
import time
import cv2
import os

import datetime
import argparse

def detect_fire(source=0, save_txt=False, save_res=False, model_path='models/fire.pt'):
    count = 0
    start_time = time.time()
    video_id_count = 0
    fourcc = cv2.VideoWriter_fourcc(*"MP4V")
    box_annotator = sv.BoxAnnotator(thickness=2, text_thickness=1, text_scale=0.5)

    if save_txt and not os.path.exists('labels'):
        os.mkdir('labels')
    

    if save_res and not os.path.exists('pred_result'):
        os.mkdir('pred_result')

    model = YOLO(model_path)
    iter_model = iter(model.track(source=source, show=False, stream=True))

    flag_save_video = 1

    try:
        while True:
            result = next(iter_model)
            img_trail = result.orig_img
            org = np.copy(img_trail)

            detections = sv.Detections.from_ultralytics(result)

            fire_indices = [i for i, class_id in enumerate(detections.class_id) if model.model.names[class_id] == 'fire']
            labels = [f"Fire {detections.confidence[i]:0.2f}" for i in fire_indices]

            if save_txt:
                with open('labels/result.txt', 'a') as f:
                    f.write(f'Detections: {labels} Time: {datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")}\n')

            img_box = box_annotator.annotate(scene=org, detections=detections, labels=labels)

            cv2.imshow('Fire Detection', img_box)
            cv2.waitKey(1)

            if save_res and flag_save_video:
                video_output_path = f'pred_result/video_result_{video_id_count}.mp4'
                height, width, _ = img_box.shape
                out = cv2.VideoWriter(video_output_path, fourcc, 25, (width, height), True)
                flag_save_video = 0

            if save_res:
                out.write(img_box)

            count += 1
            if count % 3 == 0 and count >= 3:
                fps = int(3 / (time.time() - start_time))
                print(f"FPS: {fps}")
                start_time = time.time()

    except StopIteration:
        print('Detection complete.')
        if save_res:
            out.release()

    except KeyboardInterrupt:
        print('Detection stopped by user.')
        if save_res:
            out.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fire Detection using YOLO.')
    parser.add_argument('--save_txt', action='store_true', help='Save detections to a txt file.')
    parser.add_argument('--save_res', action='store_true', help='Save video results with annotations.')

    args = parser.parse_args()

    detect_fire(source=0, save_txt=args.save_txt, save_res=args.save_res)
