# Stanford Text Analysis Tools in Python
import nltk
nltk.__version__

#sudo apt-get install default-jre

from nltk.stem.api import StemmerI
from nltk.stem.regexp import RegexpStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.isri import ISRIStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.rslp import RSLPStemmer

if __name__ == "__main__":
    import doctest
    doctest.testmod (optionflags=doctest.NORMALIZE_WHITESPACE)
    wordnet_lemmatizer.lemmatize ("churches")