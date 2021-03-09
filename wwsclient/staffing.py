import datetime
import sys
import pytz
import zeep
from zeep import xsd
from util import *

import zeep.exceptions

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


# region Get Workers
def get_workers(client, request, xslt_code, print_to_console=False, count=100):
    """
    :param client: Zeep client
    :param request: request object
    :param xslt_code: xslt code as string
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
            with client.settings(raw_response=True):
                result = client.service.Get_Workers(_soapheaders=[workday_common_header],
                                                    Request_References=None if request is None or "Request_References" not in request else
                                                    request['Request_References'],
                                                    Request_Criteria=None if request is None or "Request_Criteria" not in request else
                                                    request['Request_Criteria'],
                                                    Response_Filter={
                                                        "As_Of_Effective_Date": current_date,
                                                        "As_Of_Entry_DateTime": current_date,
                                                        "Page": current_page + 1,
                                                        "Count": count
                                                    },
                                                    Response_Group=None if request is None or "Response_Group" not in request else
                                                    request['Response_Group'])

            transformed_response = transformedresponse(result, transform)
            if transformed_response['root']['Total_Results'] == '0':
                return

            total_pages = int(transformed_response['root']['Total_Pages'])
            current_page = int(transformed_response['root']['Page'])

            if print_to_console:
                print_to_console_call_details(transformed_response)
            final_response_result = prepare_response(transformed_response, final_response_result)

        except zeep.exceptions.Fault as ex:
            print("error in Get_Suppliers : " + str(ex))
            print("Unexpected error: ", sys.exc_info()[0])
            break

        except zeep.exceptions.XMLParseError as ex:
            print("xml error in Get_Suppliers : " + str(ex))
            print("Unexpected error: ", sys.exc_info()[0])
            current_page = current_page + 1

        except Exception as ex:
            print("generic error in Get_Suppliers: " + str(ex))
            print("Unexpected error: ", sys.exc_info()[0])

    return final_response_result
