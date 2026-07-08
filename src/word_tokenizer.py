import re


class WordTokenizer:

    def __init__(self, text):

        self.tokens = self.tokenize(text)

        vocab = sorted(
            list(set(self.tokens))
        )

        self.vocab = [
            "<PAD>",
            "<UNK>"
        ] + vocab

        self.stoi = {
            token: i
            for i, token in enumerate(self.vocab)
        }

        self.itos = {
            i: token
            for token, i in self.stoi.items()
        }

        self.vocab_size = len(self.vocab)

    def tokenize(self, text):

        return re.findall(
            r"\w+|[^\w\s]",
            text.lower()
        )

    def encode(self, text):

        tokens = self.tokenize(text)

        return [
        self.stoi.get(
            token,
            self.stoi["<UNK>"]
        )
        for token in tokens
]

    def decode(self, ids):

        tokens = [
        self.itos.get(
            i,
            "<UNK>"
        )
        for i in ids
        ]

        return " ".join(tokens)
    
if __name__ == "__main__":

    with open(
        r"data/iot_queries.txt",
        "r",
        encoding="utf-8"
    ) as f:

        text = f.read()

    tokenizer = WordTokenizer(text)

    print("Vocabulary Size:")
    print(tokenizer.vocab_size)

    print()

    print("First 100 Tokens:")

    print(
        tokenizer.vocab[:100]
    )
    
    print()

    test = "show co2 sensors"

    print("Unknown Word Test:")

    print(
        tokenizer.encode(test)
    )