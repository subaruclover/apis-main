import json

data = {
    "refreshingPeriodMsec": 5000,

    "acceptSelection": {
        "strategy": "pointAndAmount"
    },

    "00:00:00-24:00:00": {
        "batteryStatus": {
            "4320-": "excess",
            "3600-4320": "sufficient",
            "2880-3600": "scarce",
            "-2880": "short"
        },
        "request": {
            "excess": {
                "discharge": {
                    "limitWh": 4320,
                    "pointPerWh": 10
                }
            },
            "sufficient": {
            },
            "scarce": {
            },
            "short": {
                "charge": {
                    "limitWh": 2880,
                    "pointPerWh": 10
                }
            }
        },
        "accept": {
            "excess": {
                "discharge": {
                    "limitWh": 3600,
                    "pointPerWh": 10
                }
            },
            "sufficient": {
                "discharge": {
                    "limitWh": 3600,
                    "pointPerWh": 10
                }
            },
            "scarce": {
                "charge": {
                    "limitWh": 3600,
                    "pointPerWh": 10
                }
            },
            "short": {
                "charge": {
                    "limitWh": 3600,
                    "pointPerWh": 10
                }
            }
        }
    },
}

# generate scenario.json file
with open('scenario.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
