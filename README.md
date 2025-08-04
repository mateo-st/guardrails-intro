# Exploring AI Guardrails

This repository documents introductory learning on **guardrails for generative AI applications**. mainly following the [Safe and Reliable AI via Guardrails](https://www.deeplearning.ai/short-courses/safe-and-reliable-ai-via-guardrails/) short course provided by [DeepLearning.AI](https://www.deeplearning.ai/). Here, you’ll find notes, code examples, and (eventually) small experiments related to safe and reliable AI practices.

## Contents

- 📝 Course notes
- 💻 Code examples
- 🧪 Experiments

## Installation

### Dependencies

This project uses [uv](https://github.com/astral-sh/uv) for Python versioning, environment and dependency management.

### Set-up

1. Clone the repository:
   ```
   git clone https://github.com/mateo-st/guardrails-intro.git
   cd guardrails-intro
   ```

2. Install dependencies and create the environment:
   ```
   uv sync
   ```

## Repo Structure

- Explore the `docs/` directory for course notes and summaries.
- Check the `examples/` directory for the course's code samples.
- Look into the `experiments/` directory for quick, small explorations on how to implement guardrails.
   - `experiments/handmade_langgraph_gr/` contains a hand-made implementation of guardrails using LangGraph.
   - `experiments/langchain_guardrailsai_gr/` integrates LangChain with GuardrailsAI for a more structured approach.

## Acknowledgments

- [Safe and Reliable AI via Guardrails – DeepLearning.AI](https://www.deeplearning.ai/short-courses/safe-and-reliable-ai-via-guardrails/)