""" Read a DHT sensor and convert the result to an Influx line-protocol message
"""
import dht
import time

def read_dht(dht_sensor, location):
    """Read a DHT sensor and convert to Influx line-protocol
        
    Args:
        dht_sensor: The sensor to read
        location:   The tag value to be used in the Influx measurement
        
    Returns:
        string containing a line-protocol message
        
    Exceptions:
        
    Side effects:
        May sleep for up to 4 seconds to get around timeouts
    """
    measurement = ''
    tries = 0
    sensorReadSuccessful = False

    while tries < 2 and not sensorReadSuccessful:
    # Read the TH sensor
        try:
            # See if I can get away with just reading the sensor without sleeping
            tries += 1
            dht_sensor.measure()
            sensorReadSuccessful = True
            
            temp  = dht_sensor.temperature()
            humid = dht_sensor.humidity()

            measurement += 'temperature,location={0},type=room value={1}\n'.format(location, temp)
            measurement += 'humidity,location={0},type=room value={1}\n'.format(location, humid)
        except OSError as e:
            print("DHT timeout - sleeping")
            time.sleep(3)

    return measurement
