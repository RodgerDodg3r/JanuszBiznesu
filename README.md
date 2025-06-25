
[img]https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRK7m597PMpPakfft8PyvkUwZ5ovk_aPJgaw&s[/img]

#Janusz Biznesu – Discord Bot

> **"Kasa sama się nie zrobi. Trzeba kombinować, inwestować i czasem przeklnąć."** – Janusz

**Janusz Biznesu** is a comedic, vulgar Discord bot inspired by *AdVenture Capitalist* — but instead of polite capitalism, you start by **hiring staff for a swingers club** and climb your way up to financial domination through shady biznesy and absurd humor. 💰🔥

---

## 💼 Features

- 🍑 **Start at the bottom**… literally, by hiring people in a swingers club.
- 🏗️ Unlock and upgrade new buildings (kebab stands, car washes, and other "enterprises").
- 🤑 Work, earn, and grow your empire using basic commands.
- 🤬 Enjoy the vulgar, sarcastic humor of Janusz — your mentor in capitalism.
- 📂 Uses JSON for persistent player data, no database setup needed.
- 🧮 Built with `discord.py`, `json`, `math`, and `os`.

---

## 📦 Requirements

Make sure you have Python 3.8+ and install required libraries:

```bash
pip install discord.py
```

Standard Python libraries used:
- `json` – for player save files
- `math` – for income and upgrades
- `os` – for file management

---

## 🚀 Setup Instructions

1. **Clone this repo:**

```bash
git clone https://github.com/yourusername/janusz-biznesu.git
cd janusz-biznesu
```

2. **Install dependencies:**

```bash
pip install discord.py
```

3. **Add your bot token:**

Create a file at:  
`/data/token.json`

Paste your token inside like this:

```json
{
  "token": "YOUR_DISCORD_BOT_TOKEN"
}
```

4. **Run the bot:**

```bash
python bot.py
```

---

## 🤖 Bot Commands

| Command         | Description                                                            |
|------------------|------------------------------------------------------------------------|
| `!panel`         | Shows your **player panel** with current money and building status     |
| `!pracuj`        | Simulates **working** — earn a random amount of money 💸               |
| `!kup_biznes`    | Lets you **buy new buildings** to expand your empire 🏢                |

More commands coming soon: upgrades, automation, bribery, and more spicy mechanics. 🌶️

---

## 🗂️ File Structure

```
janusz-biznesu/
├── bot.py
├── /data
│   ├── token.json       
│   └── config.json
├──── /players
```

---


## 💡 Contributions

Got funny ideas? Add a new biznes, some wild mechanics, or just spice up Janusz's rants.  
Pull requests welcome — just keep it hilarious *and* functional.

---

## 🧔 Final Words from Janusz

> *"Nie ma nic za darmo. Chcesz zarobić, to klikaj, kupuj i nie pytaj co to za firma."*

---

Enjoy the game. And remember: **Janusz always profits.**
