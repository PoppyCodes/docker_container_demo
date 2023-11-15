import os
import requests

# définition de l'adresse de l'API
api_address = "fastapi"
# port de l'API
api_port = 8000
log_file="log_test_authorization.log"

# requête sentiment: user has rights on v1
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
    Authorization test 1: user has rights
============================

request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is good"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if int(os.environ.get('LOG')) == 1:
    with open(log_file, 'a') as file:
        file.write(output.format(status_code=status_code, test_status=test_status))


# requête sentiment: user bob has rights on v1
r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder',
	'sentence':'life is good'
    }
)

output = '''
============================
    Authorization test 2: user has rights
============================

request done at "/v1/sentiment"
| username="bob"
| password="builder"
| sentence="life is good"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if int(os.environ.get('LOG')) == 1:
    with open(log_file, 'a') as file:
        file.write(output.format(status_code=status_code, test_status=test_status))

# requête sentiment 3: user Alice has rights on v2
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
    Authorization test 3: user has rights on V2
============================

request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is good"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if int(os.environ.get('LOG')) == 1:
    with open(log_file), 'a') as file:
        file.write(output.format(status_code=status_code, test_status=test_status))

# requête 4: user bob has no rights on V2
r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder'
    }
)

output = '''
============================
    Authorization test 4: user has no rights
============================

request done at "/v2/sentiment"
| username="bob"
| password="builder"
| sentence="life is good"

expected result = 403
actual restult = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r.status_code

# affichage des résultats
if status_code == 403:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if int(os.environ.get('LOG')) == 1:
    with open(log_file, 'a') as file:
        file.write(output.format(status_code=status_code, test_status=test_status))
