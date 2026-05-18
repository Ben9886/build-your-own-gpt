# build-your-own-gpt

Building a GPT from scratch — math, PyTorch, transformers — following Andrej Karpathy's free **"Neural Networks: Zero to Hero"** curriculum.

Goal: deeply understand how LLMs work, not just use them. Every video → a notebook / Python file pushed here.

## Curriculum (all free)

| # | Episode | Repo folder | Status |
|---|---|---|---|
| 1 | [micrograd — backprop from scratch](https://www.youtube.com/watch?v=VMj-3S1tku0) | `01_micrograd/` | ⬜ |
| 2 | [makemore — bigram language model](https://www.youtube.com/watch?v=PaCmpygFfXo) | `02_makemore_bigram/` | ⬜ |
| 3 | [makemore — MLP](https://www.youtube.com/watch?v=TCH_1BHY58I) | `03_makemore_mlp/` | ⬜ |
| 4 | [makemore — activations, gradients, BatchNorm](https://www.youtube.com/watch?v=P6sfmUTpUmc) | `04_makemore_batchnorm/` | ⬜ |
| 5 | [makemore — manual backprop](https://www.youtube.com/watch?v=q8SA3rM6ckI) | `05_makemore_backprop/` | ⬜ |
| 6 | [makemore — WaveNet](https://www.youtube.com/watch?v=t3YJ5hKiMQ0) | `06_makemore_wavenet/` | ⬜ |
| 7 | [**Let's build GPT — from scratch in code**](https://www.youtube.com/watch?v=kCc8FmEb1nY) | `07_gpt_from_scratch/` | ⬜ |
| 8 | [Let's build the GPT tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) | `08_gpt_tokenizer/` | ⬜ |
| 9 | Reproduce nanoGPT end-to-end | `09_nanogpt_reproduce/` | ⬜ |

Reference repo: [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) — the production-quality answer key.

## Setup

```bash
git clone https://github.com/Ben9886/build-your-own-gpt.git
cd build-your-own-gpt
python -m venv .venv && source .venv/bin/activate
pip install torch numpy matplotlib jupyter
```

## Progress

Tick the box above as each folder gains its committed code.
