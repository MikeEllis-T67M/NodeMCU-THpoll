import Config    # Config for this specific NodeMCU
import WiFi      # Connect to the WiFi
import DS18B20   # Read Dallas DS18B20 sensor(s) and convert to Influx line-protocol
import DHT       # Read a DHT22 sensor and convert to Influx line-protocol
import Influx    # Send a line-protocol message to Influx
import Deepsleep # Go to sleep to save power
import time      # Non-deepsleep timing

import network
import machine

def main():
    print("\n\nStarting - {}".format(machine.reset_cause()))
    
    while True:
        try:
            # Establish WiFi connection here
            interface = WiFi.connect_wifi(Config.wifi_ssid, Config.wifi_pass)
            if interface:
                print('Connected: ', interface.ifconfig())

            # If we've got somewhere to write the data, read the sensors.
            # Deliberately do the DHT22 read last to maximise the chance of it having had long enough 
            # to stabilise (only one read every 2 seconds)
            measurements = ''
            measurements += DS18B20.read_ds(Config.onewirePin, Config.location)    
            measurements += DHT.read_dht(Config.dhtPin, Config.location)
            if measurements:
                print('\nSending to {}\n{}'.format(Config.database,measurements))
                print('HTTP:{0}'.format(Influx.send(Config.database, measurements)))   
            else:
                print('No sensors read successfully.')

        except KeyboardInterrupt:
            print("Caught keyboard interrupt")
            enter_sleep = False

        except Exception as e:
            import sys
            print("Unexpected error ", e)
            sys.print_exception(e)
        finally:
            if Config.deep_sleep:
                print('Zzzz....')
                Deepsleep.deep_sleep(Config.sampleTime * 1000)

        # This will only be executed if Deepsleep is disabled
        print('Dozing....')
        time.sleep(Config.sampleTime)

if __name__ == '__main__':
    main()
