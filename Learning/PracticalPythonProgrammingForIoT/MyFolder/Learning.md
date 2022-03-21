This is learning for book Practical Python Programming for IoT (Book)



### Support starting with system
    1. Edit run_on_boot.sh
    2. Make it excutable 
        chmod u+x run_on_boot.sh
    3. Edit crontab
    4. Run run_on_boot.sh manually in terminal and check the logs, make sure it works
    5. Reboot raspi and check the results

> Task: test on raspi

### Configuring GPIO interfaces
- Enable all interfaces (VNC...)
    > Task: Make note into guide 1st boot into raspi (Notion)
- Config GPIO daemon
    - sudo systemctl enable pigpiod
    - sudo systemctl start pigpiod
    > Task: Make note into guide 1st boot into raspi (Notion)

### Install pip3 libs
    - requirements.txt
    - pip install -r requirements.txt

### global in python
https://www.programiz.com/python-programming/global-keyword

khi khai bao global trong func, thi func co the thay doi gia tri variable ngoai func

### Handle internet, requests 
Using, ref in dweet_led.py
<!-- # while True to reconnect on any disconnections. -->

### Hide the explorer VSC
command + B

### Create class for object
ref in pigpio_led_class.py as ref

### Chapter5 will do connect pi to physical world and threading managing

