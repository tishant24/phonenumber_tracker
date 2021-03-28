import phonenumbers
from no import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number,'CH')
print(geocoder.description_for_number(ch_number, 'en'))  

from phonenumbers import carrier
service_provider=phonenumbers.parse(number,'R0')
print(carrier.name_for_number(service_provider,'en'))

