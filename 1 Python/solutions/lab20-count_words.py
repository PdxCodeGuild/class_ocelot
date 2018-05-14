
import re
import random
import math

with open('the_clue_of_the_gold_coin.txt', 'r', encoding='utf-8') as f:
    contents = f.read().lower().replace('’', '')


#words = re.findall(r'\b[^A-Z\s\d]+\b', contents, re.UNICODE)
words = re.findall(r'\b[A-Za-z]+\b', contents, re.UNICODE)
print(words)


pairs = []
for i in range(len(words)-1):
    pairs.append((words[i], words[i+1]))
# lines = contents.split('\n')
# pair_frequencies = {}
# for line in lines:
#     print(line)


pair_counts = {}
for pair in pairs:
    pair_counts[pair] = pair_counts.get(pair, 0) + 1
pair_counts = list(pair_counts.items())
pair_counts.sort(key=lambda t: t[1], reverse=True)
print(pair_counts)
pair_links = {}
for pair_count in pair_counts:
    word1 = pair_count[0][0]
    word2 = pair_count[0][1]
    if word1 in pair_links:
        pair_links[word1].append(word2)
    else:
        pair_links[word1] = [word2]

print(pair_links)

def clamp(v, low, high):
    return low if v < low else high if v > high else v

# you make of volunteers and twisted and havana xiv the
# know where scattered throughout numerous locations its walls held an acknowledgment of orange juice and strained at _lost-and-found_ desk and departed vicki hello there we will pay you louise grinned i’ll let off the expression on that more in that flew to build a blanket of alarm bells just relaxing and which got its taxiing going at her prettiest smile of tiny fountain and yardarms were still looked drawn and surf cathy’s eyes dad louise john quayle’s office opened and paint buckets and cathy sighed it smells like spanish park the need help smiling to visit to death mr curtin--the man dashed against one shipped it i’ll give van walking before you ill that each date on we girls left the antique coins from gold by u.s unless i found celia trimble greeted vicki in to hers all over until by herself was taking me she dodged around mr garcia--_el duque_--is the modern firebrick fitted his car down sit down sit on quicksilver but its taxiing course i hear roy at three-seventeen vicki in large crate could help by inches from view he tapped his infectious grin if he flying down from festival souvenirs of nowhere to be stored may

word = random.choice(words)
#total = 0
for i in range(2000):
    print(word, end=' ')

    linked_words = pair_links[word]
    #k = int(random.expovariate(0.5)*len(linked_words))
    #k = (1-math.sqrt(random.uniform(0, 1)))*len(linked_words)
    k = random.expovariate(10)*len(linked_words)
    #total += k / len(linked_words)

    k = int(k)
    k = clamp(k, 0, len(linked_words)-1)
    word = linked_words[k]




    #word = random.choice(pair_links[word])


# print()
# print(f'{round(total/2000*100,2)}%')
