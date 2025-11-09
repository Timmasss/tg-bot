# tg-bot
🤖 Telegram Bot in Python (Aiogram)
📌 Project Description

This project is a Telegram bot built with Python using the Aiogram 3 framework.
It demonstrates multiple useful and interactive features:

Greeting and command responses

Custom reply keyboards

Quiz (poll) functionality inside Telegram

Weather API integration (OpenWeatherMap)

Movie recommendations by genre

GIF echo support

Text-to-speech welcome message via pyttsx3

This bot is a great example project for your portfolio, university submission, or for learning how to build Telegram bots using Aiogram.

⚙️ Technologies Used

Python 3.10+

Aiogram 3.x — Telegram API wrapper

Requests — for working with external APIs

pyttsx3 — for voice synthesis (text-to-speech)

OpenWeatherMap API — to get real-time weather data

🧩 Bot Commands
Command	Description
/start	Sends a greeting message
/info	Displays a list of available commands
/name <your name>	Greets you by name
/test	Demonstrates HTML and Markdown formatting
/button	Shows simple reply buttons
/special_buttons	Displays buttons for requesting contact and a quiz
/films	Offers movie genre selection
/weather	Gets weather information for a chosen city
🎬 Example Interaction

User sends /start → bot replies: “Hello, I’m a test bot!”

User sends /films → bot shows genre options (Horror, Action, Comedy, Fantasy)

After selecting a genre, the bot sends a random movie recommendation.

User sends /weather → bot asks for a city name → shows weather details.
