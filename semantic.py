# code to get similarity scores between different words as measured by their vector representations
import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("Example 1:")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Comment on above: the interesting thing about the results you get is that they reflect the relative semantic
# similarity between the words. In particular, the similarity scores show that the words "cat" and "monkey" are more
# similar to each other than either word is to "banana". This is because "cat" and "monkey" are both animals, whereas
# "banana" is a fruit - a very different concept. However, the similarity between 'monkey' and 'banana' is higher than
# the similarity between 'cat' and 'banana'; presumably because there is a closer connection between monkeys and bananas
# (monkeys are said to eat bananas)


# code to undertake similarity comparison between words in string
print("\nExample 2:")
tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# Comment on above: the results from running the code above show the similarity scores between each pair of words in
# the input string "cat apple monkey banana". By computing these similarity scores, the code is able to compare the
# semantic relatedness between every pair of words in the input string. The output shows that cat and monkey are similar
# (presumably because both mammals) and banana and apple are semantically similar (both fruits). However, there is also
# a slight similarity between banana and monkey, as for the first piece of code above.


# code to change words in string to check how output might vary
print('\nExample 3:')
tokens = nlp('cat panther meat banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# Comment on above: From the output using the above string and code, we can see that "cat" and "panther" are not very
# similar to each other (score of 0.049), presumably because they are different species of felines. I found
# this surprising as thought they would be more semantically similar. If you replace 'cat' for 'lion' then the
# similarity score changes from 0.049 to 0.237. The least semantically similar words are 'banana' and 'panther' which
# makes sense as there is no obvious association between these two words.


# Changing the language model from 'en_core_web_md' to 'en_core_web_sm'
# When this change is made to the language model, the output includes the following error message:
# "UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method
# will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if
# you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use
# context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if
# available."
# What this means is that this spaCy model does not have pre-trained word vectors loaded. Word vectors are dense, low-
# dimensional representations of words that capture semantic and syntactic information about their meanings and
# relationships with other words. Without word vectors, spaCy can still perform various linguistic analyses such as
# tagging, parsing, and named entity recognition. However, the similarity between words computed by the similarity()
# method will be based solely on these linguistic features and may not be as accurate or meaningful as when word
# vectors are available. Certainly in running the code using the 'small' model, the similarity numbers appear to be
# higher % which suggests to me that there is less nuance in the analysis.
