import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile


def fire_detected(result):
    

    if (result[0].boxes is None):
        return False

    detection_tensor = result[0].boxes


    
    if len(detection_tensor) > 0:
        return True
    else:
        return False


def process_frame(frame, model):
    result = model(frame)
    
    if not fire_detected(result):
        print("Success: No fire detected!")
    
    return fire_detected(result)



def main():
    st.title("Fire Detection using YOLO")
    st.subheader("For CMU Computer Vision Course")
    
    uploaded_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
    
    rets = []
    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(uploaded_file.read())
        
        st.video(tfile.name)
        
        model = YOLO('models/fire.pt')
        
        video = cv2.VideoCapture(tfile.name)
        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break
            
            annotated_frame = process_frame(frame, model)
            rets.append(annotated_frame)
            
        if rets.count(True) > 0:
            st.success("Fire detected!")
        else:
            st.error("No fire detected!")
        video.release()

    

if __name__ == "__main__":
    main()