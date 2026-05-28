


from ultralytics import YOLO
import cv2

model=YOLO("yolov8n.pt")
#open camera for visual verification
def start_yolo():
    print("starting YOLO")
    
    cap=cv2.VideoCapture(0)
    print("camera opened:", cap.isOpened())

    if not cap.isOpened():
       print("camera not opened")
       return 0
# confirm target only after repeated detections 
    scan_count=0
    detected_count=0
    required_count=3

    
    while scan_count< 20:
        ret,frame =cap.read()
        
        if not ret:
            print("camera frame not received")
            break

        print(f"scanning area {scan_count}")
        scan_count +=1


        results = model(frame, device="cpu")
        for result in results:
         for box in result.boxes:
            class_name=model.names[int(box.cls[0])]
            confidence=float(box.conf[0])

            print(
               f"Detected:{class_name}|"
               f"Confidence: {confidence:.2f}"
            )
           
            if class_name== "drone" and confidence>=0.70:
                detected_count+=1
                print(f"possible drone:{confidence:.2f}")
                if detected_count >= required_count:
                   
                  print(f"-------------wirning drone detected:{confidence:.2f} ")
#return confidence score if drone is confirmed
                  cap.release()
                  cv2.destroyAllWindows()
                  return  int (confidence*100)
            else:
               detected_count=0
        
        
        annotated_frame = results[0].plot()
        cv2.imshow("YOLO Drone detection",annotated_frame)
        if cv2.waitKey(100)&0xFF ==ord("q"):
          break
    cap.release()
    cv2.destroyAllWindows()
 # return 0 if no drone detected
    return 0
