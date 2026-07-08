import torch


class IoTDataset:

    def __init__(
        self,
        data,
        tokenizer,
        block_size
    ):

        self.block_size = block_size

        self.tokenizer = tokenizer

        self.data = torch.tensor(
            tokenizer.encode(data),
            dtype=torch.long
        )

    def get_batch(
        self,
        batch_size
    ):

        ix = torch.randint(
            len(self.data) - self.block_size,
            (batch_size,)
        )

        x = torch.stack(
            [
                self.data[
                    i:i+self.block_size
                ]
                for i in ix
            ]
        )

        y = torch.stack(
            [
                self.data[
                    i+1:i+self.block_size+1
                ]
                for i in ix
            ]
        )

        return x, y
    
if __name__ == "__main__":

    text = open(
        r"data\iot_queries.txt",
        encoding="utf-8"
    ).read()

    from word_tokenizer import WordTokenizer

    tokenizer = WordTokenizer(text)

    dataset = IoTDataset(
        text,
        tokenizer,
        block_size=32
    )

    x, y = dataset.get_batch(4)

    print(x.shape)
    print(y.shape)