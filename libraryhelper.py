"""
This module is helpful for finding out the callable functions of an object(another library or class).
"""
def display(obj,name,doc):
	print name
	if(doc):
		print obj.__doc__

def callable_functions(obj,doc=False,grep=None):
	"""Gives a list of callable functions of the specified object(obj)
If doc is set to True, prints the __doc__ of the attribute.
If grep is specified(i.e you are only interested in a function mentioned by grep) prints the name and __doc__ if it is callable"""
	flag=False
	for i in dir(obj):
		temp=getattr(obj,str(i))
		if (callable(temp)):
			if(grep==None):
				display(temp,str(i),doc)		
			else:
				if str(i)==grep:
					flag=True
					display(temp,str(i),doc)
					return
				else: 
					flag=False
	if(not flag and grep):
		print "This is not a callable function\nTry help(obj,function_name)"


def help(obj,function_name):
	"""Prints the __doc__ and callable status of any function(function_name) of the object(obj)"""
	try:
		temp=getattr(obj,function_name)
	except Exception, exc:
		print "No such function exists in the object"
		return
	if(callable(temp)):
		print "This is a callable function"
	else:
		print "This function is not callable"
	print temp.__doc__
	

