# Workday Webservice client

This project will inclide clients for all the operations defined

## Installation

Run following comand to install:

```
pip install wd-services
```

## Usage

```python
from human_resource import *

# get client
client = get_client(tenant_host, tenant_id, webservice, version, username, password)
request = {
    "Request_References": {
        "Worker_Reference": [{
            "ID": {
                "type": "Employee_ID",
                "_value_1": "12345678"
            }
        }]
    },
    "Response_Group": {
        "Include_Reference": True,
        "Include_Personal_Information": True,
        "Include_Employment_Information": True
    }
}
xslt_code = '''your xslt 1.0 code'''
get_workers_result = get_workers(client, request, xslt_code)

```

##Developing Workday webservice client

```commandline
pip install -e .[dev]
```