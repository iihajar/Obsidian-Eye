import asyncio
from mavsdk import System


#check connection
async def  check_connection(drone:System):
        async for connection in drone.core.connection_state():
            if connection.is_connected:
                print("done connection")
                return


#check arm
async def  check_arm(drone:System):
        async for armed in drone.telemetry.armed():
            if armed:
              print("armed dron")
              return
 
 #check batter        
async def check_battery(drone:System):
     async for battery in drone.telemetry.battery():
          if battery.remaining_percent <= 0.25:
               print(f"--------low battery--------- returning...")
               await drone.action.return_to_launch()
               return

#check altitude and decision making,Plan1,Plan2 
async def check_altitude(drone:System):

     drone_started_flying = False
     last_altitude= None

     async for pos in drone.telemetry.position():
          alt = pos.relative_altitude_m
          if last_altitude != round(alt, 1):

               print(f"current altitude: {alt:.1f}")

               last_altitude = round(alt, 1)
          await asyncio.sleep(3)

          if alt >2:
               drone_started_flying = True

          if not drone_started_flying:
               continue

         
          if alt<2:
               print("----------+++++++++high warning altitude too low+++++++---------")
               await drone.mission.pause_mission()
               print("mission paused")
               print("altitude warning only ,returning to launch")
               await drone.action.return_to_launch()
               break
          
          
          elif alt < 3:
               print("-------------warning altitude too low--------")
               await drone.mission.pause_mission()
               print("+++++++increase in altitude++++++++")
               

               await drone.action.goto_location(
                    pos.latitude_deg ,pos.longitude_deg,
                    5,0
                    
               )
               await asyncio.sleep(3)

               await drone.mission.start_mission()

               print("plan B done")
                
               break