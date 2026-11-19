"""
Download PayPredictor.pkl from Hugging Face Hub.
JobPredictor.pkl is already included in the GitHub repo.

"""

# === Importing Libraries ==============================

import os
from huggingface_hub import hf_hub_download


# === Configuration ==============================

REPO_ID = "Yash-Codezz/Student.Placement.Model"
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))


# === Download ==============================

print("Downloading PayPredictor.pkl from Hugging Face Hub...")
hf_hub_download(
    repo_id=REPO_ID,
    filename="PayPredictor.pkl",
    local_dir=MODEL_DIR,
)
print(f"✅ PayPredictor.pkl downloaded successfully to {MODEL_DIR}")
