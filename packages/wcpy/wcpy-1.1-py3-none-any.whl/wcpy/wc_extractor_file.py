
import nltk
from nltk.tokenize import word_tokenize
import os
import wcpy

# Add the nltk_data files to the projects
file_path = os.path.dirname(wcpy.__file__)
nltk_data_path = os.path.join(file_path, 'nltk_data')
nltk.data.path.append(nltk_data_path)

class PathNotValidException(Exception):
    """
    Thrown when a path provided does not exist or is not valid
    """
    def __init__(self, path):
        Exception.__init__(self, "Path provided is not valid: " + str(path))

class WCExtractorFile:
    """
    The extractor file class is the core of the processing. It extracts the contents
    of the files themselves, counts the words and adds them to a WC dictionary object.

    Args:
        file_path (str): The file path to extract the words from
        file_opener (func): A function that it will use to open files, passed for dependency injection
        filter_words (list): A set of words to filter on
    """

    def __init__(self, file_path, file_opener=open, filter_words=[]):
        self._file_path = file_path
        self._file_opener = file_opener
        self._filter_words = set(filter_words)

    def extract_wc_from_file(self, d_words={}):
        """
        This is the main public function, which extracts all the contents of
        a file, counts the number of occurences and updates the dictionary object

        Args:
            d_words (dict): An object to add the words, sentences and docs to

        Returns
            d_words(dict:parameter): The return is given through this parameter passed by reference
        """

        with self._file_opener(self._file_path) as file:

            for line in file:
                already_added_words = set()
                words = self._split_line(line)

                for word in words:

                    add_sentence = True

                    if word not in already_added_words:
                        already_added_words.add(word)
                    else:
                        add_sentence = False

                    self._add_word(word, line, d_words, add_sentence=add_sentence)


    def _split_line(self, line):
        """
        This function uses the NLTK library to remove characters
        and split words intelligently.

        The sentences that are repeated more than once in a document are not
        added again.

        Args:
            line (str): The line to split

        Returns:
            processed_words: A list of words without containing individual symbols
        """

        words_with_symbols = word_tokenize(line)
        words = [ w.lower() for w in words_with_symbols if any(char.isalpha() or char.isdigit() for char in w) ]

        if len(self._filter_words) > 0:
            words = [w for w in words if w in self._filter_words]

        processed_words = [ w.lower() for w in words if w not in '-' ]

        return processed_words


    def _add_word(self, word, line, d_words={}, add_sentence=True):
        """
            This function adds a word and increases its occurence, sentence and document to the
            dictionary, and handles all the necessary cases to create new objects

            Args:
                word (str): The new word to add and count
                line (str): The line where the word occurs
                d_words (dict): The WC dictionary to add he word to
                add_sentence (bool): A boolean that states if the sentence is added or not
        """
        if word not in d_words:
             d_words[word] = {
                "word_count": 0,
                "files": {
                    self._file_path: []
                }
            }

        d_words[word]["word_count"] += 1

        dw_f = d_words[word]["files"]

        if self._file_path not in dw_f:
            dw_f[self._file_path] = []

        if add_sentence:
            dw_f[self._file_path].append(line)


