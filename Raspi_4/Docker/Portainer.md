ref:
    https://pimylifeup.com/raspberry-pi-portainer/

### Install
sudo apt update
sudo apt upgrade

sudo docker pull portainer/portainer-ce:latest

sudo docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest

http://[PIIPADDRESS]:9000
    192.168.11.88


