# 🧠 MindGuard AI – Emotion Detection Chatbot

MindGuard AI is an interactive web-based chatbot that analyzes user emotions in real-time and responds intelligently. It also visualizes mood using dynamic graphs and animated emojis for a more engaging experience.

---

## 🚀 Features

* 💬 **Smart Chatbot** – Responds based on detected emotion
* 🧠 **Emotion Detection** – Classifies text into:

  * Positive 😄
  * Negative 😔
  * Neutral 🙂
* 📊 **Live Mood Graph** – Visual bar chart using Chart.js
* 🎯 **Emoji Visualization**

  * Emoji appears on top of graph bars
  * Animated **jump effect** for better UX
* 🎤 **Voice Input Support** – Speak instead of typing
* ✨ **Glass UI Design** – Modern blurred interface
* ⚡ **Typing Animation** – Realistic bot response feel

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Database:** SQLite
* **Visualization:** Chart.js

---

## 📁 Project Structure

```
MindGuard-AI/
│
├── app.py
├── model.py
├── database.db
│
├── templates/
│   ├── login.html
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/mindguard-ai.git
cd mindguard-ai
```

### 2️⃣ Install dependencies

```bash
pip install flask
```

### 3️⃣ Run the application

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧪 How It Works

1. User enters text or uses voice input
2. `model.py` analyzes emotion
3. Chatbot generates a response
4. Graph updates dynamically
5. Emoji appears and animates based on mood

---

## 🎯 Example

```
You: I am feeling great today!
Bot: 😄 That's awesome! Keep smiling!

Graph → Positive bar active with 😄 jumping emoji
```

---

## 🔥 Future Enhancements

* 📈 Mood history tracking
* 👤 User login-based analytics
* 🤖 Advanced AI integration (OpenAI / NLP models)
* 📱 Mobile responsive UI
* 🔊 Voice output (Text-to-Speech)

---

## 👨‍💻 Author

**Bhargab Maji**

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
