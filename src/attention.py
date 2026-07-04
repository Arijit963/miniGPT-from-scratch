import math
import torch
import torch.nn as nn
import torch.nn.functional as F


class CausalSelfAttention(nn.Module):
    def __init__(self, embed_dim):
        super().__init__()

        self.embed_dim = embed_dim

        self.Wq = nn.Linear(embed_dim, embed_dim, bias=False)
        self.Wk = nn.Linear(embed_dim, embed_dim, bias=False)
        self.Wv = nn.Linear(embed_dim, embed_dim, bias=False)

    def forward(self, x):

        B, T, C = x.shape

        q = self.Wq(x)
        k = self.Wk(x)
        v = self.Wv(x)

        scores = (q @ k.transpose(-2, -1)) / math.sqrt(C)

        # Causal Mask
        mask = torch.tril(
            torch.ones(T, T, device=x.device)
        )

        scores = scores.masked_fill(
            mask == 0,
            float("-inf")
        )

        att = F.softmax(scores, dim=-1)

        output = att @ v

        return output, att
    
if __name__ == "__main__":

    B = 1
    T = 4
    C = 8

    x = torch.randn(B, T, C)

    attention = CausalSelfAttention(C)

    output, att = attention(x)

    print("Attention Matrix:")
    print(att[0])