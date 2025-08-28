import re
def is_valid_hexadecimal(s):
    hex_pattern = r'^(0x|0X)?[0-9a-fA-F]+$'
    return bool(re.match(hex_pattern, s))
hex_string = "0x1A3F"
print(f"Is '{hex_string}' a valid hexadecimal number? {is_valid_hexadecimal(hex_string)}")