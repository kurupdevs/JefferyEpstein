# 🐙 JefferyEpstein × Kurup Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0%2B-orange)
![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)

**A fast, lightweight all-in-one Telegram userbot with management, fun, and utility features.**

[Features](#-features) · [Setup](#-setup) · [Commands](#-commands) · [Docker](#-docker-deployment) · [Contributing](#-contributing)

</div>

---

## 📦 Features

### ⚡ Core
- **Fast & Lightweight** — Built on Pyrogram 2.0+, optimized for speed
- **Modular Plugin System** — Easy to add custom modules via `modules/custom_modules/`
- **AFK Mode** — Auto-reply when you're away
- **Alive Check** — Verify the userbot is up and running

### 🛡️ Management
- `.ban` — Ban users from groups (reply to target)
- `.unban` — Unban users from groups (reply to target)
- `.mute` — Restrict users from sending messages (reply to target)
- `.unmute` — Remove message restrictions (reply to target)

### 🎉 Fun
- `.fun` — Random fun commands and responses
- `.spam` — Spam messages (use responsibly!)
- `.sticker` — Sticker-related commands
- `.ping` — Check bot response time

### 🛠️ Utility
- `.notes` — Save and recall notes
- `.help` — Display the full help menu
- `.extra` — Additional utility commands
- **Anti-PM** — Auto-reply and block unwanted private messages

---

## 🚀 Setup

### Prerequisites
- Python 3.9 or higher
- A Telegram account
- Telegram API credentials ([get them here](https://my.telegram.org/apps))

### Quick Install

```bash
# Clone the repository
git clone https://github.com/kurupdevs/JefferyEpstein.git
cd JefferyEpstein

# Set up a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure your credentials
cp .env.example .env
# Edit .env with your API_ID, API_HASH, and STRING_SESSION

# Run the userbot
python main.py
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_ID` | Your Telegram API ID from my.telegram.org | ✅ Yes |
| `API_HASH` | Your Telegram API hash from my.telegram.org | ✅ Yes |
| `STRING_SESSION` | Pyrogram string session for your account | ✅ Yes |
| `DATABASE_TYPE` | Database backend (`sqlite` default) | ❌ No |
| `DATABASE_NAME` | Database file name | ❌ No |
| `PM_LIMIT` | Max private messages before blocking (anti-PM) | ❌ No |
| `PREFIX` | Command prefix (defaults to `.`) | ❌ No |

### Getting a String Session

```bash
pip install pyrogram
python -c "from pyrogram import Client; c=Client('session', api_id=YOUR_API_ID, api_hash='YOUR_API_HASH'); c.start(); c.export_session_string(); c.stop()"
```

Copy the output string and set it as `STRING_SESSION` in your `.env` file.

---

## 📋 Commands

All commands use `.` as the default prefix.

| Command | Category | Description |
|---------|----------|-------------|
| `.ping` | Core | Check if the userbot is responsive |
| `.alive` | Core | Show bot status |
| `.help` | Core | Display help menu |
| `.ban` | Management | Ban a user (reply to message) |
| `.unban` | Management | Unban a user (reply to message) |
| `.mute` | Management | Mute a user (reply to message) |
| `.unmute` | Management | Unmute a user (reply to message) |
| `.afk [reason]` | Core | Set AFK status |
| `.unafk` | Core | Remove AFK status |
| `.fun` | Fun | Fun commands |
| `.spam [count] [text]` | Fun | Send repeated messages |
| `.s` or `.sticker` | Fun | Find and send stickers |
| `.notes` | Utility | Manage saved notes |
| `.a` or `.approve` | Anti-PM | Approve a user to DM you |
| `.da` or `.disapprove` | Anti-PM | Remove user from approved list |

---

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Clone and configure
git clone https://github.com/kurupdevs/JefferyEpstein.git
cd JefferyEpstein
cp .env.example .env
# Edit .env with your credentials

# Build and run
docker compose up -d
```

### Using Docker

```bash
docker build -t jeffery-epstein .
docker run -d \
  --name jeffery-epstein \
  --env-file .env \
  -v $(pwd)/jeffery_epstein.db:/app/jeffery_epstein.db \
  jeffery-epstein
```

---

## 🏗️ Project Structure

```
JefferyEpstein/
├── main.py              # Entry point
├── config.py            # Configuration loader
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build instructions
├── docker-compose.yml   # Docker Compose configuration
├── Procfile             # Heroku deployment
├── app.json             # Heroku app config
├── modules/             # Bot modules
│   ├── __init__.py      # Module loader
│   ├── afk.py           # AFK module
│   ├── alive.py         # Alive check module
│   ├── antipm.py        # Anti-PM module
│   ├── extra.py         # Extra commands
│   ├── fun.py           # Fun commands
│   ├── help.py          # Help menu
│   ├── management.py    # Group management
│   ├── notes.py         # Notes system
│   ├── ping.py          # Ping module
│   ├── spam.py          # Spam module
│   ├── stickers.py      # Sticker module
│   ├── utility.py       # Utility functions
│   └── custom_modules/  # Place for custom plugins
└── utils/               # Utility helpers
    ├── __init__.py
    ├── config.py        # Config utilities
    ├── db.py            # Database helpers
    └── scripts.py       # Helper scripts
```

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

This userbot is for educational purposes. Use it responsibly and in accordance with Telegram's Terms of Service. The developer is not responsible for any misuse or account bans resulting from the use of this userbot.

---

<div align="center">
  <strong>Built with 💜 by <a href="https://github.com/kurupdevs">KurupDevs</a></strong>
</div>
