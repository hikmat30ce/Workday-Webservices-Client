from zeep.wsse.username import UsernameToken
from zeep import Client


# region Returns workday client
# Details are provided in Credentials.py file
def get_client(tenant_host, tenant_id, webservice, webservice_version, username, password):
    """
    :param tenant_host:  Tenant Host Name
    :param tenant_id: Tenant ID
    :param webservice: Webservice name like, Human_Resources, Staffing, Resource_Management, Financial_Management etc
    :param webservice_version: Webservice Version, Currently tested with v35.0
    :param username: Integration username
    :param password: Integration user password
    :return: Zeep client object
    """
    if "https://" not in tenant_host:
        tenant_host = "https://" + tenant_host
    if "@" + tenant_id not in username:
        username = username + "@" + tenant_id
    # Build client url
    client_url = tenant_host + "/ccx/service/" + tenant_id + "/" + webservice + "/" + webservice_version + "?wsdl"
    return Client(client_url, UsernameToken(username, password))
