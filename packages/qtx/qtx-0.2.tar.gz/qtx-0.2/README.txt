## Quantextive AEX API Client

#### Dependencies

 - [**Requests: HTTP for Humans**](http://docs.python-requests.org/en/master/)
 	- install it using **pip** 
 	
 	  ```python
 	  pip install request
 	  ```
 - [**Pandas**](http://pandas.pydata.org/)
 	- install it using **pip** 
 	
 	  ```python
 	  pip install pandas
 	  ```

#### How to make an API request?

class `ApiClient` in [`qtx.py`](qtx.py) is provisioned to make API requests. In the constructor of the `ApiClient` class, a dictionary of default headers for all requests can be supplied so that headers need not be supplied with each request.

```python
default_headers = { 'x-api-key' : '<token>' }
client = ApiClient(default_headers)
``` 

To make a GET request, `ApiClient.get()` method is used with following params

- **`api_key`**: API key required for authenticating the requests
- **`name`**: `string` api name which will be appended to base_url
- **`params`**: `dict` of url params
 
**EXAMPLE**

```python
import qtx

api = "market-data-eod"
params = { 
    'securityId': 'NSE:NNFM',
    'startDate': '2017-02-08',
    'endDate': '2017-02-10'
}
api_key = '<token>'

client = api_client.ApiClient()
print client.get(api_key, api, params).data_frame()
```

The `get()` method returns a `Response` object from which below methods can be used to get response data as **json** or **Pandas DataFrame**.

 - `client.get(api_key, name, queryparams).json()` will return response data as **json**, and
 - `client.get(api_key, name, queryparams).data_frame()` will return response data as pandas **DataFrame**

##### Running the test script

```python
python tests/test.py
```