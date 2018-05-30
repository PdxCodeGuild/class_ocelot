import string, re

# get book contents
bk_name = 'clue_golden_coin.txt'
with open(bk_name, 'r', encoding='utf-8') as bk_contents:
    bk_contents = bk_contents.read()  # read the contents

# make word list of book contents
wds_all = bk_contents.split()

# list all words ending in a period.
wds_period = []
for wd_crnt in wds_all:
    char_last = wd_crnt[-1]
    if char_last == '.':
        wds_period.append(wd_crnt)

# ...convert to dict.
wds_period_d = {}
for wd_period in wds_period:
    if wd_period not in wds_period_d:
        wds_period_d[wd_period] = 1
    else:
        wds_period_d[wd_period] += 1

# ...and convert back to list to sort by freq.
wds_per_freq = list(wds_period_d.items())
wds_per_freq.sort(key=lambda tup: tup[1], reverse=True)

# select period words NOT signifying 'end of sentence.'
# copy 'list of words ending with period' to a dict for correction.

# NOTE: GIVING UP ON ACTIVE EOS WORD SELECTION.
# eos_jud_list_d = {}
# for i_wpfrq in wds_per_freq:
#     eos_jud_list_d wds_per_freq[i_wpfrq]
#         wds_period_d[i_wpfrq] = 1
#     else:
#         wds_period_d[i_wpfrq] += 1



# for i_eos in range(len(wds_per_freq)):
#     print(f'Does {wds_per_freq[i_eos]} signify \'end of sentence?\'')
#     eos_judgement = input('y/n >')
#     if eos_jud_list[i_eos] is not eos_judgement:
#         wds_period_d[wd_period] = 1
#     else:
#         wds_period_d[wd_period] += 1



