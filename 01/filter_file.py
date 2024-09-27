def filter_file(file, search_words, stop_words):

    search_words = set(word.lower() for word in search_words)
    stop_words = set(word.lower() for word in stop_words)

    if isinstance(file, str):
        with open(file, 'r', encoding='utf-8') as f:
            yield from process_file(f, search_words, stop_words)
    else:
        yield from process_file(file, search_words, stop_words)


def process_file(f, search_words, stop_words):

    for line in f:

        words = set(line.strip().lower().split())

        if words & stop_words:
            continue

        if words & search_words:
            yield line.strip()
