import json

# set time periods for scenario files
timePeriods = ["00:00:00-12:00:00", "12:00:00-24:00:00"]
# battery Size: 4800
batterySize = 4800

data = {
    "refreshingPeriodMsec": 5000,

    "acceptSelection": {
        "strategy": "pointAndAmount"
    },

    timePeriods[0]: {
        "batteryStatus": {
            str(batterySize*0.8): "excess",
            str(str(batterySize*0.5) + "-" + str(batterySize*0.8)): "sufficient",
            str(str(batterySize*0.4) + "-" + str(batterySize*0.5)): "scarce",
            str(batterySize*0.4): "short"
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
            "3360-": "excess",
            "2400-3360": "sufficient",
            "1440-2400": "scarce",
            "-1440": "short"
        },
        "request": {
            "excess": {"discharge": {
                "limitWh": 3360,
                "pointPerWh": 10
            }},
            "sufficient": {},
            "scarce": {},
            "short": {"charge": {
                "limitWh": 1440,
                "pointPerWh": 10
            }}
        },
        "accept": {
            "excess": {"discharge": {
                "limitWh": 2400,
                "pointPerWh": 10
            }},
            "sufficient": {"discharge": {
                "limitWh": 2400,
                "pointPerWh": 10
            }},
            "scarce": {"charge": {
                "limitWh": 2400,
                "pointPerWh": 10
            }},
            "short": {"charge": {
                "limitWh": 2400,
                "pointPerWh": 10
            }}
        }
    }
}

# generate scenario.json file
with open('scenario.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
