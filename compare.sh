#!/bin/bash


echo "================================================================================"
echo "================================= WITHOUT CHANGES =============================="
echo "================================================================================"
git apply -R fix.diff > /dev/null  # diff may not apply if already reverted
./python.exe demonstrate_change.py


echo "================================================================================"
echo "================================= WITH CHANGES ================================="
echo "================================================================================"
git apply fix.diff > /dev/null  # diff may not apply if already applied
./python.exe demonstrate_change.py
