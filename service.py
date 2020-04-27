import hug
import random

@hug.get()
def echoThere():
	return{
		'project':'Dockerization', 
		'language':'Python', 
		'status':'alive'
	}
	
