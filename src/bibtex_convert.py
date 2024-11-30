from util import T


def to_bibtex(items: list[T]) -> str:
    bibtex_strings = [str(x) for x in items]
    return "\n\n".join(bibtex_strings)
