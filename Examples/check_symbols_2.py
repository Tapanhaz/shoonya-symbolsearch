'''
It checks the nearest BANKNIFTY expiry is within 6 days or not.
If not it will try to redownload it. It should solve current shoonya's wrong symbolmaster error.
*** The symbolsearch module will not download the symbolmaster again within the same day
    once initialized 
    unless ==>
        1. The downloaded csv is deleted.
        2. The search_config.json deleted.
        3. Using hard_refresh=True when initializing symbols.
'''


from symbolsearch import SearchScrip
from datetime import datetime
from time import sleep

def isWithinSixDays(input_date,expiryDate):
    diff = expiryDate - input_date
    return 0 <= diff.days <= 7

def check_symbols(exch_list,hard_refresh=False, retry=1):
    sc.initialize_symbols(exch_list=exch_list, hard_refresh=hard_refresh)
    cur_expiry = sc.get_expiry()
    if not isWithinSixDays(input_date=current_date, expiryDate=cur_expiry):
        if retry <= 10:
            print(f"Retry == {retry}")
            sleep(3)
            check_symbols(sc=sc,exch_list=exch_list,current_date=current_date,hard_refresh=True, retry= retry+1)
        else:
            print("Error Fetching Correct Symbolmaster.")
    else:
        print("Symbolmaster Initialized.")

if __name__ == "__main__":
    sc = SearchScrip()
    exch_list = ['NFO'] #['NSE','NFO']
    current_date = datetime.now().date()
    check_symbols(exch_list=exch_list)
