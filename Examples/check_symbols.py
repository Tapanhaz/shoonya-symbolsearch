'''
    The nse workday library can be used to get the holidays / workday's list
as per nse trading holidays. It have some more functions.
I am not making that package open source for some reason. 
If using win X64, python 3.10 / 3.11 the library can be installed by pip install nse-workday
more info on that here : https://github.com/Tapanhaz/nse_workday

    Here that library is used to get the nearest expiry of banknifty.( The get_weekdays function will return
the given required weekday within the given period. if the calculated weekday is a holiday, it will return nearest 
previous workday.

    This method should help to get correct symbolmaster. If not win X64, python 3.10 / 3.11 user or
do not like to use closed source libraries, please check the other solution.
'''

from symbolsearch import SearchScrip
from nse_workday import get_weekdays
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.DEBUG)

sc = SearchScrip()

def check_symbols(hard_refresh= False,retry= 1):
    today = datetime.now().date()
    nse_cur_expiry = get_weekdays(start_date=today, end_date=(today + timedelta(days=6)), required_weekday='thursday')[0]
    exch_list = ['NSE', 'NFO']
    sc.initialize_symbols(exch_list=exch_list, hard_refresh=hard_refresh)
    cur_expiry = sc.get_expiry(exch='NFO', instrument='OPTIDX', symbol='BANKNIFTY', expiry='current')
    if nse_cur_expiry.date() != cur_expiry:
        if retry <= 3:
            check_symbols(hard_refresh=True, retry=retry+1)
        else:
            print("Error updating symbols")

check_symbols()
