# HTTP Status Constants

A set of constants for HTTP statuses and headers. Improve your code readability.

## Installation

You can install Http Constants from [PyPI](https://pypi.org/project/http-constants/):

    pip install http-status

The library is supported on Python 3.7+.

## Usage

### Headers
```
from http_constants.headers import HttpHeaders
HttpHeaders.ACCEPT
> 'Accept'

HttpHeaders.CONTENT_TYPE_VALUES.json
> 'application/json'
```

### Statuses
```
In[1]: 
    from http_constants import status
    status.SERVICE_UNAVAILABLE
Out[1]:
    503
---
In[2]: 
    from http_constants.status import HttpStatus
    HttpStatus(500).get_meaning()

Out[2]: 
    'Internal Server Error'
```