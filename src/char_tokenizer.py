class CharTokenizer:

    def __init__(self, text):

        chars = sorted(list(set(text)))

        self.stoi = {
            ch: i
            for i, ch in enumerate(chars)
        }

        self.itos = {
            i: ch
            for ch, i in self.stoi.items()
        }

        self.vocab_size = len(chars)

    def encode(self, text):

        return [
            self.stoi[c]
            for c in text
        ]

    def decode(self, tokens):

        return "".join(
            self.itos[t]
            for t in tokens
        )
        
if __name__ == "__main__":

    text = "hello"

    tokenizer = CharTokenizer(text)

    encoded = tokenizer.encode(text)

    print(encoded)

    decoded = tokenizer.decode(encoded)

    print(decoded)