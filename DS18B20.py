""" Read the DS18B20 temperature sensors and return an Influx line-protocol version of the results
""" 

import onewire
import ds18x20
import Config

""" A dict lookup is used to convert DS probe IDs into nicer names, if you want to
"""
dsNames    = { '28ffc5a9b1170476':'fridge'  , 
               '28fff15cb117041d':'freezer' ,
               '280c1345921602ad':'fridge'  ,
               '28610d45921602fa':'freezer' , }

def read_ds(pin, location):
    """Scan the 1-wire bus for DS18B20 probes and return an Influx line-protocol set of results
    
    Args:
        pin:       The pin the 1-ware bus is connected to
        location:  The location field to be included in the Influx line-protocol tag
        
    Return:
        A string containing the required Influx line-protocol message
        
    Exceptions:
        None
    
    Side-effects:
        Prints a commentary of progress
    """
    measurement = ''

    try:
        ow = onewire.OneWire(pin)
        ds = ds18x20.DS18X20(ow)

        ds_sensors = ds.scan()
        ds.convert_temp()
        
        for ds_sensor in ds_sensors:
            # Convert the DS sensor ID into a 16-character hex string
            id = ''.join('{:02x}'.format(x) for x in ds_sensor)

            # Try to convert the sensor ID into a name
            try:
                name = dsNames[id]
            except KeyError:
                name = id

            # Add the result to the list
            measurement += 'temperature,location={0},type={1} value={2}\n'.format(location, name, ds.read_temp(ds_sensor))
    except onewire.OneWireError as e:
        print("No OneWire found")

    return measurement
