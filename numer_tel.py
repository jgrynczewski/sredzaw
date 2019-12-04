import collections

TelNumber = collections.namedtuple('TelNumber', 'area_code delimiter number')
tel1 = TelNumber(area_code='+48', delimiter='-', number='123456789')
print (f'tel: {tel1.area_code}{tel1.delimiter}{tel1.number}')