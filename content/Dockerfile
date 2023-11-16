FROM debian:11 
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests
WORKDIR /usr/src/app
RUN mkdir logs
COPY test_content.py .
CMD python3 ./test_content.py