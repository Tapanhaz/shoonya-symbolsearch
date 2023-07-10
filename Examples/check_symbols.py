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