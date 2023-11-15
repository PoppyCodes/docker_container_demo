FROM datascientest/fastapi:1.0.0
RUN apt-get update && apt-get install python3-pip -y
VOLUME ~/docker_exam:/home/my_tests
ADD $TEST_FILE /my_tests/$TEST_FILE
WORKDIR /home/my_tests
CMD touch testfile.log
CMD python3 $TEST_FILE