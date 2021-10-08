import json

timePeriods = ["00:00:00-12:00:00", "12:00:00-24:00:00"]

data = {
    "refreshingPeriodMsec": 5000,

    "acceptSelection": {
        "strategy": "pointAndAmount"
    },

    timePeriods[0]: {
        "batteryStatus": {
            "3840-": "excess",
            "2400-3840": "sufficient",
            "1920-2400": "scarce",
            "-1920": "short"
        },
        "request": {
            "excess": {"discharge": {
                "limitWh": 3840,
                "pointPerWh": 10
            }},
            "sufficient": {},
            "scarce": {},
            "short": {"charge": {
                "limitWh": 1920,
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
