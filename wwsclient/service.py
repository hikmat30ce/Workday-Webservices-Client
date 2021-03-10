import datetime
import sys
import pytz
import zeep
from zeep import xsd
from wwsclient.util import *
import zeep.exceptions

"""
__author__      = Hikmat Ullah
__copyright__   = Copyright 2021
__date__        = 18, January 2021
"""

header = xsd.Element(
    '{urn:com.workday/bsvc}Workday_Common_Header',
    xsd.ComplexType([
        xsd.Element(
            '{urn:com.workday/bsvc}Include_Reference_Descriptors_In_Response',
            xsd.Boolean()),
    ])
)
workday_common_header = header(Include_Reference_Descriptors_In_Response=True)
current_date = datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y-%m-%dT%H:%M:%S") + "-08:00"


# region Get Operation
def get_method(client, request, xslt_code, operation, print_to_console=False, count=100):
    """
    :param client: Zeep client
    :param request: request object
    :param xslt_code: xslt code as string
    :param operation: Webservice Operation
    :param print_to_console: print page numbers fetched in console
    :param count: count returned per page
    :return: All suppliers returned from api
    """
    transform = etree.XSLT(etree.XML(xslt_code))
    total_pages = 1
    current_page = 0
    final_response_result = []

    while current_page < total_pages:
        try:
            request['_soapheaders'] = [workday_common_header]
            request['Response_Filter'] = {
                "As_Of_Effective_Date": current_date,
                "As_Of_Entry_DateTime": current_date,
                "Page": current_page + 1,
                "Count": count
            }

            with client.settings(raw_response=True):
                result = client.service[operation](**request)

            if result.status_code == 200:
                transformed_response = transformedresponse(result, transform)
                if transformed_response['root']['Total_Results'] == '0':
                    print("No data returned by the API!")
                    return

                total_pages = int(transformed_response['root']['Total_Pages'])
                current_page = int(transformed_response['root']['Page'])

                if print_to_console:
                    print_to_console_call_details(transformed_response)
                final_response_result = prepare_response(transformed_response, final_response_result)
            elif result.status_code == 500:
                print(result.text)
                return

        except zeep.exceptions.Fault as ex:
            print("error in " + operation + " : " + str(ex))
            print("Unexpected error: ", sys.exc_info()[0])
            break

        except zeep.exceptions.XMLParseError as ex:
            print("xml error in " + operation + " : " + str(ex))
            print("Unexpected error: ", sys.exc_info()[0])
            current_page = current_page + 1

        except Exception as ex:
            print("generic error in " + operation + " : " + str(ex))
            print("Unexpected error: ", sys.exc_info()[0])
            break

    return final_response_result


# endregion

# region Edit, Delete, Submit, Import, ADD, PUT methods
def crud_method(client, request, operation):
    request['_soapheaders'] = [workday_common_header]
    return client.service[operation](**request)
# endregion
