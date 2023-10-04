#!/bin/bash

# Check if monitors are active/connected
HDMIActive=$(xrandr --listmonitors | grep "HDMI-0" -q && echo true || echo false)
HDMIConnected=$(xrandr | grep "^HDMI-0" | grep disconnected -q && echo false || echo true)
eDPActive=$(xrandr --listmonitors | grep "eDP-1-1" -q && echo true || echo false)

# Enable eDP if it's not already
if ! $eDPActive; then
    if $HDMIActive; then
        xrandr --output eDP-1-1 --auto --left-of HDMI-0
    else
        xrandr --output eDP-1-1 --auto
    fi
    eDPActive=true
fi

# Connect/disconnect HDMI
if $HDMIConnected && $eDPActive && ! $HDMIActive; then
    xrandr --output HDMI-0 --auto --right-of eDP-1-1
    xrandr --output HDMI-0 --primary
    openbox --restart # prevent combining 2 monitors
elif $HDMIActive && ! $HDMIConnected; then
    xrandr --output HDMI-0 --off
fi
