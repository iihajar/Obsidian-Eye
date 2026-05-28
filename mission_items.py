from mavsdk.mission import MissionItem, MissionPlan
#Create autonomous mission points
async def create_mission(drone):
## Get home location coordinates
    home = await anext(drone.telemetry.home())

    lat = home.latitude_deg
    log = home.longitude_deg
    alt = 10.0
## Relative mission pattern points  
    points = [
        (0, 20),
        (-20, -10),
        (15, 0),
        (-20, 10),
        (0, -20),
        (0, 0)
    ]

    mission_items = []
##### Convert relative points into GPS mission items
    for x, y in points:

        mission_items.append(
            MissionItem(
                lat + x * 1e-5,
                log + y * 1e-5,
                alt,
                4.0,
                True,

                float("nan"),
                float("nan"),
                MissionItem.CameraAction.NONE,

                float("nan"),
                float("nan"),
                float("nan"),
                float("nan"),

                float("nan"),
                MissionItem.VehicleAction.NONE,
            )
        )

    return MissionPlan(mission_items)

