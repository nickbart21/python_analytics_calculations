from collections import Counter

string = "I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation. Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity. But one hundred years later, the Negro still is not free. One hundred years later, the life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination. One hundred years later, the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity. One hundred years later, the Negro is still languishing in the corners of American society and finds himself an exile in his own land. So we have come here today to dramatize a shameful condition."
words = string.split(' ')
print(words)

# unique words
num_unique = len(set(words))
print(f"\nThe number of unique words is: {num_unique} out of a total of {len(words)} words.")

# word frequencies
word_frequencies = Counter(words).most_common() #returns a list of tuples
for x, y in word_frequencies:
    print(f"{x} : {y}")
print("The word 'the' occurs the most at 14 times.\n")

# frequency of all words that start with 't'
t_words = string.count(' t')
print(f"The number of words that start with the letter 't' is: {t_words}")