#!/bin/bash

echo "-- Begining of the script --"
echo "----- Listening -----"
python listener.py
echo "----- End of listening -----"
echo "----- Data processing -----"
python data_processing.py
echo "----- End of data processing -----"
echo "----- Opening Excel file -----"

`libreoffice *.xlsx`
