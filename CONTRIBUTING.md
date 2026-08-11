# Contributing to JEK Userbot

Thank you for your interest in contributing! 🎉

## Code of Conduct

Be respectful, welcoming, and constructive. Harassment and spam will not be tolerated.

## How to Contribute

### 🐛 Reporting Bugs

1. Check the [issues page](https://github.com/kurupdevs/JefferyEpstein/issues) to see if it's already reported
2. If not, create a new issue using the **Bug Report** template
3. Include:
   - Your Python version
   - Your Pyrogram version
   - Steps to reproduce
   - Expected vs actual behavior
   - Error logs (if any)

### 💡 Suggesting Features

1. Check existing issues and PRs to avoid duplicates
2. Open a **Feature Request** issue
3. Describe the feature and why it would be useful
4. If you can, outline a possible implementation

### 🔧 Pull Requests

1. **Fork** the repository
2. **Create a branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**: Keep them focused and well-documented
4. **Test** your changes thoroughly
5. **Commit** with clear messages: `git commit -m "Add: your feature description"`
6. **Push**: `git push origin feature/your-feature-name`
7. **Open a PR** against the `main` branch

### ✅ PR Checklist

- [ ] Code follows the existing style
- [ ] Changes are tested
- [ ] No new warnings or errors
- [ ] Documentation is updated if needed
- [ ] Commit messages are descriptive

## Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/JefferyEpstein.git
cd JefferyEpstein
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use meaningful variable and function names
- Add docstrings for new functions
- Keep modules focused — one feature per module

## Adding Custom Modules

Place custom modules in `modules/custom_modules/`:

```python
# modules/custom_modules/my_module.py
from pyrogram import Client, filters
from pyrogram.types import Message

async def setup(c: Client):
    c.on_message(filters.command("mycommand", prefixes=".") & filters.me)(my_handler)

async def my_handler(c: Client, m: Message):
    await m.edit("Hello from custom module!")
```

## Questions?

Open a [discussion](https://github.com/kurupdevs/JefferyEpstein/discussions) or ask in the issues section.

---

Thank you for contributing! 🚀
