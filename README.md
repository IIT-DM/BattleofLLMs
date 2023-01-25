## ChatGPT-Benchmarks

![](https://img.shields.io/badge/Languages-%20English-red) 
![](https://img.shields.io/badge/ChatGPT-Corpus%2C%20Detector-blue)


Welcome to our project on GitHub! We are thrilled to have you here, reading through our code and documentation. We hope that you find our project interesting and useful. We have put in a lot of effort to make the code readable, well-organized, and easy to understand. We believe that open-source projects like ours are an excellent way to share knowledge, build communities, and inspire new ideas. We welcome your contributions, feedback, and ideas. Thank you for your support and we look forward to your participation in this project.<br>


Purpose of the project is to:

a. Find the Golden ratio wrt to the existing QA corpus.

b. Plagiarism detection(also detects ChatGPT generated content).





### Upcoming Benchmarks and Releases:

| Release               | Dates      |
|-----------------------|------------|
| ChatGPT Crawler| Published |
| QA Corpus Comparison| 12/15/2022 to now(working) |
| Golden ratio w.r.t to QA corpus| Posting within a week |
| Preprint | Posting within a week |
|...|...|

### ChatGPT Crawler
# ChatGPT Crawler

This script automates the process sending a query to ChatGPT and saves the response.
Since the release of Dec 15th version, ChatGPT has imposed hourly limit per account.
To solve this, this script takes multiple accounts (I found the minimum to be 4), rotates and exhausts the hourly limit of each account.

In order to register an OpenAI account, you need an email and a phone number for verification. Note that it has to be a real phone number. Bummer! I tried to register accounts with Google Voice virtual phone number, OpenAI recognized it being a virtual number and wouldn't let me register.

## Installation

1. Please follow installation instruction from [pyChatGPT](https://github.com/terry3041/pyChatGPT)

2. Creates the following folders:

```sh
mkdir ./input_raw
mkdir ./input_processed
mkdir ./output_raw
mkdir ./output_processed
mkdir ./tokens
```

## Run

1. Save the tokens (a.k.a. `__Secure-next-auth.session-token`) as files under `./tokens` folder.
2. Modify `preprocess.py` to process the raw dataset. The end goal is to save the processed dataset as a Pandas Dataframe object, with a column named `query` that contains the queries to feed to ChatGPT.
3. Change `DATASET` variable in `pychatgpt.py`.
4. Start the script `./run.sh`.

## Datasets Used

### Traditional QA

| Name              | Link                                   | Year | Size |
| ----------------- | -------------------------------------- | ---- | ---- |
| AdversarialQA     | https://adversarialqa.github.io        | 2020 | -    |
| ARC               | https://allenai.org/data/arc           | 2018 | -    |
| Natural Questions | https://research.google/pubs/pub47761/ | 2019 | 307k |

### Dialogue QA

| Name     | Link                                        | Venue | Size |
| -------- | ------------------------------------------- | ----- | ---- |
| CoQA     | https://stanfordnlp.github.io/coqa/         | 2019  | 127K |
| DialFact | https://aclanthology.org/2022.acl-long.263/ | 2022  | 11k  |

### Commonsense QA

| Name | Link                                | Venue | Size |
| ---- | ----------------------------------- | ----- | ---- |
| CoQA | https://stanfordnlp.github.io/coqa/ | 2019  | 127K |


---

### About Us

We are researchers from Illinois Institute of Technology working on various Natural Language Programming projects. Our team for these projects consists of PhD and Master students. <br>

|   |   |
|:-:|:-:|
| [Haoran Wang](https://github.com/wang2226/) | [Aman Rangapur](https://github.com/aman-17/) |
|<img src="https://avatars.githubusercontent.com/u/21370476?v=4" alt="" width="40"/>|<img src="https://avatars.githubusercontent.com/u/44740048?v=4" alt="" width="40"/>|









