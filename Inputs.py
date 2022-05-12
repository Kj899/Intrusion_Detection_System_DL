#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This function is to maintain the name of the label at a single place
def getLabelName():
	return 'attack_type'

def getPathToTrainingAndTestingDataSets():
	trainingFileNameWithAbsolutePath = "K:\\Final_Year_Project\\NetworkIntrusionDetection\Datasets\\NSL-KDD\\KDDTrain+_20Percent.csv"
	testingFileNameWithAbsolutePath = "K:\\Final_Year_Project\\NetworkIntrusionDetection\\Datasets\\NSL-KDD\\KDDTest-21.csv"
	return trainingFileNameWithAbsolutePath, testingFileNameWithAbsolutePath
	
def modelPerformanceReport():
	modelPerformanceReport = 'K:\\\Final_Year_Project\\NetworkIntrusionDetection\ModelsPerformance031442020.1.xlsx'
	return modelPerformanceReport

def getPathToGenerateModels():
	generatedModelsPath = 'K:\\Final_Year_Project\\NetworkIntrusionDetection\\'
	return generatedModelsPath

### Models with the below configuration will be generated
def defineArrayOfModels():
	arrayOfModels = [
		[	
			"FeatureSelectionTechnique", 
			"FeatureEncodingTechnique", 
			"FeatureNormalizationTechnique", 
			"ClassificationTechnique", 
			"TrainAccuraccy", 
			"TestAccuraccy", 
			"ModelName", 
			"ModelFileName"
		],
		[
			"ExtraTreesClassifier",
			"OneHotEncoder",
			"Standardization",
			"DecisonTree"
		],
		[
			"ExtraTreesClassifier",
			"OneHotEncoder",
			"Standardization",
			"RandomForestClassifier"
		],
		[
			"ExtraTreesClassifier",
			"OneHotEncoder",
			"Standardization",
			"ExtraTreesClassifier"
		],
		[
			"ExtraTreesClassifier",
			"OneHotEncoder",
			"Standardization",
			"KNN"
		] 
	]
	print(arrayOfModels)
	return arrayOfModels

def defineArrayForPreProcessing():
	arrayOfModels = [
		[
			"ExtraTreesClassifier",
			"OneHotEncoder",
			"Standardization",
		]
	]
	print(arrayOfModels)
	return arrayOfModels


# In[ ]:




