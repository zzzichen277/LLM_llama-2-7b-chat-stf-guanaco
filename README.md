# LLM_SFT

## 项目介绍

基于 Llama-2-7B-Chat 模型 + 4bit量化 + QLoRA微调 +guanaco-llama2-1k数据 -> llama-2-7b-chat-guanaco模型


+ SFT训练环境：单卡A100-40G/PyTorch2.0.1/Python 3.10/ubuntu 22.04/cuda 12.1.1

- 依赖库版本： transformers==4.31.0 /bitsandbytes==0.40.0.post4

- SFT模型：Llama-2-7B-Chat hflink：https://huggingface.co/meta-llama/Llama-2-7b-chat-hf

- SFT数据: guanaco-llama2-1k hflink：https://huggingface.co/datasets/mlabonne/guanaco-llama2-1k



## 目录结构
![1716970796653](https://github.com/zzzichen277/LLM_SFT/assets/47549017/2cdcc41d-1239-4a9b-bf9b-1fa9d2438104)



## 参考链接
1.https://mp.weixin.qq.com/s/F60XYsT1dwUBmXN6r2G0eA
