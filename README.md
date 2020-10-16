# Macaddress_apiquery
A solution to query the https://macaddress.io/ MAC address lookup API over the network and fetch the desired output

Clone the repository by running
https://github.com/yaminiveepuri/Macaddress_apiquery.git

Move to docker_pythonapp directory
cd docker_pythonapp

The application is coded and compiled in python 3

To build the docker container
  docker build -t docker_pythonapp
  
To run the image
  docker run docker_pythonapp
  
The parameters are passed as Environment variables in dockerfile
  ENV api_key=at_bTYKJq4aE0mFQtEsBy9Wn9mHECU09 
  ENV mac_address=44:38:39:ff:ef:57
 Default API key and MAC address are passed here
 
 The environment variable values can be changed by changing the values in Dockerfile
 
