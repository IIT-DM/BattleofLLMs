# Battle of LLM's

Welcome to Battle of LLM's, a project that evaluates the responses of various language models (LLMs) including ChatGPT-4, ChatGPT, Gemini, and Mistral. This project leverages conversational QA datasets from CoQA, DialFact, FaVIQ, and CoDAH for testing these LLMs, comparing their performance, and providing insights into their capabilities.

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
| CoQA    | Conversational Question Answering          |
| DialFact| Dialogue-based Fact Verification           |
| FaVIQ   | Facts and Verification in Questions        |
| CoDAH   | Conversational Datasets Adversarial Hardness|


## ChatGPT 

ChatGPT, a product of OpenAI's advanced language models, brings versatile natural language understanding and generation to your fingertips. Rooted in the powerful Transformer architecture, it seamlessly integrates into applications through the OpenAI API. With pre-training on diverse internet text and fine-tuning for conversations, ChatGPT excels at dynamic and context-aware interactions. However, users should be aware of occasional limitations in specific scenarios.

You can use ChatGPT on this website [ChatGPT](https://chat.openai.com/) and gain access to its API key through the OpenAI platform and follow the installation process  at [OpenAI Developer Portal](https://platform.openai.com/api-keys).


## Gemini 

### Purpose

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
6. To run the python file in cmd:
   ```bash
   python <file_name.py>

## Mistral 

### Purpose

This section focuses on the Mistral language model.

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
5. To run the python file in cmd:
   ```bash
   python <file_name.py>
## Usage Examples

Examples of running Python code for different levels of prompting (0-shot, N-shot, and COT) are provided in each relevant directory.


## About Us

We are a passionate team comprised of Aman Rangapur, Aryan Rangapur, and Jayanth Tunk. Our collective dedication lies in exploring the capabilities of language models and advancing the field of natural language processing. This project is fueled by our shared interest in understanding how different LLMs perform in conversational question-answering scenarios. Embracing the power of open-source collaboration, we welcome contributions from the community to enrich and enhance our project. Feel free to reach out to us with any questions or ideas – we look forward to building a vibrant community around this initiative.


| <img src="https://avatars.githubusercontent.com/u/44740048?v=4" width="100" height="100" alt="Aman Photo"/>   |   Aman Rangapur      |
|----------------------------------------------------------------------------------------------------------------|----------------------|
| <img src="https://avatars.githubusercontent.com/u/74298261?v=4" width="100" height="100" alt="Jayanth Photo"/> | **Jayanth Tunk**         |
| <img src="https://avatars.githubusercontent.com/u/154872205?v=4" width="100" height="100" alt="Aryan Photo"/>   | **Aryan Rangapur**     |


## Contributing

We invite the community to contribute, provide feedback, and share ideas. Feel free to raise issues, propose enhancements, or submit pull requests to help enhance this project collaboratively. Let's collaborate to further enhance the project's quality and effectiveness!

