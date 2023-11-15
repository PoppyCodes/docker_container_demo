FROM python:3.8-alpine 
WORKDIR /usr/src/app
COPY test_authent.py .
COPY requirements.txt .
RUN pip install --upgrade pip && pip install requests
#RUN pip install --no-cache-dir -r requirements.txt
CMD python3 test_authent.py
#CMD tail -F anything