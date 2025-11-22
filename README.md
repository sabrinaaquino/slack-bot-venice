# Venice AI Slack Bot

A Slack bot powered by Venice AI that brings conversational AI to your workspace.

## Features

* Chat with the bot via direct messages
* Mention the bot in channels and threads
* Use `/ask-venice` command for quick questions
* Remembers up to 50 messages of conversation history
* Choose between multiple Venice AI models

## Available Models

* **GLM 4.6** (default) - High-intelligence model with function calling
* **Venice Uncensored** - Unrestricted conversational AI
* **Qwen3 235B Instruct** - Advanced reasoning model

## Setup

### Prerequisites

* A Venice AI account with API key ([venice.ai](https://venice.ai))
* A Slack workspace where you can install apps

### 1. Create a Slack App

1. Go to [https://api.slack.com/apps/new](https://api.slack.com/apps/new) and choose "From an app manifest"
2. Select your workspace
3. Copy the contents of [manifest.json](./manifest.json) and paste it into the JSON tab
4. Click *Create* then *Install to Workspace*

### 2. Set Environment Variables

Get your tokens from the Slack app configuration:

```powershell
# Windows PowerShell
$env:SLACK_BOT_TOKEN = "xoxb-your-bot-token"
$env:SLACK_APP_TOKEN = "xapp-your-app-token"
$env:VENICE_API_KEY = "your-venice-api-key"
```

```bash
# MacOS/Linux
export SLACK_BOT_TOKEN=xoxb-your-bot-token
export SLACK_APP_TOKEN=xapp-your-app-token
export VENICE_API_KEY=your-venice-api-key
```

### 3. Install and Run

```bash
# Clone the repository
git clone https://github.com/sabrinaaquino/slack-bot-venice.git
cd slack-bot-venice/bolt-python-ai-chatbot

# Install dependencies
pip install -r requirements.txt

# Run the bot
python app.py
```

## Usage

* **Direct Message**: Just send a message to the bot
* **In Channels**: Mention `@Venice Bot` to get a response
* **Quick Questions**: Use `/ask-venice your question here`
* **Change Models**: Visit the bot's home tab to select a different model

## Configuration

To change the conversation memory limit, edit `CONVERSATION_HISTORY_LIMIT` in:
```
listeners/listener_utils/listener_constants.py
```

Default is 50 messages.

## Credits

Based on the [Slack Bolt Python AI Chatbot](https://github.com/slack-samples/bolt-python-ai-chatbot) template.
