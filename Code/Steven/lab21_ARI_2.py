import string, re

# get book contents
bk_name = 'clue_golden_coin.txt'
with open(bk_name, 'r', encoding='utf-8') as bk_contents:
    bk_contents = bk_contents.read()  # read the contents

# make word list of book contents
wds_all = bk_contents.split()

# list all words ending in a period.
wds_period = []
# wds_period_len = int(len(wds_all))
for word in range(wds_period_len):
    char_last = word[-1]
    if char_last == '.':
        # print(wds_all[int(j)])
        eos_str = wds_period[word - 1] + ' ' + wds_period[word]
        # eos_str = wds_period[word - 1] + ' ' + wds_period[word]
        wds_period.append(eos_str)


# ...convert to dict.
wds_period_d = {}
for wd_period in wds_period:
    if wd_period not in wds_period_d:
        wds_period_d[wd_period] = 1
    else:
        wds_period_d[wd_period] += 1

wds_period_len

# ...and convert back to list to sort by freq.
# wds_per_freq = list(wds_period_d.items())
# wds_per_freq.sort(key=lambda tup: tup[1], reverse=True)



# for i in range(int(len(wds_per_freq))):
#     print(wds_per_freq[i])





