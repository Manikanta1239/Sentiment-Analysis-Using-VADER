# 📊 Sentiment Analysis Web Application

---

## 🚀 Project Overview
This **Flask-based web application** performs **sentiment analysis** on user-inputted text using **VADER (Valence Aware Dictionary and sEntiment Reasoner)**, a lexicon and rule-based tool optimized for analyzing social media and textual data.

---

## 🌟 Features
- ✅ Analyze sentiment of user-inputted text.
- ✅ Provides scores for **Positive**, **Neutral**, **Negative**, and **Compound** sentiments.
- ✅ Interactive, responsive UI built with **HTML**, **CSS**, and **Bootstrap**.
- ✅ Backend powered by **Flask** and **NLTK**.

---

## 🛠️ Technologies Used
### 🎨 Frontend
- **HTML**
- **CSS** (Styled with **Bootstrap** for responsiveness)

### ⚙️ Backend
- **Flask** (Python)
- **VADER Sentiment Analysis** from the **NLTK** library

### 📚 Additional Libraries
- **nltk** for text preprocessing and stopwords removal
- **re** for text cleaning
- **Bootstrap** for enhanced UI styling

---

## 🏗️ Installation and Setup
### Prerequisites
Ensure you have the following installed:
- ✅ Python 3.x
- ✅ pip (Python package manager)

### 🔧 Steps to Install
1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK stopwords (if not already installed):**
   ```bash
   python -c "import nltk; nltk.download('stopwords')"
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Open the app in your browser:**
   Navigate to **http://127.0.0.1:5002/**.

---

## 📂 File Structure
```plaintext
<repo-name>/
├── app.py               # Main Flask application
├── templates/
│   └── form.html        # HTML template for UI
├── static/              # Directory for static files (if needed)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation (this file)
```

---

## 🏗️ How It Works
1. The user enters text into a text area and submits it for analysis.
2. The text is **cleaned** and **preprocessed** (removing punctuation, numbers, and stopwords).
3. VADER Sentiment Analyzer generates scores for:
   - ✅ **Positive Sentiment**
   - ⚪ **Neutral Sentiment**
   - ❌ **Negative Sentiment**
   - 🔢 **Compound Sentiment**
4. The results are displayed with percentage scores and detailed metrics.

---

## 🖼️ Example Screenshots
### ✅ Positive Sentiment
![image](https://github.com/user-attachments/assets/2ddf8bf6-3b72-4aad-bea1-75b1035081be)

### ⚪ Neutral Sentiment
![image](https://github.com/user-attachments/assets/83c3be16-98de-4643-9346-ba3274c2eb46)

### ❌ Negative Sentiment
![image](https://github.com/user-attachments/assets/3e7f57fd-cd54-47cb-8e3e-66cec04b1038)

---

## 🔮 Future Enhancements
- 📂 Support for analyzing **large texts** (e.g., uploaded files).
- 🌍 **Multi-language support** using advanced models like **mBERT**.
- 🔗 **Integration with APIs** for real-time text analysis.

---

## 🤝 Contribution Guidelines
We welcome contributions! You can contribute by:
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🔀 Submitting pull requests

---

## 📞 Contact
For any questions or suggestions, feel free to reach out:
- 📧 **Email**: smanikanta1239@gmail.com  
- 🐙 **GitHub**: [Manikanta1239](https://github.com/Manikanta1239/Sentiment-Analysis-Using-VADER/)  


