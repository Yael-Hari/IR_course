import re
import collections
from part1_inverted_index import InvertedIndex


class BooleanRetrieval:
    """
    iran israel AND
    southwest Airlines OR Africa NOT
    Winner
    death cancer OR US NOT
    telescope space NOT hubble AND
    """

    def __init__(self):
        # self.inverted_index = InvertedIndex()
        pass

    def boolean_retrival_model(self, inverted_index: InvertedIndex, boolean_query: str):
        boolean_query = self.normalize_text(boolean_query)
        boolean_query_dict = self.translate_reverse_polish_notation_to_dict(boolean_query)

        # retrieve a set of matching documents
        word_to_posting_list = inverted_index.word_to_posting_list

        all_postings_lists = []

        # AND
        and_list = boolean_query_dict['AND']
        for and_word in and_list:
            postings_list = word_to_posting_list[and_word]
            all_postings_lists.append(postings_list)

        # OR
        or_tuples = boolean_query_dict['OR']
        for or_tuple in or_tuples:
            word1 = or_tuple[0]
            word2 = or_tuple[1]
            postings_list1 = word_to_posting_list[word1]
            postings_list2 = word_to_posting_list[word2]

            all_postings_lists.append(self.get_postings_lists_union(postings_list1, postings_list2))

        # NOT
        not_list = boolean_query_dict['NOT']
        for not_word in not_list:
            postings_list = word_to_posting_list[not_word]
            all_postings_lists.append(self.get_postings_list_complimentary(postings_list))

        # set of docs that are relevant to the need presented by the query
        docs_for_query_postings_list = self.get_postings_lists_intersection(all_postings_lists)

        return docs_for_query_postings_list

    def translate_reverse_polish_notation_to_dict(self, boolean_query: str):
        # boolean_query is an expression in reverse polish notation

        boolean_query_dict = {
            "AND": [],
            "OR": [],
            "NOT": []
        }

        # split the query
        boolean_query_list = boolean_query.split()

        # stack
        stack = []

        # iterating expression
        for element in boolean_query_list:

            if element not in ['AND', 'OR', 'NOT']:
                # element is a word
                stack.append(element)

            else:
                # element is an operator

                # adding tuples to boolean_query_dict according to the operator
                if element == 'AND':
                    # get operands:
                    operand1 = stack.pop()  # take out the last item of the stack
                    operand2 = stack.pop()
                    boolean_query_dict['AND'].append(operand1)
                    boolean_query_dict['AND'].append(operand2)

                elif element == 'OR':
                    # get operands:
                    operand1 = stack.pop()  # take out the last item of the stack
                    operand2 = stack.pop()
                    boolean_query_dict['OR'].append((operand1, operand2))

                elif element == 'NOT':
                    operand = stack.pop()
                    boolean_query_dict['NOT'].append(operand)

            if len(stack) == 1:
                and_element = stack.pop()
                boolean_query_dict['AND'].append(and_element)

            elif len(stack) > 1:
                raise Exception("this not suppose to happen!")

        return boolean_query_dict

    def normalize_text(self, text: str) -> str:
        norm_text = re.sub(r'[^\w\s]', '', text).lower()
        return norm_text

    def get_postings_lists_intersection(self, list_of_postings_list: list):
        # TODO
        #  returns a posting list!
        pass

    def get_postings_lists_union(self, postings_list1, postings_list2):
        # TODO
        #  returns a posting list!
        pass

    def get_postings_list_complimentary(self, postings_list):
        # TODO
        pass


if __name__ == '__main__':
    pass
