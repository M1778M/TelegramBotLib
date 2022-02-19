def DataAnalyze(dataText: str):
	""" for Get Data And Analyze For Output
	    Example -> 3,143 BTC ($153,013,170) transfered from Unknown / 3143 BTC from[unknown] -> [unknown]
	"""
    
	if 'transfered' in dataText:
		print('DataFormat : True\nStart Analyze')
	else:
		print('Can\'t Analyze The Data')
		return False
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
	for v in dataText:
		if v == emj_warning:
			WarningCode += 1
		else:
			lenend = WarningCode
	i = 0
	findSharp = dataText.find('#')
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
		fromLoc = dataText.find('from')
		fromLoc = dataText[fromLoc+5:]
		test = fromLoc.find('to')
		fromLoc = fromLoc[:test]
		toLoc = dataText.find('to')
		toLoc = dataText[toLoc+3:]
		print('WarningCode : ' , WarningCode)
		print('Value : ',ValueOfType)
		print(fromLoc , ' to' , toLoc)
	except Exception:
		print('Error IN app')
# End Of Function DataAnalyze for test[1]

DataAnalyze('\U0001f6a8\U0001f6a8 3,143 #BTC ($153,013,170) transfered from Unknown to BNNTS')
