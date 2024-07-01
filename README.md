# Interface Parser

This is a script that allows you to take output from the command 

    show run | section interface

and convert this into a .json file. 

## History 

This script came about as I had need to iterate over a multi stack switch, 
looking for specific configuration that possibly existed on over 100 interfaces.
To ensure i didnt make human error. I created the script to determine which 
interfaces the configuration was present on.

Not all configuration is currently supported, but this can be easilly programmed. 

## Running this script

Feel free to play with the sample file 

    Show_Run_Interface.txt

This file contains configuration for 24 Gigabit interfaces.
When the script runs it will generate an output.json file. 


