#Specify base image
FROM python:3.7.3-stretch

#Create a work directory
RUN mkdir /app

#Specify port number
ENV PORT=3000

#Specify working directory
WORKDIR /app

#Copy all files to working directory
COPY . .

#Install dependencis
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

#Expose port number
EXPOSE ${PORT}

#Start the app
CMD ["python", "app.py"]