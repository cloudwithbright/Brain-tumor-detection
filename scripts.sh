#!/bin/bash

#DEFINE VARIABLES
#FOR APPLICATION
PORT=8080
INGRESS=all
MEMORY=128Mi
RUNTIME=python38
REGION=europe-west2
PROJECT=fastbidgh-dev
IMAGE_NAME=brain-tumor
SERVICE_NAME=brain-tumor

# #BUILD, TAG AND PUSH IMAGE TO GOOGLE CONTAINER REGISTORY
echo "START BUILDING DOCKER IMAGE"
docker image build -f dockerfile -t $IMAGE_NAME .
docker image tag $IMAGE_NAME gcr.io/$PROJECT/$IMAGE_NAME
docker image push gcr.io/$PROJECT/$IMAGE_NAME
echo "AFTER IMAGE HAS BEEN PUSHED"

#DEPLOY APPLICATION FOR CLOUDRUN APP
echo "START DEPLOYING APPLICATION"
gcloud run deploy $SERVICE_NAME --image=gcr.io/$PROJECT/$IMAGE_NAME:latest --platform=managed --memory=$MEMORY \
--port=$PORT --region=$REGION --ingress=$INGRESS --allow-unauthenticated --project=$PROJECT 
echo "AFTER DEPLOYING APPLICATION"
#sudo lsof -i -P -n | grep LISTEN