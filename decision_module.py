import asyncio



#---combine sensor results and calculate threat confidence ----
def make_decision(rf_detected,
                  acoustic_detected,
                  yolo_detected,
                  rf_score,
                  sound_score,
                  yolo_score):
  
  
  confidence= int(
    rf_score *0.3+
    sound_score*0.2+
    yolo_score *0.5
  )
  
  #--- calculate target confidence level----

  #high confidence target
  if  yolo_detected and confidence >= 80:
    threat_level="HIGH" 
    decision ="CONFIRMED_DRONE"
    action ="send alert and start autonomous tracking"

# medium confidence suspicious object 
  elif (rf_detected or acoustic_detected) and confidence >=50:
    threat_level="MEDIUM" 
    decision= "SUSPICIOUS_OBJECT"
    action="send alert,Rescan and open camera"

  else:
    threat_level= "LOW" 
    decision="NO_THREAT"
    action="continue monitoring"

  return decision ,confidence,threat_level ,action

