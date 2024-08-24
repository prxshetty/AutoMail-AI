# Auto-Mail AI

Auto-Mail AI is a Python-based automated email response system. It listens to an inbox for incoming emails and automatically generates a response based on the content of the email. This project is ideal for companies that need to address customer queries quickly and efficiently.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Results](#results)


## Features
- Automatically checks for new emails in the inbox.
- Responds to emails based on predefined conditions.
- Can be configured to respond to specific email addresses.
- Customizable email response content.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/auto-mail-ai.git
    cd auto-mail-ai
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the whitelist of email addresses that should trigger automatic responses. This can be done in the `whitelist.yaml` file:
    ```yaml
    whitelist:
      - example1@example.com
      - example2@example.com
      - example3@example.com
    ```

## Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. The script will start checking the configured inbox for new emails and will automatically respond based on the content of the email and the configuration.

## Configuration

- The `whitelist.yaml` file should contain all the email addresses that should trigger the auto-response:
    ```yaml
    whitelist:
      - example1@example.com
      - example2@example.com
      - example3@example.com
    ```

## Results

### Terminal Output
The terminal displays the log of activities such as checking for new emails and sending responses.

<img width="1279" alt="TerminalOutput" src="https://github.com/user-attachments/assets/6a45ecb0-efbd-4b40-8460-ed8529eab798">


### Email in Inbox
The system checks for new emails in the inbox. Here's an example:


<img width="1184" alt="MailinInbox" src="https://github.com/user-attachments/assets/97ee5b09-3d5d-4218-b885-6da4ceb03618">

### Automated Response
Based on the content of the received email, the system generates an appropriate response.

<img width="1184" alt="AIResponseMail" src="https://github.com/user-attachments/assets/76fb2776-8d4e-46a9-ae97-28ca184d1d01">

### Future Work

- Make this into a webapp for automated responses to recruiters, job offers, etc.
- Add a automatic listing system, so that there is no need to keep adding into whitelist ( Or just turn it into blacklist)
- Improve the terminal Output in a more description format 
- Sort the emails Function into Categorys: If a Job got rejected, put it in a Rejected Label Category and so on
- More Ideas are welcome!
