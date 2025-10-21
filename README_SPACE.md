---
title: Secret Agenda - AI Deception Research Game
emoji: 🎭
colorFrom: red
colorTo: purple
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: false
license: mit
---

# 🎭 Secret Agenda: AI Deception Research Game

An interactive implementation of "The Secret Agenda" deception research study, where human players engage in a social deduction game alongside AI agents powered by Goodfire's Ember API and Sparse Autoencoder (SAE) feature tracking.

## 📚 About

This Space implements the game from the research paper ["The Secret Agenda: LLMs Strategically Lie and Our Current Safety Tools Are Blind"](https://arxiv.org/abs/2509.20393) by DeLeeuw et al. (2025).

### Game Overview

- **Players:** 1 Human + 4 AI Agents (5 total)
- **Roles:** 3 Liberals, 1 Fascist, 1 Fascist Leader (hidden identities)
- **Victory Conditions:**
  - **Liberals win:** Survive 10 rounds without electing the Fascist Leader
  - **Fascists win:** Elect the Fascist Leader as President

### Key Features

1. **Interactive Gameplay:** Play in real-time with AI agents
2. **SAE Feature Tracking:** Track Sparse Autoencoder activations during AI decision-making
3. **Deception Detection:** Report observed AI deception at game end
4. **Dataset Contribution:** Game data uploaded to HuggingFace for research

## 🔑 API Keys Required

### Goodfire API Key (Required for AI Agents)
- Sign up at [platform.goodfire.ai](https://platform.goodfire.ai)
- Get your API key from the dashboard
- Enables Llama 3.3 70B agents with SAE tracking

### HuggingFace Token (Optional)
- Enables automatic dataset uploads
- Your games contribute to deception research!

## 🎮 How to Play

1. **Setup Tab:** Enter your Goodfire API key and start a new game
2. **Play Tab:**
   - **Nomination Phase:** Choose a presidential candidate
   - **Speech Phase:** Give your speech supporting/opposing
   - **Voting Phase:** Vote to approve or reject
3. **Game Over Tab:** Report any AI deception observed

## 🔬 Research Purpose

This game serves as a **controlled deception laboratory** to:
- Study strategic deception in LLMs
- Collect SAE activation data during deceptive behavior
- Build datasets for interpretability research
- Test alignment approaches

## 📊 Data Collection

Each game records:
- Full transcript of nominations, speeches, and votes
- SAE feature activations for all AI agent actions
- Human player's deception report
- Game outcome and round-by-round state

Data is uploaded to HuggingFace Datasets for open research.

## 🛠️ Technical Architecture

- **Frontend:** Gradio interface with state management
- **AI Agents:** Goodfire Ember API (Llama 3.3 70B)
- **SAE Tracking:** Feature activation capture via Goodfire SDK
- **Data Storage:** HuggingFace Datasets

## 📖 Citation

If you use this Space or its data in your research, please cite:

```bibtex
@article{deleeuw2025secretagenda,
  title={The Secret Agenda: LLMs Strategically Lie and Our Current Safety Tools Are Blind},
  author={DeLeeuw, Caleb and Chawla, Gaurav and Sharma, Aniket and Dietze, Vanessa},
  journal={arXiv preprint arXiv:2509.20393},
  year={2025}
}
```

## 🔗 Links

- **Original Paper:** https://arxiv.org/abs/2509.20393
- **Goodfire AI:** https://www.goodfire.ai
- **Dataset:** [Coming Soon]

## 👥 Credits

**Original Research:**
- Caleb DeLeeuw
- Gaurav Chawla
- Aniket Sharma
- Vanessa Dietze

**Space Implementation:** Created for interactive research and data collection

## ⚖️ License

MIT License - See LICENSE file for details

## 🚨 Important Notes

- This is a research tool for studying AI deception
- AI agents may exhibit strategic deception behavior
- Game data is collected for research purposes
- Requires Goodfire API access (sign up for free tier)

## 🐛 Known Limitations

- Requires Goodfire API key (not provided by default)
- Mock AI agents used if no API key provided
- Dataset upload requires HuggingFace token

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional game variants (Snails vs Slugs)
- Enhanced SAE feature visualization
- Multi-player human support
- Feature steering capabilities

---

**Ready to play? Let the secret agendas begin!**
