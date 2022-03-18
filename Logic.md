# Main

## Data Source:
    - sensors
        - Wire (GPIOs)
            - Temp
            - Humid
            - Motion
            - Light
        - Wireless (MQTT, ZigBee) https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-python-module?view=iotedge-2020-11
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

### MQTT payload wrapping
https://www.hivemq.com/blog/mqtt-raspberrypi-part03-sending-sensor-data-hivemqcloud-pico/

### Sensors
#### Prepare hardware - connectting

#### Prepare software - code


## Database - NoSQL



## DEVOPS with 5 pizero 2w
 
Sử dụng docker swarm để scale/ deploy lên raspi zero
Phần cứng bao gồm:
    - Nguồn: 1 pcs
    - Cáp nguồn đến pi: 5
    - Pi zero 2w: 5 pcs with attached heatsink
    - Cáp tín hiệu màn hình: 1 > DONE
    - Cluster barebone case
    - Thẻ nhớ: 128gb * 5


### Tasks:
- Lam case, xay dung phan cung de setup stack of pi

### Manage docker swarm
https://www.portainer.io/?hsLang=en

### Prepare boot img for raspi zero 2w

specs: sdcard 128gb

original raspi 64bit img > configuring ip address > locale > language

### Deploy on docker swarm
- cassandra: https://ralph.blog.imixs.com/2019/06/24/cassandra-and-docker-swarm/
- mqtt: load balancer for getting data in
- kafka: https://collabnix.com/implementing-apache-kafka-on-docker-swarm-running-on-aws-platform-in-5-minutes/


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