import asyncio

from rf_module import check_rf_signal
from acoustic_module import check_acoustic_sound
from decision_module import make_decision
from yolo_module import start_yolo


async def autonomous_tracking(drone):
    print("Autonomous tracking mode started")

    await drone.mission.pause_mission()

    print("mission paused")
#----------camera frame center position,640pix-----------
    target_x=400
    center_x=320
# ----check targt direction relative to camera center-------
    if target_x > center_x + 50:
        print("target on right , rotere right ")
    elif target_x <center_x - 50:
         print("target on left , rotere left ")
    else:
        print("target cantered ,keep tracking")



async def monitor_sensors(drone):
    await asyncio.sleep(1)

    scan_count = 0

    while True:

        scan_count += 1
        print(f"\nMonitoring scan #{scan_count}")

 # RF
        rf_signal = check_rf_signal()
        print("RF:", rf_signal)


# Sound 
        sound_type, sound_score = check_acoustic_sound()
        print("Sound:", sound_score)


 # Dectected start
        rf_detected = rf_signal in [
            "drone",
            "telemetry",
            "long_range_signal"
        ]

        sound_detected = (

    sound_type == "propeller"

    and sound_score >= 70

)

        print("rf_detected:", rf_detected)
        print("sound_detected:", sound_detected)

# Open YOLO when RF or sound is SUSPICIOUS
        
        if rf_detected or sound_detected:

            print(
                f"Suspicious detected | "
                f"RF: {rf_signal} | "
                f"Sound: {sound_score}%"
            )

            print("Opening camera now...")
            yolo_score = start_yolo()
            print("YOLO score:", yolo_score)

            yolo_detected = yolo_score >= 70

        else:
            yolo_score = 0
            yolo_detected = False

    # Decision 
        decision, confidence, threat_level, action = make_decision(

            rf_detected=rf_detected,
            acoustic_detected=sound_detected,
            yolo_detected=yolo_detected,

            rf_score=50 if rf_detected else 0,
            sound_score=sound_score,
            yolo_score=yolo_score
        )

        print(
            f"Decision: {decision} | "
            f"Confidence: {confidence}% | "
            f"Threat level: {threat_level}"
        )

        print(f"Action: {action}")
# --------make final decision using sensor fusion------
    # Confirmed target
        if decision == "CONFIRMED_DRONE":

            print("done confirmed")
            print("decision:start autonomous tracking")


            await autonomous_tracking(drone)

            print("Mission paused because drone confirmed")

            break

        elif decision == "SUSPICIOUS_OBJECT":
            print("suspicious object, opening camera verification...")

            yolo_result= start_yolo()

            if yolo_result>=70:

                print("Yolo confirmed drone")
                print("decision:start autonomous tracking")

                await autonomous_tracking(drone)

                break

            else:

                print("Yolo did not confirm")
                print("continue monitoring")
                


        await asyncio.sleep(0.2)

    ############future improvement :
   ########### #add optical and infrared scanning
   ########### #for better drone detection accuracy