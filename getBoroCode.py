def getBoroCode(bName):
	bName = bName.lower().replace('the','').replace(' ','')
	if bName.isdigit():
		return bName
	elif bName == 'manhattan':
		return '1'
	elif bName == 'newyork':
		return '1'
	elif bName == 'bronx':
		return '2'
	elif bName == 'kings':
		return '3'
	elif bName == 'brooklyn':
		return '3'
	elif bName == 'statenisland':
		return '5'
	elif bName == 'richmond':
		return '5'
	else:
		return '4'