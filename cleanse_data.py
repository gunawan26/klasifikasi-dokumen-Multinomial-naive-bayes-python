import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


class TrainingData:

    nama = []
    factory = StemmerFactory()
    factory_remove_word = StopWordRemoverFactory()
    stemmer = factory.create_stemmer()
    stopword = factory_remove_word.create_stop_word_remover()

    def read_file_data(url_args):
        # file = textract.process(Uri,method="tesseract")
        file = open(url_args, 'rb')

        return file


    def clean_words(words_args,stemmer=stemmer, stopword_args = stopword):

        clean_words = re.sub("[(){}<>\",\-*0-9;']", " ", words_args)
        stemmed_word = stemmer.stem(clean_words)
        output = stopword_args.remove(stemmed_word)

        return output

