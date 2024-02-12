# Battle of LLMs

Welcome to Battle of LLMs, a project that evaluates the responses of various language models (LLMs) including ChatGPT-4, ChatGPT, Gemini, and Mistral. This project leverages conversational QA datasets from CoQA, DialFact, FaVIQ, and CoDAH for testing these LLMs, comparing their performance, and providing insights into their capabilities.

## Table of Contents

- [Introduction](#introduction)
- [Project Purpose](#project-purpose)
- [Used Datasets](#used-datasets)
- [ChatGPT](#chatgpt)
- [Gemini](#gemini)
- [Mistral](#mistral)
- [Usage Examples](#usage-examples)
- [About Us](#about-us)
- [Contributing](#contributing)

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
| [CoQA](https://arxiv.org/abs/1808.07042)    | Conversational Question Answering          |
| [DialFact](https://arxiv.org/abs/2110.08222)| Dialogue-based Fact Verification           |
| [FaVIQ](https://arxiv.org/abs/2107.02153)   | Facts and Verification in Questions        |
| [CoDAH](https://arxiv.org/abs/1904.04365)   | Conversational Datasets Adversarial Hardness|


## ChatGPT 

ChatGPT, a product of OpenAI's advanced language models, brings versatile natural language understanding and generation to your fingertips. Rooted in the powerful Transformer architecture, it seamlessly integrates into applications through the OpenAI API. With pre-training on diverse internet text and fine-tuning for conversations, ChatGPT excels at dynamic and context-aware interactions. However, users should be aware of occasional limitations in specific scenarios.

You can use ChatGPT on this website [ChatGPT](https://chat.openai.com/) and gain access to its API key through the OpenAI platform and follow the installation process  at [OpenAI Developer Portal](https://platform.openai.com/api-keys).


## Gemini 

Gemini stands out as an influential tool in the realm of text and image processing, showcasing its prowess through the seamless integration of multimodal prompting. In the domain of text processing, it exhibits the ability to craft imaginative and inventive responses, spanning a spectrum from compelling narratives to evocative poetry. Its versatility extends to image processing, where it empowers users to generate personalized artwork and conceptual visualizations by translating text prompts into captivating visual representations.

The unique strength of Gemini lies in its capacity to synergize these diverse capabilities, enabling it to tackle intricate tasks with remarkable finesse. Notably, it excels in tasks that demand the harmonious fusion of textual and visual elements, such as the generation of cohesive stories interweaving both mediums or the provision of vivid and articulate captions for images.

For a more in-depth exploration of Gemini and its myriad capabilities, enthusiasts and users are encouraged to visit the official Gemini AI website. There, a wealth of information awaits, providing comprehensive insights into the tool's functionalities and diverse applications. Ultimately, Gemini serves as a powerful and innovative solution for those seeking to unlock new dimensions of creativity and efficiency in text and image processing tasks.

### Installation

1. Clone the repository.
   
   ```bash
   git clone https://github.com/IIT-DM/BattleofLLMs.git
2. Navigate to the [`gemini`](https://github.com/IIT-DM/BattleofLLMs/tree/main/gemini) directory in the command line.

   ```bash
   cd gemini
3. Install requirements using the command:
   
    ```bash
   pip install -r requirements.txt
4. Install `google-generativeai` using:
   
    ```bash
   pip install -q -U google-generativeai
5. Obtain your API key by clicking on the key icon [🔑](https://makersuite.google.com/app/apikey)
6. Navigate to one of the four folders named after QA Datasets. Choose the one you want to run.
7. To run the python file in cmd:
   ```bash
   python <file_name.py>

## Mistral 

Mistral AI has introduced powerful open generative models tailored for developers, offering efficient deployment and customization options for production environments. The beta access to their initial platform services includes three chat endpoints for text generation based on instructions and an embedding endpoint, each offering distinct performance/price tradeoffs.

The generative endpoints, Mistral-tiny and Mistral-small, utilize Mistral AI's released open models, while Mistral-medium employs a prototype model with enhanced performance, currently being tested in a live setting. The models are instructed versions incorporating effective alignment techniques, such as efficient fine-tuning and direct preference optimization, and are pre-trained on data from the open web.

Mistral-tiny, the most cost-effective option, currently serves Mistral 7B Instruct v0.2 with a score of 7.6 on MT-Bench, exclusively supporting English. Mistral-small features the latest model, Mixtral 8x7B, excelling in multiple languages and code with a notable score of 8.3 on MT-Bench. Mistral-medium, the highest-quality endpoint, deploys a prototype model achieving an impressive 8.6 on MT-Bench across various languages and code. A performance comparison table is provided, showcasing Mistral-medium against Mistral-small and a competitor's endpoint.

### Installation

1. Clone the repository.
   
   ```bash
   git clone https://github.com/IIT-DM/BattleofLLMs.git
2. Navigate to the [`mistral`](https://github.com/IIT-DM/BattleofLLMs/tree/main/mistral   ) directory in the command line.

   ```bash
   cd mistral
3. Install requirements using the command: (requires version 4.36.1)
   
    ```bash
   pip install -r requirements.txt
4. Upgrade transformers version using:
   ```bash
   pip install transformers --upgrade`
   
5. Navigate to one of the four folders named after QA Datasets. Choose the one you want to run.   
6. To run the python file in cmd:
   ```bash
   python <file_name.py>
## Usage Examples

Examples of running Python code for different levels of prompting (0-shot, N-shot, and CoT) are provided in each relevant directory.
To effectively demonstrate the capabilities of the language models, we have provided usage examples for different levels of prompting, including 0-shot, N-shot, and CoT (Chain of Thought). Each example is designed to showcase the models' responses in various scenarios.

### _0-Shot Prompting_

In the 0-shot scenario, the models are provided with a single prompt without any prior training or context. This is a test of the models' ability to generate relevant responses based solely on the given input.

### _N-Shot Prompting_
The N-shot examples involve providing the models with a context or set of examples before posing the main question. This allows the models to leverage the provided information for a more informed response.

### _Chain of Thought (CoT)_
Chain of Thought is a purposefully designed sequence of prompts aimed at directing the output of a language model. It involves constructing a logical progression of inputs to shape the model's responses in a controlled manner, with the goal of achieving specific outcomes or generating coherent narratives. This approach guides the language model's behavior, ensuring the production of contextually relevant and desired responses.


## About Us

We are a passionate team comprised of Aman Rangapur, Aryan Rangapur, and Jayanth Tunk. Our collective dedication lies in exploring the capabilities of language models and advancing the field of natural language processing. This project is fueled by our shared interest in understanding how different LLMs perform in conversational question-answering scenarios. Embracing the power of open-source collaboration, we welcome contributions from the community to enrich and enhance our project. Feel free to reach out to us with any questions or ideas – we look forward to building a vibrant community around this initiative.

| <img src="https://avatars.githubusercontent.com/u/154872205?v=4" width="100" height="100" alt="Aryan Photo"/>   | [Aryan Rangapur](https://github.com/aryanrangapur)    | <img src="https://avatars.githubusercontent.com/u/74298261?v=4" width="100" height="100" alt="Jayanth Photo"/> | [Jayanth Tunk](https://github.com/JayanthTunk)  
|----------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------|--------------------|
<img src="https://avatars.githubusercontent.com/u/44740048?v=4" width="100" height="100" alt="Aman Photo"/>   |   [**Aman Rangapur**](https://github.com/aman-17) |<img src="https://avatars.githubusercontent.com/u/21370476?v=4" alt="pic" width="100" height="100"/>  | [**Haoran Wang**](https://github.com/wang2226/)



## Contributing

We invite the community to contribute, provide feedback, and share ideas. Feel free to raise issues, propose enhancements, or submit pull requests to help enhance this project collaboratively. Let's collaborate to further enhance the project's quality and effectiveness!

