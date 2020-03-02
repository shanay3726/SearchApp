from app import app
from flask import render_template
from yelpapi import YelpAPI 

yelp_api = YelpAPI('bW_9l9UbOK43YgVZOvElByHS8EiWj2AdyWJRw4oArWfQ0ankq6kJG8oAiseRgJNsWG4SnhY4L65swJmbZ5VDbVFDkHvDmgrlrFCUhjSUAfZqd-LYxoj86o2mM8FPXnYx')
def getice():
	RESTAURANTS = yelp_api.search_query(term='ice cream', location='austin, tx', sort_by='rating', limit=5)
	RESTAURANTS1 = yelp_api.search_query(term='food', location='austin, tx', sort_by='rating', limit=5)
	RESTAURANTS2 = yelp_api.search_query(term='restaurants', location='austin, tx', sort_by='rating', limit=5)

	#print(RESTAURANTS)
	busy=(RESTAURANTS['businesses'])
	busy1=(RESTAURANTS1['businesses'])
	busy2=(RESTAURANTS2['businesses'])
	count =0;
	ice=[]
	for i in busy:
		ice.append(i)
	for i in busy1:
		ice.append(i)
	for i in busy2:
		ice.append(i)
	return ice

def getcat():
	#yelp_api = YelpAPI('bW_9l9UbOK43YgVZOvElByHS8EiWj2AdyWJRw4oArWfQ0ankq6kJG8oAiseRgJNsWG4SnhY4L65swJmbZ5VDbVFDkHvDmgrlrFCUhjSUAfZqd-LYxoj86o2mM8FPXnYx')
	CAT = yelp_api.business_query(id='amys-ice-creams-austin-3')
	print(CAT)
	busyy=(CAT['categories'])
	count =0;
	cat=[]
	for i in busyy:
		cat.append(i)
	return cat

@app.route('/')
@app.route('/index')
def index():
	ice=getice()
	cat=getcat()
	return render_template('index.html',title='Home', ice=ice, cat=cat)

