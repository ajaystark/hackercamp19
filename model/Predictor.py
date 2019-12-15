import random, os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf, tensorflow.keras as keras
# from train import xTrain, yTrain

class Predictor:
	companies = 20
	features = 6
	trainEpochs = 5000	
	savePath = os.path.join(os.getcwd(), 'checkpoints', 'cp.ckpt')
	shouldSave = True
	
	def __init__(self):
		self.model = keras.models.Sequential([
			keras.layers.Dense(200, input_shape=(Predictor.features,)),
			keras.layers.Dropout(0.3),
			keras.layers.Dense(100, activation='sigmoid'),	
			keras.layers.Dropout(0.3),
			keras.layers.Dense(60, activation='sigmoid'),
			keras.layers.Dropout(0.3),
			keras.layers.Dense(Predictor.companies, activation='sigmoid')
		])
		self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
	
		# try:	
		self.model.load_weights(Predictor.savePath)
		# except:
		# 	print('Untrained model! Proceed with caution!')

	def _train(self, features, companies):
		assert len(features[0]) == Predictor.features, 'Can only train data with '+str(Predictor.features)+' features!'
		assert len(companies[0]) == Predictor.companies, 'Can only train data with '+str(Predictor.features)+' companies!'
		
		self.model.fit(x = features, y = companies, epochs = Predictor.trainEpochs, verbose=2, use_multiprocessing=True)	 
		if Predictor.shouldSave:
			self.model.save_weights(Predictor.savePath)
	
	def	getPrediction(self, features):
		assert len(features) == Predictor.features, 'Can only predict on data with '+str(Predictor.features)+' features!'
		y = self.model.predict([features])[0]
		return list(y)

	def getCompany(self, features):
		pred = list(self.getPrediction(features))
		return pred

	def formatY(self, yIn):
		y = []
		for i in range(len(yIn)):
			y1 = []
			for j in range(Predictor.companies):
				y1.append(0)
			
			y1[yIn[i]] = 1
			y.append(y1)

		return y

