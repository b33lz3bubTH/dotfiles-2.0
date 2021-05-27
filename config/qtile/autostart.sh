#!/bin/sh

# systray battery icon
#cbatticon -u 5 &
# systray volume
xcompmgr -cfF -t-9 -l-11 -r9 -o.95 -D6 &
volumeicon &
nitrogen --restore &
