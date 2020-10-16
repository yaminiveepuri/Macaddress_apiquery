FROM python:3

ADD assignment.py /
RUN pip3 install requests
EXPOSE 8080
ENTRYPOINT [ "python", "./assignment.py"]
ENV api_key=at_bTYKJq4aE0mFQtEsBy9Wn9mHECU09 
ENV mac_address=44:38:39:ff:ef:57
