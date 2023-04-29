from part1_inverted_index import InvertedIndex


def print_statistics(inverted_index):
    word_to_frequency = dict()

    for word, posting_list in inverted_index.word_to_posting_list.items():
        word_to_frequency[word] = len(posting_list)

    words_sorted_by_freq = sorted(
        word_to_frequency, key=word_to_frequency.get, reverse=True
    )
    top = words_sorted_by_freq[:10]
    bottom = words_sorted_by_freq[-10:]

    # top_df = pd.DataFrame(data={"word": top}, index=range(1, 11))
    # bottom_df = pd.DataFrame(data={"word": bottom}, index=range(1, 11))
    #
    # for df in [top_df, bottom_df]:
    #     df["doc frequency"] = df["word"].apply(lambda w: word_to_frequency[w])
    #
    # print("Top 10 words")
    # print(top_df)
    #
    # print("---------------")
    #
    # print("Bottom 10 words")
    # print(bottom_df)

    print("---------------")
    print("Top 10 words")
    print(" ", "\t", "word", "\t", "\t", "doc frequency")
    for i, word in enumerate(top):
        print(i + 1, "\t", word, "\t", "\t", word_to_frequency[word])
    print("\n")
    print("---------------")
    print("Bottom 10 words")
    print("  ", "\t", "word", "\t", "\t", "doc frequency")
    for i, word in enumerate(bottom):
        print(i + 1, "\t", word, "\t", "\t", word_to_frequency[word])


if __name__ == "__main__":
    inverted_index = InvertedIndex()
    print_statistics(inverted_index)
