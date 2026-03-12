# 🤖 AI Telegram Presentation Bot

AI powered Telegram bot that automatically generates **PowerPoint presentations, assignments and images** using AI.

The bot supports **Uzbek, Russian and English languages** and allows users to create professional presentations directly inside Telegram.

---

# 🚀 Features

✅ AI presentation generator
✅ AI assignment generator
✅ Image generation for slides
✅ Multi-language interface (UZ / RU / EN)
✅ Telegram WebApp interface
✅ Custom slide count (up to 25 slides)
✅ Optional images in slides
✅ Beautiful Telegram keyboards
✅ File storage system
✅ Docker support
✅ Render deployment support

---

# 🧠 AI Technology

This project uses:

* Google Gemini AI for content generation
* Python PPTX for presentation creation
* Aiogram for Telegram bot framework

---

# 📁 Project Structure

ai-presentation-bot

bot
ai
presentation
assignment
services
database
utils
storage
tests
webapp

main.py
requirements.txt
Dockerfile

---

# ⚙ Installation

Clone the repository

git clone https://github.com/yourusername/ai-presentation-bot.git

Enter project directory

cd ai-presentation-bot

Install dependencies

pip install -r requirements.txt

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

Example:

TELEGRAM_BOT_TOKEN=your_bot_token
GEMINI_API_KEY=your_gemini_api_key

---

# ▶ Running the Bot

Run the project using:

python main.py

The Telegram bot will start polling.

---

# 🐳 Docker Deployment

Build container

docker build -t ai-presentation-bot .

Run container

docker run -d ai-presentation-bot

---

# ☁ Deploy to Render

1. Push the project to GitHub
2. Connect repository to Render
3. Create new Web Service
4. Set start command

python main.py

---

# 📊 Bot Functions

The bot can:

• Generate presentations
• Generate assignments
• Generate images
• Provide Telegram Web interface
• Store generated files

---

# 📜 License

This project is open-source and free to use.

---

# 👨‍💻 Author

Created for learning AI + Telegram bot development.

