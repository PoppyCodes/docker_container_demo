import os
import requests

# définition de l'adresse de l'API
api_address = "fastapi"
#local
#api_address = "localhost"
# port de l'API
api_port = 8000
log_file="log_test_authent.log"

# requête authent test 1: Alice avec des droits renvoie 200 SUCCESS
r = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland'
    }
)

output = '''
============================
    Authentication test 1
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual result = {status_code}

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
if os.environ.get('LOG') == "1":
    print("je lgo")
    with open(log_file, 'a') as file:
        file.write(output)
else:
    print("je log pas")

# requête authent test 2: Bob avec des droits renvoie 200 SUCCESS
r2 = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder'
    }
)

output = '''
============================
    Authentication test 2
============================

request done at "/permissions"
| username="bob"
| password="builder"

expected result = 200
actual result = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r2.status_code

# affichage des résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
    with open(log_file, 'a') as file:
        file.write(output.format(status_code=status_code, test_status=test_status))

# requête authent test 3: user factice sans droits renvoie 403 Forbidden
r3 = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'clementine',
        'password': 'mandarine'
    }
)

output = '''
============================
    Authentication test 3
============================

request done at "/permissions"
| username="clementine"
| password="mandarine"

expected result = 403
actual result = {status_code}

==>  {test_status}

'''


# statut de la requête
status_code = r3.status_code

# affichage des résultats
if status_code == 403:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
print(output.format(status_code=status_code, test_status=test_status))

# impression dans un fichier
if os.environ.get('LOG') == "1":
    with open(log_file, 'a') as file:
        file.write(output.format(status_code=status_code, test_status=test_status))
