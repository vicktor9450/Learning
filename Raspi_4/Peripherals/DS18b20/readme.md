
Phần setup Có thể nhúng trong file setup.sh như ở trong phân setup của 16x2 LCD , git clone của lcd-master

# SETUP
sudo nano /boot/config.txt
add dtoverlay=w1-gpio in the bottom
save and reboot sudo reboot
sudo modprobe w1-gpio
sudo modprobe w1-therm

data to GPIO#4