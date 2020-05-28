""" Connect to the Wi-Fi
"""
import time
import network

def connect_wifi(ssid, passphrase):
    """ Connect to the WiFi
    
    Args:
        ssid, passphrase
        
    Returns:
        interface or None on error
        
    Exceptions:
        Should raise a connectionError, but I can't work out how to do so!
        
    Side effects:
    """
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        print('Already connected!')
        return sta_if
    else:
        print('Connect to {}'.format(ssid), end='')
        sta_if.active(True)
        sta_if.connect(ssid, passphrase)

        for t in range(0, 120):
            print('.', end='')
            if sta_if.isconnected():
                print('success!')
                return sta_if
            time.sleep_ms(500)
            if t == 40 or t == 80:
                # One more try....
                print('\nRetrying: ', end='')
                sta_if.disconnect()
                sta_if.active(False)
                time.sleep(1)
                sta_if.active(True)
                sta_if.connect(ssid, passphrase)

    # Unable to connect
    raise ConnectionRefusedError("Unable to connect to Server")
