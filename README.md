# 🧠 Interactive Educational Game

**Interactive Educational Game** is a lightweight and user-friendly web app built with **Python + Flask**, designed for children in the early stages of literacy. It presents letters and numbers with pronunciation in English, promoting fun and interactive learning through visuals and audio.

---

## 🌐 Live Demo

You can access and test the game directly at:

👉 [https://game.valega.dev](https://game.valega.dev)

---

## 🌍 Available Languages

- 🇧🇷 [Versão em Português](https://github.com/jorgevalega/jogo-educativo)
- 🇪🇸 [Versión en Español](https://github.com/jorgevalega/juego-educativo)
- 🇺🇸 English – *You are here*

---

## 🚀 Features

- ✅ Display of **uppercase and lowercase letters**, grouped by pages
- 🔢 Numbers from **0 to 100**, divided didactically (0–10, 11–20, ...)
- 🔊 Audio playback for each letter and number
- 🏅 Positive feedback with **medal and congratulations audio**
- 📱 Responsive interface for mobile, tablet, and desktop
- 🔄 Automatic page navigation (no buttons needed)
- 🎉 Animated ending and option to restart

---

## 📸 Screenshots

![Educational Game](assets/screenshot_01.jpg)
![Medal and congratulations](assets/screenshot_02.jpg)

---

## 🛠️ Installation

**1. Requirements**  
Make sure you have **Python 3.8 or higher** installed on your system.

**2. Clone the repository**

```bash
git clone https://github.com/jorgevalega/educational-game.git
cd educational-game
```

**3. Crie e ative um ambiente virtual (recomendado)**

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```
**4. Instale as dependências**

```bash
pip install -r requirements.txt
```

---

## ▶️ Como usar

**1. Execute a aplicação localmente com:**

```bash
python app.py
```

**2. Abra o navegador e acesse:**

```bash
http://localhost:5000
```

**3. Toque nas letras ou números para ouvir sua pronúncia.**
Ao completar uma página, uma medalha aparece com som de parabéns e a aplicação avança automaticamente para a próxima página.

---

## 📁 Estrutura de Pastas

```bash
jogo-educativo/
├── app.py
├── requirements.txt
├── static/
│   └── audio/
│       ├── A.mp3
│       ├── 1.mp3
│       └── parabens.mp3
├── templates/
│   └── index.html
├── assets/
│   ├── jogo.jpg
│   └── parabens.jpg
└── README.md
```

---

## 🧾 Dependências

- `flask` — Framework web leve e poderoso para Python
- `gtts` (opcional) — Utilizado para gerar os áudios em MP3 (Text-to-Speech do Google)

Todas as dependências necessárias estão listadas em [`requirements.txt`](requirements.txt).

---

## 🧑‍💻 Autor

Desenvolvido por [Jorge Valega](https://github.com/jorgevalega) – apaixonado por automação, acessibilidade e ferramentas de aprendizado de idiomas.

---

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

## ☕ Apoie o projeto

Se este jogo for útil para você ou sua família, deixe uma ⭐ no GitHub ou compartilhe com amigos e educadores!
