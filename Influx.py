""" Send a line-protocol message to a database
""" 
import urequests

def send(database, influx_data):
    """ Send line protocol to an Influx database
    
    Args:
        database:    URL of the database to post data to
        influx_data: Influx line protocol message to write
        
    Returns:
        HTTP result code
        
    Exceptions:
        None
        
    Side effects:
        Writes data to a database
    """
    try:
        response = urequests.post(database, data=influx_data)
    except OSError:
        response.status_code = 500
        
    return response.status_code
