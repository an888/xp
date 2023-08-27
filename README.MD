# Nintendo Switch Virtual Controller with Raspberry Pi

Tested on Raspberry Pi 400
Raspberry Pi OS 32 bit

## Setup
https://github.com/Brikwerk/nxbt/tree/master
https://github.com/Brikwerk/nxbt/blob/master/docs/Macros.md

## Remote Connection
VS Code + Remote SSH Extension

## How to run the macro using CLI
```
sudo nxbt macro -c test.txt -r
```

## Connection Error - Restart bluetooth
```
systemctl stop bluetooth.service
systemctl start bluetooth.service
```