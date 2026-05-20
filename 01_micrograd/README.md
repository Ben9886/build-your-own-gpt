# Episode 1 — micrograd

Karpathy: [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) (~2h25m)

Reference: [karpathy/micrograd](https://github.com/karpathy/micrograd)

## What you'll build

A tiny autograd engine — a `Value` class that wraps a scalar, tracks its parents in a computation graph, and implements `.backward()` to compute gradients via the chain rule. Then a `Neuron` / `Layer` / `MLP` on top of it, trained with manual gradient descent.

## Files

| File | Purpose |
|---|---|
| `micrograd.ipynb` | Follow-along notebook — section headers match video chapters |
| `engine.py` | Final `Value` class (filled in as you go) |
| `nn.py` | Final `Neuron`, `Layer`, `MLP` classes |

## Workflow

1. Watch a section of the video.
2. Type (don't paste) the code into the notebook cell.
3. Run it. If it breaks, debug before moving on.
4. When the section is done, copy the final code into `engine.py` / `nn.py`.
5. Commit with a message like `01: section 5 — backward() function`.

## Setup

```bash
cd ~/Code/build-your-own-gpt
python -m venv .venv
source .venv/bin/activate
pip install torch numpy matplotlib jupyter graphviz
jupyter notebook 01_micrograd/micrograd.ipynb
```
