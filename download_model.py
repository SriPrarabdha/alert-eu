# download_model.py

from huggingface_hub import snapshot_download

model_id = "cognitivecomputations/dolphin-2.9.2-qwen2-7b"
cache_dir = "/leonardo_work/EUHPC_E03_068/alert-eu/cache"

snapshot_download(
    repo_id=model_id,
    cache_dir=cache_dir,
    local_dir_use_symlinks=False  # Optional: make full copy
)
