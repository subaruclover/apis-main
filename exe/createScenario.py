# create by Qiong
# create scenario files for updating the energy exchange rules

import json
import time

# set time periods for scenario files
timePeriods = ["00:00:00-12:00:00", "12:00:00-24:00:00"]
# battery Size: 4800
batterySize = 4800

data1 = {
    "refreshingPeriodMsec": 5000,

    "acceptSelection": {
        "strategy": "pointAndAmount"
    },

    timePeriods[0]: {
        "batteryStatus": {
            str(batterySize*0.8) + "-": "excess",
            str(str(batterySize*0.5) + "-" + str(batterySize*0.8)): "sufficient",
            str(str(batterySize*0.4) + "-" + str(batterySize*0.5)): "scarce",
            "-" + str(batterySize*0.4): "short"
        },
        "request": {
            "excess": {"discharge": {
                "limitWh": batterySize*0.8,
                "pointPerWh": 10
            }},
            "sufficient": {},
            "scarce": {},
            "short": {"charge": {
                "limitWh": batterySize*0.4,
                "pointPerWh": 10
            }}
        },
        "accept": {
            "excess": {"discharge": {
                "limitWh": batterySize*0.5,
                "pointPerWh": 10
            }},
            "sufficient": {"discharge": {
                "limitWh": batterySize*0.5,
                "pointPerWh": 10
            }},
            "scarce": {"charge": {
                "limitWh": batterySize*0.5,
                "pointPerWh": 10
            }},
            "short": {"charge": {
                "limitWh": batterySize*0.5,
                "pointPerWh": 10
            }}
        }
    },

    timePeriods[1]: {
        "batteryStatus": {
            str(batterySize*0.7) + "-": "excess",
            str(str(batterySize*0.5) + "-" + str(batterySize*0.7)): "sufficient",
            str(str(batterySize*0.3) + "-" + str(batterySize*0.5)): "scarce",
            "-" + str(batterySize*0.3): "short"
        },
        "request": {
            "excess": {"discharge": {
                "limitWh": batterySize*0.7,
                "pointPerWh": 10
            }},
            "sufficient": {},
            "scarce": {},
            "short": {"charge": {
                "limitWh": batterySize*0.3,
                "pointPerWh": 10
            }}
        },
        "accept": {
            "excess": {"discharge": {
                "limitWh": batterySize*0.5,
                "pointPerWh": 10
            }},
            "sufficient": {"discharge": {
                "limitWh": batterySize*0.5,
                "pointPerWh": 10
            }},
            "scarce": {"charge": {
                "limitWh": batterySize*0.5,
                "pointPerWh": 10
            }},
            "short": {"charge": {
                "limitWh": batterySize*0.5,
                "pointPerWh": 10
            }}
        }
    }
}

# generate scenario.json file
t_end = time.time() + 60 * 15  # run for 15 min x 60 s = 900 seconds.
while time.time() < t_end:
    print(time.time())

    with open('scenario.json', 'w') as jsonfile:
        json.dump(data1, jsonfile)

    print("scenario file updated")
    # refresh every 5 seconds
    time.sleep(5)

# with open('scenario.json', 'w') as jsonfile:
#     json.dump(data1, jsonfile)
