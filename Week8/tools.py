import re


def calculator(expression: str) -> str:
    try:
        expression = re.sub(r"[^0-9+\-*/(). ]", "", expression)
        result = eval(expression)
        return f"Answer: {result}"
    except Exception:
        return "Invalid mathematical expression."


def keyword_extractor(text: str) -> str:
    words = text.split()

    keywords = sorted(set(
        word.strip(".,!?")
        for word in words
        if len(word.strip(".,!?")) > 4
    ))

    return ", ".join(keywords)