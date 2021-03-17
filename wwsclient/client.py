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


def get_raas_client(tenant_host, tenant_id, raas, raas_user, username, password):
    """
    :param tenant_host:  Tenant Host Name
    :param tenant_id: Tenant ID
    :param raas:Report as service Reference ID
    :param raas_user: The username whos has this report in ownership
    :param username: Integration username
    :param password: Integration user password
    :return: Zeep client object
    """
    if "https://" not in tenant_host:
        tenant_host = "https://" + tenant_host
    if "@" + tenant_id not in username:
        username = username + "@" + tenant_id
    # Build client url
    client_url = tenant_host + "/ccx/service/Report2/" + tenant_id + "/" + raas_user + "/" + raas + "?wsdl"

    return Client(client_url, UsernameToken(username, password))
