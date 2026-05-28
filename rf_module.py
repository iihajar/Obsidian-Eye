


import random

#---------simulate RF signal scanning--------
def check_rf_signal():
# common drone communication frequencies
    print("Scanning RF signals...")
    frequencies=[2.4,
                 #GHz drone.wifi
             5.8,
             915,
             433] #MHz telemetry  433,915
#bluetooth nearby wireless device
    
    #for frequencies in frequencies
    frequencies = random.choice(frequencies)
    signal_strength = random.randint(0,100)
        

    if frequencies ==2.4 and signal_strength>= 70:
        signal_type= "drone"
    
    elif frequencies ==5.8 and signal_strength>= 60:
        signal_type= "drone"

    elif frequencies ==915 and signal_strength>= 65:
        signal_type= "telemetry"

    elif frequencies ==433 and signal_strength>= 65:
        signal_type= "long_range_signal"
    else:
        signal_type="unknown"



    print(f"Detected signal: {signal_type}")
    return signal_type


    
   
