## beluga_py

Command line interface and python module for the BelugaCDN API. Python2 and Python3 compatible.


### Installation

```
pip install beluga_py
```

### API Usage

```
from beluga_py.api import BelugaAPI

api = BelugaAPI(token_id=<BELUGACDN_TOKEN_ID>, token_secret=<BELUGACDN_TOKEN_SECRET>)
# or
api = BelugaAPI(username=<BELUGACDN_USERNAME>, password=<BELUGACDN_PASSWORD>)

# get a list of all site configurations
r = api.get('api/cdn/v2/sites')

# create an authentication token
r = api.post('api/token/token', json={'description': 'test from api'})

data = r.json()
```

### Command Line

```
# get a list of all site configurations
beluga --username <your username> --password <your password> --service api/cdn/v2 --path sites

# create an authentication token
beluga --username <your username> --password <your password> --method POST --service api/token --path token --body '{"description": "my new token"}'
```

Refer BelugaCDN's API documentation at https://docs.belugacdn.com/ for more information.

#### Notes

* based on [`python-beluga`](https://github.com/belugacdn/python-beluga) by Adam Jacob Muller ([@AdamJacobMuller](https://github.com/AdamJacobMuller))
