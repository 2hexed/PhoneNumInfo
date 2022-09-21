import sys;import phonenumbers;from phonenumbers.phonenumberutil import NumberParseException;from phonenumbers import timezone;from phonenumbers.geocoder import *;from phonenumbers.carrier import *;initialPhone='';
for i, arg in enumerate(sys.argv):
    if i>=1:initialPhone+=sys.argv[i]
if initialPhone=='':print("\033[0;31m[ ? ] Specify a number.\n( eg. `python3 main.py +44 1632 960005` )\033[0m");exit()
if not initialPhone.startswith("+"):print("\033[0;31m[ ? ] Specified number must start with a dialing code. ( eg. +44 )\033[0m");exit()
try: parsedPhone = phonenumbers.parse(initialPhone)
except NumberParseException:print("\033[0;31m[ ? ] Specified number was invalid.\033[0m");exit()
print(f"""
    \033[0;34m➤ Basic\033[0m:
        \033[0;32m➜ Parsed Information:\t\t\t{parsedPhone}\033[0m
    \n
    \033[0;34m➤ Phone\033[0m:
        \033[0;32m➜ Format ( NATIONAL ):\t\t\t{phonenumbers.format_number(parsedPhone, phonenumbers.PhoneNumberFormat.NATIONAL)}\033[0m
        \033[0;32m➜ Format ( INTERNATIONAL ):\t\t{phonenumbers.format_number(parsedPhone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}\033[0m
        \033[0;32m➜ Possible:\t\t\t\t{phonenumbers.is_possible_number(parsedPhone)}\033[0m
        \033[0;32m➜ Valid:\t\t\t\t{phonenumbers.is_valid_number(parsedPhone)}\033[0m
    \n
    \033[0;34m➤ Carrier\033[0m:
        \033[0;32m➜ Name:\t\t\t\t\t{name_for_valid_number(parsedPhone, "en")}\033[0m
    \n
    \033[0;34m➤ Geo-details\033[0m:
        \033[0;32m➜ Country:\t\t\t\t{country_name_for_number(parsedPhone, "en")}\033[0m
        \033[0;32m➜ Time-Zones:\t\t\t\t{timezone.time_zones_for_geographical_number(parsedPhone)}\033[0m
    """)