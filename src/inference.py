import torch
import pickle
import streamlit as st
from gpt import MiniGPT

@st.cache_resource
def load_model():

    ...

# =====================================================
# Load Model Once
# =====================================================

with open(
    r"data/tokenizer.pkl",
    "rb"
) as f:

    tokenizer = pickle.load(f)


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

        if ";" in generated_text:

            break

    return tokenizer.decode(
        idx[0].tolist()
    )


def extract_sql(text):

    marker = "# # # response :"

    text_lower = text.lower()

    if marker in text_lower:

        start = text_lower.find(
            marker
        )

        text = text[
            start + len(marker):
        ]

    stop_marker = "# # # instruction"

    stop = text.lower().find(
        stop_marker
    )

    if stop != -1:

        text = text[:stop]

    return text.strip()


def query_to_sql(user_query):

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

    return extract_sql(
        result
    )