""" Configuration file for the <wherever> NodeMCU
"""
import machine
import dht

# Change the log location here
location   = 'garage'

# Add IDs to this if you want more human-friendly names for 1-wire probes
dsNames    = { '28ffc5a9b1170476':'fridge'  , 
               '28fff15cb117041d':'freezer' ,
               '280c1345921602ad':'fridge'  ,
               '28610d45921602fa':'freezer' , }

# Where are the devices connected
onewirePin = machine.Pin(4)
dhtPin     = dht.DHT22(machine.Pin(14))

# Deep sleep or doze?
deep_sleep = False