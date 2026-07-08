BLOCK_SIZE = 128
BATCH_SIZE = 32
TRAIN_STEPS = 4000
import torch
import torch.optim as optim
import pickle
import json
from word_tokenizer import WordTokenizer
from dataset import IoTDataset
from gpt import MiniGPT, GPTConfig


# Load dataset
with open(
    r"data/iot_queries.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

print("Dataset Length:", len(text))

# Tokenizer
tokenizer = WordTokenizer(text)

print("Vocabulary Size:", tokenizer.vocab_size)
print("Block Size:", BLOCK_SIZE)
print("Batch Size:", BATCH_SIZE)
print("Training Steps:", TRAIN_STEPS)
# Dataset
dataset = IoTDataset(
    text,
    tokenizer,
    block_size=BLOCK_SIZE
)

device = "cuda" if torch.cuda.is_available() else "cpu"

print("Using Device:", device)


# Model Config
config = GPTConfig(
    vocab_size=tokenizer.vocab_size,
    block_size=BLOCK_SIZE,
    n_layer=6,
    n_head=8,
    n_embd=256
)


# Model
model = MiniGPT(config).to(device)

print(
    "Parameters:",
    sum(
        p.numel()
        for p in model.parameters()
    )
)


# Optimizer
optimizer = optim.AdamW(
    model.parameters(),
    lr=3e-4
)
model.train()
# Training Loop
for step in range(TRAIN_STEPS):

    xb, yb = dataset.get_batch(
        batch_size=BATCH_SIZE
    )

    xb = xb.to(device)
    yb = yb.to(device)

    logits, loss = model(
        xb,
        yb
    )

    optimizer.zero_grad(set_to_none=True)

    loss.backward()
    torch.nn.utils.clip_grad_norm_(
    model.parameters(),
    1.0
    )

    optimizer.step()

    if step % 100 == 0:

        print(
            f"Step {step} | Loss {loss.item():.4f}"
        )

    # ==========================================
    # Checkpoint Saving
    # ==========================================

    if step % 500 == 0 and step > 0:

        torch.save(
        {
            "step": step,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "config": config
        },
        f"data/checkpoint_{step}.pt"
    )

        print(
            f"Checkpoint Saved: checkpoint_{step}.pt"
        )


# Save model
torch.save(
    {
        "model_state_dict": model.state_dict(),
        "config": config
    },
    r"data/model.pt"
)
with open(
    r"data/tokenizer.pkl",
    "wb"
) as f:

    pickle.dump(
        tokenizer,
        f
    )

info = {

    "vocab_size": tokenizer.vocab_size,

    "block_size": BLOCK_SIZE,

    "n_layer": 6,

    "n_head": 8,

    "n_embd": 256
}

with open(
    r"data/training_info.json",
    "w"
) as f:

    json.dump(
        info,
        f,
        indent=4
    )

print("\nTraining Complete!")
print("Model Saved")
print("Tokenizer Saved")
print("Training Info Saved")