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
        line_clean = line.strip().lower()

        if any(stop_word in line_clean for stop_word in stop_words):
            continue

        if any(search_word in line_clean for search_word in search_words):
            yield line.strip()
