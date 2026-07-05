import torch
import torch.nn as nn
import torch.nn.functional as F


class MLP(nn.Module):

    def __init__(self, embed_dim):

        super().__init__()

        self.fc = nn.Linear(
            embed_dim,
            4 * embed_dim
        )

        self.proj = nn.Linear(
            4 * embed_dim,
            embed_dim
        )

    def forward(self, x):

        x = self.fc(x)

        x = F.gelu(x)

        x = self.proj(x)

        return x


if __name__ == "__main__":

    x = torch.randn(2, 4, 8)

    mlp = MLP(8)

    out = mlp(x)

    print(out.shape)