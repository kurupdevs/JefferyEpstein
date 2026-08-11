# Contributing to JEK Userbot

Thank you for your interest in contributing! 🎉

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/JefferyEpstein.git
   cd JefferyEpstein
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Guidelines

### Code Style
- Follow [PEP 8](https://pep8.org/) style guidelines
- Use 4 spaces for indentation (no tabs)
- Keep lines under 120 characters
- Use meaningful variable and function names
- Add docstrings to all functions

### Commit Messages
- Use the present tense ("Add feature" not "Added feature")
- Keep the first line under 72 characters
- Reference issues and pull requests when relevant

### Adding New Modules

1. Create your module in `modules/` or `modules/custom_modules/`
2. Follow the existing module pattern:
   ```python
   import logging
   from pyrogram import Client, filters
   from pyrogram.types import Message

   logger = logging.getLogger(__name__)

   async def setup(c: Client):
       """Register command handlers."""
       c.on_message(filters.command("mycommand", prefixes=".") & filters.me)(handler)

   async def handler(c: Client, m: Message):
       """Handle my custom command."""
       await m.edit("Hello from my custom module!")
   ```
3. Import your module in `modules/__init__.py` if needed

### Testing
- Run existing tests: `python -m pytest tests/`
- Add tests for new features in the `tests/` directory

## Pull Request Process

1. Update the `CHANGELOG.md` with your changes
2. Make sure all tests pass
3. Update documentation if you're changing functionality
4. Your PR will be reviewed by a maintainer

## Reporting Bugs

Use the [Bug Report](https://github.com/kurupdevs/JefferyEpstein/issues/new?template=bug_report.md) template.

Include:
- Python version
- Pyrogram version
- Steps to reproduce
- Expected vs actual behavior
- Error logs if applicable

## Feature Requests

Use the [Feature Request](https://github.com/kurupdevs/JefferyEpstein/issues/new?template=feature_request.md) template.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the project

---

Thanks for contributing! 💜
