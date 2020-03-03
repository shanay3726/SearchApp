from app import app
from flask import render_template
from yelpapi import YelpAPI 

yelp_api = YelpAPI('bW_9l9UbOK43YgVZOvElByHS8EiWj2AdyWJRw4oArWfQ0ankq6kJG8oAiseRgJNsWG4SnhY4L65swJmbZ5VDbVFDkHvDmgrlrFCUhjSUAfZqd-LYxoj86o2mM8FPXnYx')
RESTAURANTS = yelp_api.search_query(term='ice cream', location='austin, tx', sort_by='rating', limit=6)['businesses']
RESTAURANTS1 = yelp_api.search_query(term='food', location='austin, tx', sort_by='rating', limit=6)['businesses']
RESTAURANTS2 = yelp_api.search_query(term='shopping', location='austin, tx', sort_by='rating', limit=6)['businesses']
RESTAURANTS3 = yelp_api.search_query(term='salon', location='austin, tx', sort_by='rating', limit=6)['businesses']
RESTAURANTS4 = yelp_api.search_query(term='club', location='austin, tx', sort_by='rating', limit=6)['businesses']
RESTAURANTS5 = yelp_api.search_query(term='cafe', location='austin, tx', sort_by='rating', limit=6)['businesses']
RESTAURANTS6 = yelp_api.search_query(term='events', location='austin, tx', sort_by='rating', limit=6)['businesses']
RESTAURANTS7 = yelp_api.search_query(term='hotels', location='austin, tx', sort_by='rating', limit=6)['businesses']
	#print(RESTAURANTS)

def getice():
	count =0;
	ice=[]
	for i in RESTAURANTS:
		ice.append(i)
	for i in RESTAURANTS1:
		ice.append(i)
	for i in RESTAURANTS2:
		ice.append(i)
	for i in RESTAURANTS3:
		ice.append(i)
	for i in RESTAURANTS4:
		ice.append(i)
	for i in RESTAURANTS5:
		ice.append(i)
	for i in RESTAURANTS6:
		ice.append(i)
	for i in RESTAURANTS7:
		ice.append(i)
	return ice
@app.route('/salon')
def salon():
	ice=getice()
	return render_template('salon.html',title='Home', ice=ice)
@app.route('/shopping')
def shopping():
	ice=getice()
	return render_template('shopping.html',title='Home', ice=ice)
@app.route('/restaurants')
def restaurants():
	ice=getice()
	return render_template('restaurants.html',title='Home', ice=ice)
@app.route('/dessert')
def dessert():
	ice=getice()
	return render_template('dessert.html',title='Home', ice=ice)
@app.route('/cafe')
def cafe():
	ice=getice()
	return render_template('cafe.html',title='Home', ice=ice)
@app.route('/clubs')
def clubs():
	ice=getice()
	return render_template('clubs.html',title='Home', ice=ice)
@app.route('/events')
def events():
	ice=getice()
	return render_template('events.html',title='Home', ice=ice)
@app.route('/hotels')
def hotels():
	ice=getice()
	return render_template('hotels.html',title='Home', ice=ice)



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
def index():
	ice=getice()
	cat=getcat()
	return render_template('index.html',title='Home', ice=ice, cat=cat)

@app.route('/about')
def about():
	ice=getice()
	return render_template('about.html',title='About',ice=ice)

@app.route('/contact')
def contact():
	ice=getice()
	return render_template('contact.html',title='Contact',ice=ice)

@app.route('/disp1/<key>')
def disp1(key):
	ice=getice()
	key=int(key)
	print(ice[key])
	name=ice[key]["name"]
	image_url=ice[key]["image_url"]
	phone=ice[key]["phone"]
	website=ice[key]["url"]
	rating=ice[key]["rating"]
	address=ice[key]["location"]["address1"]
	address1=ice[key]["location"]["city"]
	address2=ice[key]["location"]["zip_code"]
	return render_template('disp1.html',title='Contact',name=name,image_url=image_url,phone=phone,website=website,rating=rating,address=address)




