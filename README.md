# Blender-Node-Copilot

# SetUp
Create a python env and activate it:
```
python3 -m venv .venv
source .venv/bin/activate
```

# install dependencies

To instal packages mentioned in .toml file:
```
poetry install
```
**Generate Blender Shader and Geometry Node graphs directly from natural language.**

Blender Node-CoPilot is an open-source Blender add-on designed to dramatically accelerate your 3D modeling and animation workflow. It allows you to describe the node setup you want in plain English, instantly generating the corresponding Shader or Geometry Node graph inside Blender.

## The Problem
Blender’s Shader and Geometry Node Editors are incredibly powerful, but their complexity can create a steep learning curve and slow down the prototyping phase, even for experienced artists. Manually building or translating textual node descriptions into a functional graph is time-consuming and tedious.

## How It Works
Node-CoPilot bridges the gap between creative intent and technical implementation:

1. Natural Language Input: Simply type your desired outcome into the add-on's text field (e.g., "Create a procedural brick texture with moss on the crevices").
2. AI Compilation: An integrated language model translates your instruction into a structured node graph.
3. Instant Generation: The add-on uses Blender's API to automatically build the full node setup directly in your editor.

This process makes prototyping faster and serves as a powerful learning tool for newcomers.

## Future Development & AI Backbone
The add-on is currently being extended to offer more functionality:

- Graph Interpretation: Ask the model to explain how an existing node graph works.
- Modification Requests: Request changes to a selected node group using natural language.

To ensure the highest quality and most artist-friendly outputs, the core compiler is a fine-tuned Qwen Coder model. I am applying **Reinforcement Learning from Human Feedback (RLHF) with PPO** to align the model's outputs with the natural language and problem-solving styles of 3D artists.

## Technical Highlights
This project combines advanced LLM fine-tuning and Reinforcement Learning with practical Blender API integration, resulting in a tool that lowers the barrier to entry for new artists while providing a significant productivity boost for veterans.
