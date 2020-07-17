from datetime import date, timedelta



def get_today_in_quickstatements():

    '''
    Summary:
        Gets a string fo todays date in the format used in Quickstatements. 

    Returns 
        A string of the current day in the Quickstatements format.

    '''
    today = date.today()
    return today.strftime("+%Y-%m-%dT00:00:00Z/11")
