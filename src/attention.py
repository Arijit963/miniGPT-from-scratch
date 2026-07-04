import math
import torch
import torch.nn as nn
import torch.nn.functional as F


class SelfAttention(nn.Module):
    def __init__(self, embed_dim):
        super().__init__()

        self.embed_dim = embed_dim

        # Learnable projection matrices
        self.Wq = nn.Linear(embed_dim, embed_dim, bias=False)
        self.Wk = nn.Linear(embed_dim, embed_dim, bias=False)
        self.Wv = nn.Linear(embed_dim, embed_dim, bias=False)

    def forward(self, x):
        """
        x shape = (B, T, C)

        B = Batch Size
        T = Sequence Length
        C = Embedding Dimension
        """

        B, T, C = x.shape

        # Step 1: Generating Q, K, V
        q = self.Wq(x)
        k = self.Wk(x)
        v = self.Wv(x)

        # Step 2: Computing Attention Scores
        scores = q @ k.transpose(-2, -1)

        # Step 3: Scale
        scores = scores / math.sqrt(C)

        # Step 4: Softmax
        att = F.softmax(scores, dim=-1)

        # Step 5: Weighted Sum of Values
        output = att @ v

        return output, att


if __name__ == "__main__":

    B = 1
    T = 4
    C = 8

    x = torch.randn(B, T, C)

    attention = SelfAttention(C)

    output, att = attention(x)

    print("Input Shape :", x.shape)
    print("Output Shape:", output.shape)
    print("Attention Shape:", att.shape)

    print("\nAttention Matrix:")
    print(att[0])