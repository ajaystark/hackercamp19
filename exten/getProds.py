import flask, json
from Predictor import Predictor

data = [
	[
		'Bewakoof T-Shirt',
		'https://www.bewakoof.com/p/gym-karo-half-sleeve-t-shirt-for-men',
		'3/5'
	],
	[
		'SouledStore T-Shirt',
		'thesouledstore.com/product/namaste-bitches-tshirt',
		'4/5'
	],
	[
		'PopXO T-Shirt',
		'//www.popxo.com/product/adulting-t-shirt-boyfriend-fit',
		'2/5'
	],
	[
		'TMC Beard Oil',
		'//www.themancompany.com/products/almond-thyme-beard-oil?variant=20823289991',
		'2.5/5'
	],
	[
		'Beardo Oil',
		'https://www.beardo.in/oil/beardo-beard-hair-growth-oil-for-full-beard',
		'3/5'
	],
	[
		'BMC Oil',
		'https://www.amazon.in/Bombay-Shaving-Company-Beard-Growth/dp/B07H83VQ4Z ',
		'4/5'
	],
	[
		'Beardhood Oil',
		'//www.amazon.in/Beardhood-Subtle-Citrus-Beard-30ml/dp/B071VPVKG6',
		'3.5/5'
	],
	[
		'Chumbak Laptop Sleeve',
		'amazon.in/Chumbak-Made-India-Laptop-Sleeve/dp/B01LY4T4EA',
		'3/5'
	],
	[
		'DailyObj Laptop Sleeve',
		'dailyobjects.com/dailyobjects-burgundy-vegan-leather-zippered-sleeve-for-14-laptop-macbook',
		'4.5/5'
	],
	[
		'SouledStore Sleeve',
		'thesouledstore.com/product/pbl-premier-badminton-league-laptop-sleeve ',
		'2/5'
	]
]

app=Flask(__name__,static_folder='static')

p = Predictor()

@app.route('/getProds',methods=['POST','GET'])
def save():
    if request.method=='POST':
        return json.dumps(model.getPred(data))
		