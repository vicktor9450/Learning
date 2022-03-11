# Main

## Data Source:
    - sensors
        - Wire (GPIOs)
            - Temp
            - Humid
            - Motion
            - Light
        - Wireless (MQTT, ZigBee)
            - Temp
            - Humid
    - internet, API
        - Weather
        - Location
        - Webscraping

## Realtime Analytic - Data processing, cleanse
Sensors >>>> mqtt, zigbee... Protocol   >>>> Apache kafka >>> 
    >>> DB Sink Service
    >>> Consumer for realtime analytic, also producer to kafka 
.>>>> Graph, Plot 
## Database - NoSQL