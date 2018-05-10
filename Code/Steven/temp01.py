# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in range(len(test_list)):
#     print(test_list[i - 1], test_list[i])

import re
s = 'keyword: some keywords concept :some concepts'
dict(re.findall(r'(\S+)\s*:\s*(.*?)\s*(?=\S+\s*:|$)', s))

print(s)