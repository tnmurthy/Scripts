# Install PyYaml and nltk
# pip install -U pyyaml nltk
import nltk
nltk.download()
from nltk.corpus import brown

# Test Brown Corpus:
brown.words()[0:10]
brown.tagged_words ()[0:10]
len(brown.words())
dir(brown)

# Test NLTK Book Resources:
from nltk.book import *
dir(text1)
len(text1)

# Sent Tokenize(sentence boundary detection, sentence segmentation), Word Tokenize and Pos Tagging:
from nltk import sent_tokenize, word_tokenize, pos_tag
text = "Machine learning is the science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best way to make progress towards human-level AI. In this class, you will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for yourself. More importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, you'll learn about some of Silicon Valley's best practices in innovation as it pertains to machine learning and AI."
sents = sent_tokenize(text)
sents
len(sents)
tokens = word_tokenize(text)
tokens
len(tokens)
tagged_tokens = pos_tag(tokens)
tagged_tokens

# How to use POS Tagging in NLTK
import nltk
text = "Dive into NLTK: Part-of-speech tagging and POS Tagger"
nltk.word_tokenize(text)
nltk.pos_tag(text)
nltk.help.upenn_tagset("RB")
nltk.help.upenn_tagset("NN.*")
nltk.help.upenn_tagset("NNP")

# How to train a POS Tagging Model or POS Tagger in NLTK
from nltk.corpus import treebank
len(treebank.tagged_sents())
train_data = treebank.tagged_sents()[:3000]
test_data = treebank.tagged_sents()[3000:]
train_data[0]
test_data[0]

# We use the first 3000 treebank tagged sentences as the train_data, and last 914 tagged sentences as the test_data, now we train TnT POS Tagger by the train_data and evaluate it by the test_data:
from nltk.tag import tnt
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data)
tnt_pos_tagger.evaluate(test_data)

# NOT RUN
# import pickle
# f = open('tnt_treebank_pos_tagger.pickle', 'w')
# pickle.dump(tnt_pos_tagger, f)
# f.close()

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
porter_stemmer.stem("maximum")

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
wordnet_lemmatizer.lemmatize("abaci")