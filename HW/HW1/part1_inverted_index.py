import collections
import os
import re


FILES_DIRECTORY_NAME = "/data/HW1/AP_Coll_Parsed"
START_DOC_TOKEN = "<DOC>"
START_TEXT_TOKEN = "<TEXT>"
END_TEXT_TOKEN = "</TEXT>"


class InvertedIndex:
    def __init__(self):
        self.word_to_posting_list = dict()
        self.internal_idx_to_original_idx = dict()

        self.index_files()

    def index_files(self):
        curr_doc_internal_idx = 1

        for root, dirs, files in os.walk(FILES_DIRECTORY_NAME):  # directory of files -> files
            for name in files:
                print(name)
                file = open(os.path.join(root, name), "r").read()
                docs = file.split(START_DOC_TOKEN)[1:]  # file -> docs
                for doc in docs:
                    self.add_to_idx_dict(doc, curr_doc_internal_idx)
                    self.index_doc(doc, curr_doc_internal_idx)
                    curr_doc_internal_idx += 1

    def add_to_idx_dict(self, doc, doc_internal_idx):
        doc_original_idx = re.findall("<DOCNO>.*</DOCNO>", doc)[0][8:21]
        self.internal_idx_to_original_idx[doc_internal_idx] = doc_original_idx

    def index_doc(self, doc, doc_internal_idx):
        texts = doc.replace("\n", " ").split(START_TEXT_TOKEN)[1:]  # doc -> texts
        for text in texts:
            text = text.split(END_TEXT_TOKEN)[0]
            words = text.split()  # text -> words
            for word in words:
                # NOTE: no need for preprocess because it is already
                # lower cased and without punctuation

                if word not in self.word_to_posting_list.keys():
                    self.word_to_posting_list[
                        word
                    ] = collections.deque()  # create new linked list
                    self.word_to_posting_list[word].append(doc_internal_idx)
                else:
                    if doc_internal_idx not in self.word_to_posting_list[word]:
                        self.word_to_posting_list[word].append(doc_internal_idx)


if __name__ == "__main__":
    pass
