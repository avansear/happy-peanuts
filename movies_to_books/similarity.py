from rapidfuzz import fuzz

def calculate_similarity(title1, title2):
    """
    Desc: Uses rapidfuzz to calculate a similarity score between two strings. We're doing this to filter and narrow down search results so we can choose the most matching one.
    """

    ratio = fuzz.partial_ratio(title1, title2)
    return ratio