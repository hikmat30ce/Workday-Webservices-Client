import xmltodict
from collections import OrderedDict
from io import StringIO
import json
from lxml import etree


def parse_xml_response(response):
    rsp_txt=response.text.replace("<?xml version='1.0' encoding='UTF-8'?>", '')
    rsp_txt=rsp_txt.replace('<?xml version="1.0" encoding="utf-8"?>', '')
    return etree.parse(StringIO(rsp_txt))


def transformedresponse(result, transform):
    doc = parse_xml_response(result)
    result_tree = transform(doc)
    return xmltodict.parse(result_tree)


def print_to_console_call_details(response):
    print("current_page: " + response['root']['Page'])
    print("total_pages: " + response['root']['Total_Pages'])
    print("total_results: " + response['root']['Total_Results'])


def prepare_response(transformed_response, final_response_result):
    if isinstance(transformed_response['root']['records']['record'], OrderedDict):
        final_response_result = final_response_result + json.loads(
            json.dumps([transformed_response['root']['records']['record']]))
    else:
        final_response_result = final_response_result + json.loads(
            json.dumps(transformed_response['root']['records']['record']))
    return final_response_result

