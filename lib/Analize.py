from ccxt import exchanges as Lec
import requests as rq
import xmltodict as x2d


def DataAnalyze(dataText: str,chn):
    """ for Get Data And Analyze For Output
    Example -> 3,143 BTC ($153,013,170) transfered from Unknown / 3143 BTC from[unknown] -> [unknown]
    """
    USDAPI = 'http://parsijoo.ir/api?serviceType=price-API&query=Currency'
    if 'transfered' in dataText or 'transferred' in dataText:
        print('DataFormat : True\nStart Analyze')
    else:
        print('Can\'t Analyze The Data')
        return False
    if chn == 'WhaleBotAlerts':
        dataText = dataText.rstrip('TX - link @WhaleBotAlerts')
    elif chn == 'whale_alert_io':
        dataText = dataText.rstrip('Details')
    print(dataText)
    # Variables
    # Emoji Warning -> for Warning Code Show Bigger Warning
    emj_warning = '\U0001f6a8'
    # Warning Code for emj_warning in data
    WarningCode = 0
    # Get Digital currency Type from database and analyze
    Type = None
    # Get Value Digital currency
    ValueOfType = ''
    # from This wallet transfered to [toLoc]
    fromLoc = None
    # for test in function
    test = None
    # from [fromLoc] transfered to [toLoc]
    toLoc = None
    # output
    output = ''
    # Start Work
    FOUNDHTTP = dataText.find('http')
    dataText = dataText[:FOUNDHTTP]
    for v in dataText:
        if v == emj_warning:
            WarningCode += 1
            dataText = dataText.strip(emj_warning)
        else:
            lenend = WarningCode
    i = 0
    findSharp = dataText.find('#')
    testc = dataText[findSharp:dataText.find('(')-1]
    TypeOf = testc.strip('#')
    findprice = dataText[dataText.find('(')+1:dataText.find(')')]
    print(findprice)
    for dd in dataText:
        try:
            dataText = dataText.strip(emj_warning)
        except Exception as err:
            break
    dataText = emj_warning + emj_warning+ dataText
    for v in dataText:
        i += 1
        test = str(dataText[:findSharp])
        test = str(test[lenend+1:])	
        test = test.split(',')
        work = ''
    for val in test:
        work += str(val)
        ValueOfType = str(work)
        lenend = lenend + i - 1
    try:
        ValueOfType.strip(' ')
        fromLoc = dataText.find('from')
        fromLoc = dataText[fromLoc+5:]
        test = fromLoc.find('to')
        fromLoc = fromLoc[:test].strip(' ')
        toLoc = dataText.find('to')
        toLoc = dataText[toLoc+3:].strip(' ')
        for i in Lec:
            if fromLoc.lower() in i or fromLoc in i:
                fromLoc = f"#{fromLoc}"
            if toLoc.lower() in i or toLoc in i:
                toLoc =f"#{toLoc}"
        
        if 'unknown' in fromLoc.lower() or 'Unknown' in fromLoc:
            fromLocp = 'ناشناخته'
        else:
            fromLocp = fromLoc
        if 'unknown' in toLoc.lower() or 'Unknown' in toLoc:
            toLocp = 'ناشناخته'
        else:
            toLocp = toLoc
        print('WarningCode : ' , WarningCode)
        print('Value : ',ValueOfType)
        print(fromLoc , 'to' , toLoc)
        obj = x2d.parse(rq.get(USDAPI).text)
        USD_IRR = obj['main']['sadana-services']['price-service']['item'][0]['price']
        return [{"warningcode" : WarningCode, 'from' : fromLocp, 'to' : toLocp, 'usd' : USD_IRR, 'value' : ValueOfType, 'type' : TypeOf, 'price' : findprice.strip('USD').strip(' ') },{"warningcode" : WarningCode, 'from' : fromLoc, 'to' : toLoc, 'value' : ValueOfType, 'type' : TypeOf, 'price' : findprice}]
    except Exception as err:
        print(f'Error IN app {err}')
        return False
    

