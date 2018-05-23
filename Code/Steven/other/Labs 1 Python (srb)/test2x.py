import itertools, collections

tweets = ['I went to work but got delayed at other work and got stuck in a traffic and I went to drink some coffee but got no money and asked for money from work', 'We went to get our car but the car was not ready. We tried to expedite our car but were told it is not ready']

words = set(word.lower() for tweet in tweets for word in tweet.split())
_pairs = list(itertools.permutations(words, 2))
# We need to clean up similar pairs: sort words in each pair and then convert
# them to tuple so we can convert whole list into set.
pairs = set(map(tuple, map(sorted, _pairs)))

c = collections.Counter()

for tweet in tweets:
    for pair in pairs:
        if pair[0] in tweet and pair[1] in tweet:
            c.update({pair: 1})

print c.most_common(10)


