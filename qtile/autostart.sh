#!/bin/bash

picom &
nitrogen --restore &
nm-applet &
pkill -f volumeicon
sleep 1
volumeicon &
sudo udisksctl mount -b /dev/sdb1 &
