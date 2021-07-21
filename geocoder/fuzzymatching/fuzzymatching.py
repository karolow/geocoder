import fuzzyset


def build_fuzzyset(collection: dict):
    """Prepare a fuzzy set based on provided mapping"""
    keys = {x for x in collection.keys()}
    return fuzzyset.FuzzySet(keys, use_levenshtein=False)


def find_match(phrase: str, fuzzy_set, return_top_match=True):
    """Find match(es) between the search phrase and provided set of values"""
    if return_top_match:
        _, output = fuzzy_set.get(phrase)[0]
        return output
    return fuzzy_set.get(phrase)
