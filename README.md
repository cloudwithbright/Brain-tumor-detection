# Brain-tumor-detection
A deep learning model to Detect brain tumor cloud architecture.

![production - Page 1](https://user-images.githubusercontent.com/74520811/137378929-fb5307ea-4200-4065-a564-8eb046e4118c.png)

# Scores
Six different models were built by performing different experiments. After comparing the models, the 5th model was performing well more than the other models.
**model_5**
* Loss value of **0.07**
* Accuracy score of **0.98**

# Overview
A Brain tumor is considered as one of the aggressive diseases, among children and adults. Brain tumors account for 85 to 90 percent of all primary Central Nervous System(CNS) tumors. Every year, around 11,700 people are diagnosed with a brain tumor.


The 5-year survival rate for people with a cancerous brain or CNS tumor is approximately 34 percent for men and36 percent for women. Brain Tumors are classified as: Benign Tumor, Malignant Tumor, Pituitary Tumor, etc. Proper treatment, planning, and accurate diagnostics should be implemented to improve the life expectancy of the patients. The best technique to detect brain tumors is Magnetic Resonance Imaging (MRI).

A huge amount of image data is generated through the scans. These images are examined by the radiologist. A manual examination can be error-prone due to the level of complexities involved in brain tumors and their properties.

Application of automated classification techniques using Machine Learning(ML) and Artificial Intelligence(AI)has consistently shown higher accuracy than manual classification. Hence, proposing a system performing detection and classification by using Deep Learning Algorithms using ConvolutionNeural Network (CNN), Artificial Neural Network (ANN), and TransferLearning (TL) would be helpful to doctors all around the world.


# Problem Definition
A machine learning model to help identify brain tumor. This model will be apple to predict if a person has a brain tumor and the solutions needed to be taken.

# Dataset
The dataset can be located at kaggle. Click on the link to be directed to the datasets repository. [Link to datasets](https://www.kaggle.com/ahmedhamada0/brain-tumor-detection)

# Deployment
A restfull API will be created for the model and deployed on Google Cloud taking advantage of its serverless container engine(Cloudrun) All using automation script.

* Deployment Services
  * Python(Flask)
  * Cloudrun
  * Container Registory

* Others
  * Docker
  * gcloud
  * gsutil

To deploy the application, give the scripts.sh permission using `chmod +x scripts.sh` then deploy your application by runing `./scripts.sh`.

