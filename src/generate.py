import torch
import pickle

from gpt import MiniGPT


# =====================================================
# Load Tokenizer
# =====================================================

with open(
    r"data/tokenizer.pkl",
    "rb"
) as f:

    tokenizer = pickle.load(f)


# =====================================================
# Load Checkpoint
# =====================================================

checkpoint = torch.load(
    r"data/model.pt",
    map_location="cpu",
    weights_only=False
)

config = checkpoint["config"]

model = MiniGPT(config)

model.load_state_dict(
    checkpoint["model_state_dict"]
)

model.eval()


# =====================================================
# Generate
# =====================================================

def generate(
    prompt,
    max_new_tokens=100
):

    tokens = tokenizer.encode(
        prompt
    )

    idx = torch.tensor(
        [tokens],
        dtype=torch.long
    )

    for _ in range(max_new_tokens):

        idx_cond = idx[
            :,
            -config.block_size:
        ]

        with torch.no_grad():

            logits, _ = model(
                idx_cond
            )

        logits = logits[:, -1, :]

        probs = torch.softmax(
            logits,
            dim=-1
        )

        # Greedy Decoding
        next_token = torch.argmax(
            probs,
            dim=-1,
            keepdim=True
        )

        idx = torch.cat(
            [idx, next_token],
            dim=1
        )

        generated_text = tokenizer.decode(
            idx[0].tolist()
        )

        # Stop when SQL statement is complete
        if ";" in generated_text:

            break

    return tokenizer.decode(
        idx[0].tolist()
    )

# =====================================================
# Main
# =====================================================

if __name__ == "__main__":

    user_query = input(
        "Prompt: "
    )

    prompt = f"""
### Instruction:
Convert the following IoT query into SQL.

### Input:
{user_query}

### Response:
"""

    result = generate(
        prompt
    )

    result_lower = result.lower()

    # Extract only the SQL response section
    marker = "# # # response :"

    if marker in result_lower:

        start = result_lower.find(marker)

        result = result[
            start + len(marker):
        ]

    # Remove the next instruction if generated
    stop_marker = "# # # instruction"

    stop = result.lower().find(
        stop_marker
    )

    if stop != -1:

        result = result[:stop]

    print("\nGenerated SQL:\n")

    print(
        result.strip()
    )