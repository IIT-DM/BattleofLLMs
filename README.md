# Battle of LLM's

Welcome to ChatGPT-Crawler, a project that evaluates the responses of various language models (LLMs) including ChatGPT-4, ChatGPT, Gemini, and Mistral. This project leverages conversational QA datasets from CoQA, DialFact, FaVIQ, and CoDAH for testing these LLMs, comparing their performance, and providing insights into their capabilities.

## Table of Contents

- [Introduction](#introduction)
- [Project Purpose](#project-purpose)
- [Used Datasets](#used-datasets)
- [Upcoming Benchmarks and Releases](#upcoming-benchmarks-and-releases)
- [ChatGPT API Section](#chatgpt-api-section)
- [Gemini Section](#gemini-section)
- [Mistral Section](#mistral-section)
- [Installation Guides](#installation-guides)
- [Running Gemini LLM](#process-for-gemini-llm-running)
- [Running Mistral LLM](#process-for-mistral-llm-running)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project focuses on evaluating the responses of ChatGPT-4, ChatGPT, Gemini, and Mistral through the lens of conversational QA datasets from CoQA, DialFact, FaVIQ, and CoDAH. By comparing their performance, we aim to provide valuable insights into the strengths and weaknesses of each language model.

## Project Purpose

The primary purpose of this project is to:

- Evaluate responses of different LLMs using conversational QA datasets.
- Conduct a "Battle of LLMs" with datasets including CoQA, DialFact, FaVIQ, and CoDAH.
- Provide a platform for testing and comparing LLMs' capabilities.

## Used Datasets

| Dataset | Description                                |
|---------|--------------------------------------------|
| CoQA    | Conversational Question Answering          |
| DialFact| Dialogue-based Fact Verification           |
| FaVIQ   | Facts and Verification in Questions        |
| CoDAH   | Conversational Datasets Adversarial Hardness|

## Upcoming Benchmarks and Releases

Stay tuned for upcoming benchmarks and releases, including:

- ChatGPT API for bulk responses.
- QA Corpus Comparison.
- Golden ratio & NLI with respect to QA corpus.
- Evaluation scores.
- Preprint publication.

For more details, check out our [preprint](#) link.

## ChatGPT API Section

Our script automates the process of sending queries to ChatGPT, saving responses, and handling hourly limits per account. Refer to the installation guide [here](#) for detailed instructions on setting up your API key.

## Gemini Section

### Purpose

This section focuses on the Gemini language model.

### Installation

1. Clone the repository.
   
   ```bash
   git clone https://github.com/IIT-DM/BattleofLLMs.git
2. Navigate to the `gemini` directory in the command line.

   ```bash
   cd gemini
3. Install requirements using the command:
   
    ```bash
   pip install -r requirements.txt
4. Install `google-generativeai` using:
   
    ```bash
   pip install -q -U google-generativeai
5. Obtain your API key by clicking on the key icon [🔑](https://makersuite.google.com/app/apikey)
6. To run the python file in cmd:
   ```bash
   python <file_name.py>

## Mistral Section

### Purpose

This section focuses on the Mistral language model.

### Installation

1. Clone the repository.
   
   ```bash
   git clone https://github.com/IIT-DM/BattleofLLMs.git
2. Navigate to the `mistral` directory in the command line.

   ```bash
   cd mistral
3. Install requirements using the command:
   
    ```bash
   pip install -r requirements.txt


4. Upgrade transformers version using:
   ```bash
   pip install transformers --upgrade`
(requires version 4.36.1)

5. To run the python file in cmd:
   ```bash
   python <file_name.py>


## Usage Examples

Examples of running Python code for different levels of prompting (0-shot, N-shot, and COT) are provided in each relevant directory.

## Contributing

We welcome contributions, feedback, and ideas from the community. Feel free to raise issues, propose enhancements, or submit pull requests. Together, let's make this project even better!

## License

[Insert License Information Here]
