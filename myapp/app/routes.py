from app import app
from flask import render_template
from yelpapi import YelpAPI 

def getice():
	yelp_api = YelpAPI('bW_9l9UbOK43YgVZOvElByHS8EiWj2AdyWJRw4oArWfQ0ankq6kJG8oAiseRgJNsWG4SnhY4L65swJmbZ5VDbVFDkHvDmgrlrFCUhjSUAfZqd-LYxoj86o2mM8FPXnYx')
	RESTAURANTS = yelp_api.search_query(term='ice cream', location='austin, tx', sort_by='rating', limit=5)
	#pprint(RESTAURANTS)
	busy=(RESTAURANTS['businesses'])
	count =0;
	ice=[]
	for i in busy:
		ice.append(i)
	return ice

@app.route('/')
@app.route('/index')
def index():
	ice=getice()
	return render_template('try.html',title='Home', ice=ice)

