from typing import Dict


def correct_word(word: str, dictionary: Dict[str, str]) -> str:
    return dictionary[word] if word in dictionary.keys() else word



def main():
    content = "Hello world this is a sentence."

    words = {
        "Hello": "Helo",
        "world": "werld",
        "sentence.": "santance."
    }

    result = []
    for word in content.split(" "):
        result.append(correct_word(word, words))

    print(" ".join(result))


if __name__ == "__main__":
    main()
