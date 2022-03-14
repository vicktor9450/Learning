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

# TODO: Làm sao để khởi tạo system > add các module vào được nhỉ

Ví dụ như là: Sau khi raspi khởi động sẽ chạy docker - system nào đó,

turn off raspi - connect các thiết bị ngoại vi, thông số kết nối
turn on raspi - chạy *.py connect vào running system với thông số và protocol nhất định, gồm các bước test connect > test sample >running > removing protocol (thiết bị này sẽ relate với các phần cứng khác như thế nào - theo thứ tự cần đủ)

tưởng tượng giống như con tàu điện đang chạy, chạy đến điểm đó, toa tàu tách ra, các phần còn lại tiép tục đi tiếp, các tàu cần dùng sẽ ở lại, ghép nối, module

micro services 
distributed system

cài đặt requirements bằng file requirements.txt

cách tốt nhất là dùng docker
- docker cho raspi
- docker cho raspi zero

ưu điểm: 
- shutdown hệ thống không cần tắt raspi
- Microservices control
- 

Nhươc điểm:
- vì là container nên không kiểm soát được version
- cần nhiều thời gian hơn để học docker
- 