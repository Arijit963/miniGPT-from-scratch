from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F
from transformer_block import TransformerBlock

@dataclass
class GPTConfig:

    vocab_size: int

    block_size: int

    n_layer: int = 4

    n_head: int = 4

    n_embd: int = 128
    
class MiniGPT(nn.Module):

    def __init__(self, config):

        super().__init__()

        self.config = config

        self.wte = nn.Embedding(
            config.vocab_size,
            config.n_embd
        )

        self.wpe = nn.Embedding(
            config.block_size,
            config.n_embd
        )

        self.blocks = nn.ModuleList(
            [
                TransformerBlock(
                    config.n_embd,
                    config.n_head
                )
                for _ in range(config.n_layer)
            ]
        )

        self.ln_f = nn.LayerNorm(
            config.n_embd
        )

        self.lm_head = nn.Linear(
            config.n_embd,
            config.vocab_size
        )
        
    def forward(self, idx, targets=None):
        B, T = idx.shape
        pos = torch.arange(
        T,
        device=idx.device
        ).unsqueeze(0)
        x = (
        self.wte(idx)
        +
        self.wpe(pos)
        )
        for block in self.blocks:
            x = block(x)

        x = self.ln_f(x)

        logits = self.lm_head(x)

        loss = None

        if targets is not None:

            loss = F.cross_entropy(
                logits.view(-1, logits.size(-1)),
                targets.view(-1)
            )

        return logits, loss

if __name__ == "__main__":

    cfg = GPTConfig(
        vocab_size=100,
        block_size=32
    )

    model = MiniGPT(cfg)

    idx = torch.randint(
        0,
        100,
        (2, 16)
    )

    targets = torch.randint(
        0,
        100,
        (2, 16)
    )

    logits, loss = model(
        idx,
        targets
    )

    print("Logits Shape:", logits.shape)
    print("Loss:", loss.item())