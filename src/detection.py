from os import path, walk, listdir

from .ngram import NGram


def get_language_documents():
    directory = 'dataset'
    data = {}
    if not path.exists(path.expanduser(directory)):
        raise FileNotFoundError("({}) file not found ".format('Dataset'))
    if listdir(directory) == []:
        raise FileNotFoundError("({}) path is empty".format('Dataset'))
    else:
        try:
            for root, _, files in walk(directory):
                for file in files:
                    with open(root + '/' + file, 'r', encoding='utf-8') as f:
                        data[file.split('.')[0]] = f.read()
        except IOError:
            raise ("Could not read ({})".format(file))
    return data


def measure_distance(language_profiles, tokens):
    rank = 0
    distance = {}
    max = sum([len(v) for v in language_profiles.values()])
    for key, value in language_profiles.items():
        for token in tokens:
            if token in value:
                difference = (value.index(token) - tokens.index(token))
                if difference < 0:
                    difference = difference * -1
                rank += difference
            else:
                rank += max
        distance[key] = rank
        rank = 0
    return min(distance, key=distance.get)


def get_language_profiles():
    data = get_language_documents()
    data_to_ngram = {}
    for key, value in data.items():
        ngram = NGram(text=value).rank()
        data_to_ngram[key] = ngram
    return data_to_ngram


def get_closest_language(text):
    language_profiles = get_language_profiles()
    tokens = NGram(text=text).rank()
    closest_language = measure_distance(language_profiles=language_profiles, tokens=tokens)
    return "Closest Language: " + closest_language
