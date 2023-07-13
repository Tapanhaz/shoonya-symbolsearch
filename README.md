# shoonya-symbolsearch

<div class="cell markdown">
    
    Code for downloading and searching scrips in Shoonya symbolmaster 

</div>

<div class="cell code" execution_count="3">

``` python
from symbolsearch import SearchScrip
```

</div>


<div class="cell code" execution_count="6">

``` python
sc = SearchScrip()
```

</div>

<div class="cell markdown">

    Now its needed to initialize symbols of the required exchanges. 

    It will not not download the symbolmaster for a exchange within the same day twice unless

    it is specified by using hard_refresh=True

</div>

<div class="cell code" execution_count="8">

``` python
exch_list = ['NSE', 'NFO']
sc.initialize_symbols(exch_list=exch_list)
```

</div>

<div class="cell markdown">

get_expiry(exch, instrument, symbol, expiry) By default, it returns
current expiry of banknifty options

</div>

<div class="cell code" execution_count="9">

``` python
sc.get_expiry()
```

<div class="output execute_result" execution_count="9">

    datetime.date(2023, 7, 13)

</div>

</div>

<div class="cell code" execution_count="10">

``` python
sc.get_expiry(exch='NFO', instrument='FUTIDX', symbol='FINNIFTY',expiry='current')
```

<div class="output execute_result" execution_count="10">

    datetime.date(2023, 7, 25)

</div>

</div>

<div class="cell markdown">

search_scrip(exch, \*\*kwargs)

    The function will return in 3 different ways depending on the inputs

    1. if **kwargs params are symbol, instrument, optiontype, expiry, strikeprice then it 
    will return corresponding tradingsymbol and token

    2. if **kwargs params are same as point 1 but lacks any of the input then it will 
    return a dict of  tradingsymbols and tokens

    3. if **kwargs input is tradingsymbol then it will return the corresponding token

</div>

<div class="cell code" execution_count="11">

``` python
sc.search_scrip(exch='NFO', symbol='BANKNIFTY', instrument='OPTIDX', 
                optiontype='CE', expiry="13-7-2023", strikeprice=44000)
```

<div class="output execute_result" execution_count="11">

    array(['BANKNIFTY13JUL23C44000', 41702], dtype=object)

</div>

</div>

<div class="cell code" execution_count="12">

``` python
sc.search_scrip(exch='NFO', symbol='BANKNIFTY', instrument='OPTIDX', 
                expiry="13-7-2023", strikeprice=44000)
```

<div class="output execute_result" execution_count="12">

    {'BANKNIFTY13JUL23P44000': 41703, 'BANKNIFTY13JUL23C44000': 41702}

</div>

</div>

<div class="cell code" execution_count="13">

``` python
sc.search_scrip(exch='NFO', tradingsymbol='BANKNIFTY13JUL23C44000')
```

<div class="output execute_result" execution_count="13">

    41702

</div>

</div>

<div class="cell markdown">

get_tradingsymbol(exch, \*\*kwargs)

    Returns tradingsymbol

    **kwargs params are symbol, instrument, optiontype, strikeprice, expiry for 'NFO', 
    'MCX' & 'CDS'

    **kwargs params are symbol, instrument for 'NSE'

</div>

<div class="cell code" execution_count="14">

``` python
sc.get_tradingsymbol(exch='NFO', symbol='BANKNIFTY', instrument='OPTIDX', 
                optiontype='CE', expiry="13-7-2023", strikeprice=44000)
```

<div class="output execute_result" execution_count="14">

    'BANKNIFTY13JUL23C44000'

</div>

</div>

<div class="cell code" execution_count="15">

``` python
sc.get_tradingsymbol(exch='NSE', symbol='HDFC', instrument='EQ')
```

<div class="output execute_result" execution_count="15">

    'HDFC-EQ'

</div>

</div>

<div class="cell markdown">

get_lotsize(exch, \*\*kwargs)

    Returns lotsize of the given symbol.

    1. **kwargs -> tradingsymbol

    2. **kwargs -> symbol, expiry

    3. **kwargs -> symbol (lacks accuracy as it will return the lotsize 
            regardless of expiry.)

</div>

<div class="cell code" execution_count="16">

``` python
sc.get_lotsize(exch='NFO', symbol='BANKNIFTY')
```

<div class="output execute_result" execution_count="16">

    25

</div>

</div>

<div class="cell code" execution_count="17">

``` python
sc.get_lotsize(exch='NFO', symbol='BANKNIFTY', expiry='27-7-2023')
```

<div class="output execute_result" execution_count="17">

    15

</div>

</div>
