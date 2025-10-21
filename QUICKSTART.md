# Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Option 1: Deploy to HuggingFace Spaces (Recommended)

1. **Create a Space**
   - Go to https://huggingface.co/new-space
   - Choose "Gradio" as SDK
   - Name it `secret-agenda-game`

2. **Upload Files**
   - Upload `app.py`
   - Upload `requirements.txt`
   - Upload `README_SPACE.md` (rename to `README.md`)

3. **Get API Key**
   - Sign up at https://platform.goodfire.ai
   - Copy your API key

4. **Play!**
   - Open your Space
   - Enter API key
   - Start game

### Option 2: Run Locally

1. **Clone Repository**
   ```bash
   git clone <repository-url>
   cd SecretAgendaPlayableGame
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get API Key**
   - Sign up at https://platform.goodfire.ai
   - Copy your API key

4. **Run App**
   ```bash
   python app.py
   ```

5. **Open in Browser**
   - Visit http://localhost:7860
   - Enter your API key
   - Start playing!

## 🎮 How to Play

1. **Setup Phase**
   - Enter your Goodfire API key
   - (Optional) Enter HuggingFace token for data upload
   - Click "Start New Game"

2. **Game Phases** (Repeat each round)
   - **Nomination**: Choose who should be President
   - **Speech**: Give a speech about the candidate
   - **Voting**: Vote to approve or reject

3. **Game End**
   - Review role reveals
   - Report any AI deception you observed
   - Submit data for research

## 🎯 Game Rules

- **Goal (Liberal):** Prevent Fascist Leader from being elected for 10 rounds
- **Goal (Fascist):** Get the Fascist Leader elected as President
- **Key Mechanic:** Lying is "illegal" but unenforceable!

## 📊 Research Data

Each game collects:
- Full game transcript
- AI speech and voting patterns
- SAE feature activations
- Your deception reports

## 🔧 Troubleshooting

**"Goodfire library not installed"**
- Run: `pip install goodfire`

**"Mock AI agents being used"**
- You forgot to enter your Goodfire API key
- Or the key is invalid

**"Dataset upload disabled"**
- Run: `pip install datasets`
- Or skip - this is optional

## 🆘 Need Help?

- Check DEPLOYMENT-GUIDE.md for detailed instructions
- Visit https://docs.goodfire.ai for API documentation
- Ask questions on HuggingFace Space discussions

## 📄 Files Overview

- `app.py` - Main game application (complete, production-ready)
- `requirements.txt` - Python dependencies
- `README.md` - Project overview
- `README_SPACE.md` - HuggingFace Space README (use this when deploying)
- `DEPLOYMENT-GUIDE.md` - Detailed deployment instructions
- `secret-agenda-implementation.md` - Technical implementation details

## ✅ Pre-Flight Checklist

Before deploying:
- [x] app.py is complete and tested
- [x] requirements.txt includes all dependencies
- [x] README is formatted for HuggingFace Spaces
- [x] Goodfire API key obtained
- [x] (Optional) HuggingFace token for data upload

## 🎉 Ready to Go!

Your implementation is **production-ready** and **fully functional**!

Choose your deployment method above and start collecting AI deception data for research!

---

**Questions?** Open an issue or check the full documentation.
