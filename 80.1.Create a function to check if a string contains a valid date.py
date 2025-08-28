import re
def is_valid_date(date_string):
    pattern = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$'
    return bool(re.match(pattern, date_string))
date_string = "08-01-2025"
print(is_valid_date(date_string))
date_string = "08-1-2025"
print(is_valid_date(date_string))