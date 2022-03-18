# Implementation
Once you are done editing a `demo_*.py` file or writing your own Python script, follow the instructions on this section to run the script in the background. First, however, ensure that the script (e.g., `script.py`) has at least permission to be executed, as follows:

```sh
sudo chmod +x script.py
```

Similarly, file ownership can be configured via `chown`.  For example, to set the user `pi` as owner of the file `script.py`, run the following:

```sh
sudo chown pi script.py
```

## Systemd
Use the following procedure to run any LCD Python script as a (systemd) service:

1. Create a new unit file in `/lib/systemd/system/` called `rpi-lcd.service`:
   ```sh
   sudo nano /lib/systemd/system/rpi-lcd.service
   ```

2. Copy and paste the following in the new unit file:
   ```sh
   [Unit]
   Description=RPi Python script for a 16x2 LCD

   [Service]
   Type=simple
   ## Edit the following according to the script permissions
   User=pi
   #Group=users

   ## Edit the following with the full path to the compatible Python version and your script
   ExecStart=/usr/bin/python /path/to/script.py

   Restart=always
   RestartSec=5

   KillMode=process
   KillSignal=SIGINT

   [Install]
   WantedBy=multi-user.target
   ```

3. Enable the service and start it:
   ```sh
   sudo systemctl enable rpi-lcd.service
   sudo systemctl start rpi-lcd.service
   ```

4. Check that the LCD is displaying the correct information; otherwise, check the service status:
   ```sh
   systemctl status rpi-lcd.service
   ```
