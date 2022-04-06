# Main Flow
Install rasbian img

initialize setting
    zram
    ssh cluster
    ip assign
cassandra
    download
    config
    install
    run
install docker
    init docker swarm
        nodered
        mqtt

## Required libs
    - pigpio (by Joan)
    - Anduino

## Ref link for raspi
    https://tutorials-raspberrypi.com
    
    https://www.youtube.com/channel/UCfY8sl5Q6VKndz0nLaGygPw

    Install docker

    rasp8 as master
        sudo docker swarm init --advertise-addr 192.168.11.8

        docker swarm join-token manager
            docker swarm join --token SWMTKN-1-53ml21n30ju3f4i6kwqzcrg7yxbj0unpb3ol29zef6vlzj2xa3-64nk1ee5jw265bmgluylclrdu 192.168.11.8:2377


    rasp4 as worker

        docker swarm join --token SWMTKN-1-53ml21n30ju3f4i6kwqzcrg7yxbj0unpb3ol29zef6vlzj2xa3-6fxi366fcck4h7xrwniyrqvzb 192.168.11.8:2377


    deploy nodered
        sudo docker service create --name mynodered -p :1880:1880 --replicas 1 --detach=true elzekool/rpi-nodered
    
    docker node rm ID
    docker swarm leave
    docker node demote

## Projects
### Smart agriculture
    https://tutorials-raspberrypi.com/smart-agriculture-system-using-iot-esp32-nodemcu/

### Google Coral
    https://tutorials-raspberrypi.com/using-tensorflow-lite-with-google-coral-tpu-on-raspberry-pi-4/





## Startup services
    - pigpio by Joan:
        
## Các loại sensor đang có và mục đích của chúng
    - Cảm biến ánh sáng: Nhận biết ánh sáng 
        - return dạng float
        - số lượng:
    - Cảm biến nhiệt độ - độ ẩm
        - Không dây
            - Xiaomi 
                - Số lượng: 2
        - Có dây 
            - DHT22
                - Số lượng: 1
    - Cảm biến nhiệt độ
        - Có dây
            - DS18B20
                - Số lượng: 10
                - return: float
    - Quạt  
        - 12v 3pin 7k rpm
            - số lượng: 1
        - 12v 4pin PWM 3k rpm
            - NZXT 140mm
                - Số lượng 1
        - 5v 2pin
            - 10mm
                - Số lượng: 3
            - 14mm
                - Số lượng: 1
    - Đèn UV cho rau
        - 12v 1m
            - Số lượng: 4
        - 5v 1m
            - Số lượng: 2
    - Relay
        - 4channel 
            - Số lượng: 1
        - 8channel 
            - Số lượng: 1
    - Màn hình hiện thị
        - 16digt
            - Số lượng

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

## Cassandra on kubernetes
https://www.datastax.com/learn/apache-cassandra-operations-in-kubernetes?utm_source=thenewstack&utm_medium=byline&utm_campaign=cassandra-docker&utm_term=all-plays&utm_content=TL34

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
# Clone backup multiple sdCard
    https://beebom.com/how-clone-raspberry-pi-sd-card-windows-linux-macos/

# DIY projects
- Auto-shaker pCB
    https://www.youtube.com/watch?v=DX881LdzVTU
# Buying 
    - Driller
        https://www.amazon.co.jp/-/en/dp/B007CEUH4Q/ref=emc_b_5_t?th=1

# Python project manage
    https://dev.to/awwsmm/managing-your-python-project-with-git-and-pybuilder-21if
# POE HAT
    https://www.cytrontech.vn/c-raspberry-pi/c-raspberry-pi-hat/c-hat-for-rpi-4/p-5v-5a-power-over-ethernet-plus-hat-for-raspberry-pi
