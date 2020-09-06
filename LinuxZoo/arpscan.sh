#!/bin/bash
for i in {161..166}; do
        arping -c 2 10.0.2.$i | grep 'bytes from' | awk '{print " possible target up at: " $4 " " $5}' | sort -u
done
