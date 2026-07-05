import torch
import torch.nn as nn

from multihead_attention import MultiHeadAttention
from mlp import MLP


class TransformerBlock(nn.Module):

    def __init__(
        self,
        embed_dim,
        num_heads
    ):

        super().__init__()

        self.ln1 = nn.LayerNorm(embed_dim)

        self.attn = MultiHeadAttention(
            embed_dim,
            num_heads
        )

        self.ln2 = nn.LayerNorm(embed_dim)

        self.mlp = MLP(embed_dim)

    def forward(self, x):

        x = x + self.attn(
            self.ln1(x)
        )

        x = x + self.mlp(
            self.ln2(x)
        )

        return x


if __name__ == "__main__":

    x = torch.randn(2,4,8)

    block = TransformerBlock(
        embed_dim=8,
        num_heads=2
    )

    out = block(x)

    print(out.shape)