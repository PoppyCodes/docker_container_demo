import os
import requests
import json

# définition de l'adresse de l'API
api_address = "fastapi"
# port de l'API
api_port = 8000
log_file="./logs/log_test.log"


# requête content: sentence is positive for v1
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
	'sentence':'life is good'
    }
)

output = '''
============================
    Content test 1: sentence is positive on V1
============================

request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is good"

score={score}
expected result (score is greater than 0) = True
actual result = {is_score_positive}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code
r_dict = json.loads(r.content)

is_score_positive=r_dict["score"]>0

# affichage des résultats
if is_score_positive:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(score=r_dict["score"],is_score_positive=is_score_positive, test_status=test_status))

# impression dans un fichier
if int(os.environ.get('LOG'))==1:
    with open(log_file, 'a') as file:
        file.write(output.format(score=r_dict["score"],is_score_positive=is_score_positive, test_status=test_status))

# requête content: sentence is negative for v1
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
	'sentence':'that sucks'
    }
)

output = '''
============================
    Content test 2: sentence is negative on V1
============================

request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="that sucks"

score={score}
expected result (score is greater than 0) = False
actual result = {is_score_positive}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code
r_dict = json.loads(r.content)

is_score_positive=r_dict["score"]>0

# affichage des résultats
if is_score_positive:
    test_status = 'FAILURE'
else:
    test_status = 'SUCCESS'
print(output.format(score=r_dict["score"],is_score_positive=is_score_positive, test_status=test_status))

# impression dans un fichier
if int(os.environ.get('LOG')) == 1:
    with open(log_file, 'a') as file:
        file.write(output.format(score=r_dict["score"],is_score_positive=is_score_positive, test_status=test_status))

# requête content: sentence is positive for v2
r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
	'sentence':'life is good'
    }
)

output = '''
============================
    Content test 3: sentence is positive on V2
============================

request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is good"

score={score}
expected result (score is greater than 0) = True
actual result = {is_score_positive}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code
r_dict = json.loads(r.content)

is_score_positive=r_dict["score"]>0

# affichage des résultats
if is_score_positive:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(score=r_dict["score"],is_score_positive=is_score_positive, test_status=test_status))

# impression dans un fichier
if int(os.environ.get('LOG')) == 1:
    with open(log_file, 'a') as file:
        file.write(output.format(score=r_dict["score"],is_score_positive=is_score_positive, test_status=test_status))

# requête content: sentence is negative for v2
r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
	'sentence':'that sucks'
    }
)

output = '''
============================
    Content test 4: sentence is negative on V2
============================

request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="that sucks"

score={score}
expected result (score is greater than 0) = False
actual result = {is_score_positive}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code
r_dict = json.loads(r.content)

is_score_positive=r_dict["score"]>0

# affichage des résultats
if is_score_positive:
    test_status = 'FAILURE'
else:
    test_status = 'SUCCESS'
print(output.format(score=r_dict["score"],is_score_positive=is_score_positive, test_status=test_status))

# impression dans un fichier
if int(os.environ.get('LOG')) == 1:
    with open(log_file, 'a') as file:
        file.write(output.format(score=r_dict["score"],is_score_positive=is_score_positive, test_status=test_status))

