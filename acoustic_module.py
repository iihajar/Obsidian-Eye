


import random

#
def check_acoustic_sound():
    print("Listening for drone sound...")

    sounds = [
        "propeller",
        "car",
        "wind",
        "noise",
        "none"
    ]
#simulate sound intensity level
    sound_type = random.choice(sounds)
    #Simulate sound intensity based on sound type

    if sound_type == "propeller":

        sound_level = random.randint(65, 100)

    elif sound_type == "car":
       sound_level = random.randint(40, 60)

    elif sound_type == "wind":
        sound_level = random.randint(20, 50)

    elif sound_type == "noise":
        sound_level = random.randint(10, 55)

    else:
        sound_level = 0


    print(f"Detected sound: {sound_type}")
    print(f"sound level: {sound_level}")

    
    
    return sound_type, sound_level 
#acoustic detection may produce false positives , so it is combined with RF and YOLO verification
    
