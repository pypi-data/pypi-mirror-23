"""HAP Constants"""

from .utils import (to_bool, to_float, to_int32, to_uint16, to_uint32,
                    to_uint64, to_uint8, to_utf8, to_uuid, parse_format)

characteristic_ID_descriptor_UUID = 'DC46F0FE-81D2-4616-B5D9-6ABDD796939A'

HAP_param_type_code_to_name = {
    1: 'Value',
    2: 'Additional_Authorization_Data',
    3: 'Origin_(local_vs_remote)',
    4: 'Characteristic_Type',
    5: 'Characteristic_Instance_ID',
    6: 'Service_Type',
    7: 'Service_Instance_ID',
    8: 'TTL',
    9: 'Return_Response',
    10: 'HAP_Characteristic_Properties_Descriptor',
    11: 'GATT_User_Description_Descriptor',
    12: 'GATT_Presentation_Format_Descriptor',
    13: 'GATT_Valid_Range',
    14: 'HAP_Step_Value_Descriptor',
    15: 'HAP_Service_Properties',
    16: 'HAP_Linked_Services',
    17: 'HAP_Valid_Values_Descriptor',
    18: 'HAP_Valid_Values_Range_Descriptor'
}

HAP_param_name_to_converter = {
    "Value": 1,
    "Additional_Authorization_Data": 2,
    "Origin_local_vs_remote": 3,
    "Characteristic_Type": to_uuid,
    "Characteristic_Instance_ID": to_uuid,
    # DC46F0FE-81D2-4616-B5D9-6ABDD796939A
    "Service_Type": to_uuid,
    "Service_Instance_ID": to_uint16,
    # E604E95D-A759-4817-87D3-AA005083A0D1
    "TTL": 8,
    "Return_Response": 9,
    "HAP_Characteristic_Properties_Descriptor": to_uint16,
    "GATT_User_Description_Descriptor": to_utf8,
    "GATT_Presentation_Format_Descriptor": parse_format,
    "GATT_Valid_Range": 13,
    "HAP_Step_Value_Descriptor": 14,
    "HAP_Service_Properties": to_uint16,
    "HAP_Linked_Services": 16,
    "HAP_Valid_Values_Descriptor": 17,
    "HAP_Valid_Values_Range_Descriptor": 18
}

format_code_to_name = {
    0x01: 'bool',
    0x04: 'unit8',
    0x06: 'unit16',
    0x08: 'uint32',
    0x0A: 'uint64',
    0x10: 'int',
    0x14: 'float',
    0x19: 'string',
    0x1B: 'data'
}

format_name_to_converter = {
    'bool': to_bool,
    'uint8': to_uint8,
    'uint16': to_uint16,
    'uint32': to_uint32,
    'uint64': to_uint64,
    'int': to_int32,
    'float': to_float,
    'string': to_utf8,
    'data': lambda x: x
}

unit_name_to_code = {
    'celsius': 0x272F,
    'arcdegrees': 0x2763,
    'percentage': 0x27AD,
    'unitless': 0x2700,
    'lux': 0x2731,
    'seconds': 0x2703
}

unit_code_to_name = {
    9984: 'unitless',
    9987: 'seconds',
    10031: 'celsius',
    10033: 'lux',
    10083: 'arcdegrees',
    10157: 'percentage'
}


class HapBleStatusCodes:
    """HAP Status code definitions and descriptions."""

    Success = 0x00
    Unsupported_PDU = 0x01
    Max_Procedures = 0x02
    Insufficient_Authorization = 0x03
    Invalid_Instance_ID = 0x04
    Insufficient_Authentication = 0x05
    Invalid_Request = 0x06


class HapBleOpCodes:
    """HAP Opcode Descriptions."""

    Characteristic_Signature_Read: int = 0x01
    Characteristic_Write: int = 0x02
    Characteristic_Read: int = 0x03
    Characteristic_Timed_Write: int = 0x04
    Characteristic_Execute_Write: int = 0x05
    Service_Signature_Read: int = 0x06


status_code_to_name = {
    0: 'Success',
    1: 'Unsupported_PDU',
    2: 'Max_Procedures',
    3: 'Insufficient Authorization',
    4: 'Invalid Instance ID',
    5: 'Insufficient Authentication',
    6: 'Invalid Request'
}

status_code_to_message = {
    0x00:
    'The request was successful.',
    0x01:
    'The request failed as the HAP PDU was not recognized or supported.',
    0x02:
    'The request failed as the accessory has reached the the limit on the '
    'simultaneous procedures it can handle.',
    0x03:
    'Characteristic requires additional authorization data.',
    0x04:
    "The HAP Request's characteristic Instance id did not match the addressed "
    "characteristic's instance id.",
    0x05:
    'Characteristic access required a secure session to be established.',
    0x06:
    'Accessory was not able to perform the requested operation.'
}
