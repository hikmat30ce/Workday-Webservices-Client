# Workday Webservice client

This project will include clients for all the operations defined in [Workday Public Webservices (WWS)](https://community.workday.com/sites/default/files/file-hosting/productionapi/operations/index.html)

## Installation

Run following comand to install:

```
pip install wwsclient
```

## Usage

### GetWorkers

```python
from wwsclient.client import get_client
from wwsclient.service import get_method

tenant_host = 'https://wd2-impl-services1.workday.com'
tenant_id = 'tenantID'
webservice = 'Human_Resources'
version = 'v35.0'
username = 'Integration System User@tenantID'
password = 'Password'

# get client.py
client = get_client(tenant_host, tenant_id, webservice, version, username, password)
request = {
    "Request_Criteria": {
        "Transaction_Log_Criteria_Data": [{
            "Transaction_Date_Range_Data": {
                "Updated_From": "1970-01-01T00:00:00",
                "Updated_Through": "2021-03-01T14:55:00.000+05:00",
                "Effective_From": "2021-01-01T14:45:00.000+05:00",
                "Effective_Through": "2021-03-01T14:55:00.000+05:00"
            }
        },
            {
                "Transaction_Date_Range_Data": {
                    "Updated_From": "2021-01-01T14:45:00.000+05:00",
                    "Updated_Through": "2021-03-01T14:55:00.000+05:00",
                    "Effective_From": "1970-01-01T00:00:00",
                    "Effective_Through": "2021-03-01T14:55:00.000+05:00"
                }
            }
        ]
    },
    "Response_Group": {
        "Include_Reference": True,
        "Include_Personal_Information": True,
        "Include_Employment_Information": True
    }
}
xslt_code = '''<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wd="urn:com.workday/bsvc" exclude-result-prefixes="xs wd env" version="2.0"><xsl:output method="xml" indent="yes"></xsl:output><xsl:template match="env:Envelope/env:Body"><root><Total_Results><xsl:value-of select="*/wd:Response_Results/wd:Total_Results"/></Total_Results><Total_Pages><xsl:value-of select="*/wd:Response_Results/wd:Total_Pages"/></Total_Pages><Page_Results><xsl:value-of select="*/wd:Response_Results/wd:Page_Results"/></Page_Results><Page><xsl:value-of select="*/wd:Response_Results/wd:Page"/></Page><records><xsl:for-each select="*/wd:Response_Data/wd:Worker"><record><workday_id><xsl:value-of select="wd:Worker_Reference/wd:ID[@wd:type='WID']"/></workday_id><employee_id><xsl:value-of select="wd:Worker_Data/wd:Worker_ID"/></employee_id><formatted_name><xsl:value-of select="wd:Worker_Data/wd:Personal_Data/wd:Name_Data/wd:Legal_Name_Data/wd:Name_Detail_Data/@wd:Formatted_Name"/></formatted_name></record></xsl:for-each></records></root></xsl:template></xsl:stylesheet>'''
operation = "Get_Workers"
get_workers_result = get_method(client, request, xslt_code, operation, True)

```


### Create_Position

```python
from wwsclient.client import get_client
from wwsclient.service import crud_method

tenant_host = 'https://wd2-impl-services1.workday.com'
tenant_id = 'tenantID'
webservice = 'Recruiting'
version = 'v35.0'
username = 'Integration System User@tenantID'
password = 'Password'

# get client.py
client = get_client(tenant_host, tenant_id, webservice, version, username, password)
request = {
    "Business_Process_Parameters": {
        "Auto_Complete": True,
        "Run_Now": True
    },
    "Create_Position_Data": {
        "Supervisory_Organization_Reference": [{
            "ID": [{
                "type": "Organization_Reference_ID",
                "_value_1": "Human_Resources_supervisory"
            }]
        }],
        "Position_Data": {
            "Job_Posting_Title": "Technical Recruiter Python"
        },
        "Position_Group_Restrictions_Data": {
            "Availability_Date": "2019-10-20",
            "Earliest_Hire_Date": "2019-10-20"
        },
        "Edit_Assign_Organization_Sub_Process": {
            "Business_Sub_Process_Parameters": {
                "Auto_Complete": True
            },
            "Position_Organization_Assignments_Data": {
                "Company_Assignments_Reference": [{
                    "ID": [{
                        "type": "Company_Reference_ID",
                        "_value_1": "GMS_USA_company"
                    }]
                }],
                "Cost_Center_Assignments_Reference": [{
                    "ID": [{
                        "type": "Organization_Reference_ID",
                        "_value_1": "10000"
                    }]
                }],
                "Region_Assignments_Reference": [{
                    "ID": [{
                        "type": "Region_Reference_ID",
                        "_value_1": "USA_NE_Region"
                    }]
                }]
            }
        }

    }
}
operation = "Create_Position"
get_workers_result = crud_method(client, request, operation)

```
