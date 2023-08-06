# python-cip

A very simple python interface to Canto Cumulus CIP

Wraps [requests](http://python-requests.org) to call CIP endpoints in a session


## API

### class cip.CIP

> CIP(url, serveraddress, user=None, password=None)

#### Methods:


** login(user = None, password=None, catalogname=None) **

Open a session on CIP. Returns reply from server.


** do(api, rawdata=False, ...) **

Call a `api` CIP endpoint. Returns reply from server.
If `rawdata` is False, reply is parsed JSON.

Any extra arguments are passed to request post call


** request(api, ...) **

Do a POST request to `api` CIP endpoint. Returns
[request Response object](http://docs.python-requests.org/en/master/api/#requests.Response)

Any extra arguments are passed to request post call


** logout(self) **

Close CIP session. Returns nothing


### class cip.CIPException(Exception)


## Example

```python
from cip import CIP

self.cip = CIP("http://localhost:8080/CIP/", "localhost")
self.cip.login('user', 'password', 'Sample Catalog')

r = self.cip.do("metadata/search/Sample Catalog", data={
     'querystring': '"Asset Name" contains "photo"',
     'field': ["ID", "Asset Name", "Asset Modification Date"],
})

print( r['items'][0]['Asset Modification Date'] )

```


## Test

```bash
$ pip install tox
$ tox
```


