# API-REST-Bibus
API REST Bibus in python3 from "https://geo.pays-de-brest.fr/donnees/Documents/Public/DocWebServicesTransport.pdf"

Example :
print(api.getStop("ISEN"))

[
    {
        "Stop_id": "ISEN_1",
        "Stop_lat": "48.40663812328",
        "Stop_lon": "-4.49582390658722",
        "Stop_name": "ISEN"
    },
    {
        "Stop_id": "ISEN_2",
        "Stop_lat": "48.4067199238482",
        "Stop_lon": "-4.49565841134279",
        "Stop_name": "ISEN"
    }
]

## Requirements
pip3 install requests
