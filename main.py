# main file connected the drone ,upload the mission
# start safety check , run the monitoring system

import asyncio
from mavsdk import System


from mission_items import create_mission
from rf_module import check_rf_signal
from acoustic_module import check_acoustic_sound
from yolo_module import start_yolo
from decision_module import make_decision
from check_module import (check_connection,
                          check_arm,
                          check_battery,
                          check_altitude
                          )
from monitor_module import monitor_sensors

     

async def run():
    drone = System()
     

            
#connected drone 
    await drone.connect(system_address="udp://:14540")
    await check_connection(drone)
    print("connected drone done")
    
#uploading mission
    mission_plan = await create_mission(drone)
    
    

    print(f"uploading mission")
    await drone.mission.upload_mission(mission_plan)
    await asyncio.sleep(5)

#arm
    await drone.action.arm()
    print("drone armed")

#check
    asyncio.create_task(check_battery(drone))
    asyncio.create_task(check_altitude(drone))



    print(f"start drone mission")
    await drone.mission.start_mission()
   # await asyncio.sleep (1)
    
    
# monitor missioning , start sonser monitoring    

    sensor_task =None
    
    async for mission_progress in drone.mission.mission_progress():
     print(f"mission_progress= {mission_progress.current} /{mission_progress.total}")
     
     if mission_progress.current >= 0 and sensor_task is None:
         sensor_task= asyncio.create_task( monitor_sensors(drone))

     if mission_progress.current == mission_progress.total:
            print("mission completed")
            await asyncio.sleep(5)
            break
   
   
    if sensor_task:
        sensor_task.cancel()


#land after mission completion
    print("landing ....")
    await drone.action.land()
    await asyncio.sleep(10)


asyncio.run(run())