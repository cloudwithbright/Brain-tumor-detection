#Import core tools
import numpy as np
import tensorflow as tf
from PIL import Image
import cv2

#import flask libries
from flask import Flask, render_template, request

#Initialize Flask APP
app = Flask(__name__)

#Our saved model
model = "modules/model_6.h5"

#A function to scale our image dataset to make prediction and to return the final results.
def evaluate_models(image_name, models):
  """
  So with this function, two(2) things will be done here. The
  first thing that we will do is to change the shape of our
  images to be in the same scale and then resize it. The second
  thing is to make prediction then plot plot the image(visualize it)
  by showing the name also.
  """
    
  image = cv2.imread(image_name)
  img = Image.fromarray(image)
  img=img.resize((64, 64))
  
  img=np.array(img)
  input_image = np.expand_dims(img, axis=0)
  res = models.predict(input_image)
  image_class = np.round(res[0][0])
  
  if image_class > 0.5:
    class_pred = "Tumor"
  elif image_class == 0:
    class_pred = "No tumor"
  else:
    class_pred = "Unknown"
  
  #plot image
  print(f"Print started here: {res}")
  return class_pred

#Route to display homepage
@app.route("/", methods=["GET"])
def hello_world():
    return render_template("index.html")

#Route to make prediction our custom image datasets
@app.route("/", methods=["POST"])
def predict():
  
    #Process and save image in a directory
    imagefile = request.files['imagefile']
    image_path = "./static/" + imagefile.filename
    imagefile.save(image_path)
    print(image_path)
    #Load in model and make predictions
    my_model = tf.keras.models.load_model(model)
    results = evaluate_models(image_path, my_model)
    # results="Owusu"
    return render_template("index.html", results=results, image_path=image_path)
    
if __name__ == "__main__":
    app.run(port=3000, debug=True)