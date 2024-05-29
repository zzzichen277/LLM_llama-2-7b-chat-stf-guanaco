import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
from huggingface_hub import snapshot_download

# 替换为自己的存储路径
model_path = "Llama-2-7b-chat-hf"

snapshot_download(
            repo_id="meta-llama/Llama-2-7b-chat-hf",
            local_dir=model_path,
            max_workers=8
        )
