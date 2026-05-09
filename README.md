<div align="center">
  <img alt="Discord Bot Banner" src="https://cdn.squarecloud.app/png/github-readme.png">
</div>

> 📌 **Note:** This README is written in Portuguese because this project was created as part of a YouTube tutorial in Portuguese.

<h1 align="center">bot-de-reaction-role</h1>

<p align="center">Um bot de Discord para gerenciar reaction roles, criado durante um tutorial no Youtube usando <a href="https://discordpy.readthedocs.io/en/stable/" target="_blank">discord.py</a>.</p>

---

This project is a **reaction role bot** developed during a youtube **discord.py** tutorial. The main goal is to demonstrate how to manage roles automatically based on emoji reactions in messages.

The video can be found on YouTube:
https://youtu.be/E3uPTbR4GFU

## Features

- `/rr create` — Creates a reaction role embed message in a channel
- `/rr add` — Links an emoji reaction to a role in a message
- `/rr remove` — Removes an emoji-role mapping from a message
- `/rr list` — Lists all emoji-role mappings configured for a message
- Automatically assigns/removes roles when members add or remove reactions

## Setup

1. Clone this repository
2. Install the dependencies:
   ```
   pip install discord.py python-dotenv
   ```
3. Create a `.env` file with your bot token:
   ```
   TOKEN=your_token_here
   ```
4. Run the bot:
   ```
   python main.py
   ```

## Requirements

- Python 3.10+
- A Discord bot with the `Manage Roles` permission and all intents enabled
