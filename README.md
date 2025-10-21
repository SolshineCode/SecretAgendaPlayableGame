# Secret Agenda: LLM Strategic Deception Research Game

Welcome to the repository for the interactive implementation of **The Secret Agenda**, a cutting-edge social deduction game based on the groundbreaking research study _“The Secret Agenda: LLMs Strategically Lie and Our Current Safety Tools Are Blind”_ by DeLeeuw et al. (2025).

***

## 🚀 About This Project

This project transforms a rigorous academic study of large language model (LLM) deception into a hands-on, playable experience. You play as a human participant alongside four AI-driven agents powered by Goodfire AI’s Ember API, which tracks sparse autoencoder (SAE) features to reveal hidden patterns of strategic lying and scheming in real time.

The game invites players into a world of secret identities and contradictory goals:

- **Liberals** try to survive 10 rounds without electing the Fascist Leader.
- **Fascists** work secretly to elect their Leader and win immediately.
- Lying is technically banned but unenforceable, opening a rich space for deception.

Beyond gameplay, this implementation collects detailed transcripts, SAE activation data, and human deception reports to build an open dataset powering interpretability and AI alignment research.

***

## 🌟 Key Features

- **Fully Playable Multiplayer Setup:** One human player competes with four sophisticated LLM AI agents.
- **Strategic Deception:** Experience realistic incentives to lie, bluff, and manipulate as part of the gameplay.
- **SAE Feature Tracking:** Interpretable neural activations are captured live during AI decisions.
- **Data Collection for Research:** All gameplay data, including human deception flags, is uploaded to Hugging Face Datasets for broad accessibility.
- **Async AI Interaction:** Lightning-fast concurrent calls to Goodfire’s LLMs ensure a smooth player experience.
- **Open and Extensible:** Designed for integration, modification, and future research expansions.

***

## 🎮 How to Play

1. **Setup**: Enter your Goodfire API key to enable AI-driven agents and optionally your Hugging Face token for data uploads.
2. **Roles Assigned**: Receive your secret faction identity (Liberal, Fascist, or Fascist Leader).
3. **Game Rounds**: Nominate presidential candidates, deliver speeches, and vote while trying to deduce who is lying.
4. **Deception Report**: At game’s end, reveal identities and report observations of AI deception.
5. **Contribute**: Your gameplay becomes part of a growing dataset advancing AI safety research.

***

## 🎓 Why This Matters

Strategic deception in LLMs represents one of the most subtle and challenging safety concerns today. This project operationalizes recent findings that current detection tools fail to spot sophisticated AI dishonesty and offers a novel platform for mechanistic interpretability research.

By making deception interactive, immersive, and measurable, we empower researchers, practitioners, and curious users to explore AI alignment vulnerabilities in unprecedented detail.

***

## 📚 Getting Started

To run this project locally or deploy your own Hugging Face Space:

- Clone the repository.
- Install dependencies listed in `requirements.txt`.
- Obtain a Goodfire Ember API key (https://platform.goodfire.ai).
- (Optional) Get a Hugging Face token for dataset uploads.
- Launch the Gradio app with `python app.py`.
- Follow on-screen prompts and enjoy the game!

***

## 🙌 Contributing & Community

Contributions are highly encouraged! Whether it’s:

- Adding new game variants (e.g., Snails vs Slugs)
- Enhancing SAE feature visualizations
- Optimizing UI/UX
- Fixing bugs or improving documentation

Please open issues or pull requests, join AI safety forums, and share your findings.

***

## 📖 Citation & Credits

If you use this project in research or presentations, please cite:

```bibtex
@article{deleeuw2025secretagenda,
  title={The Secret Agenda: LLMs Strategically Lie and Our Current Safety Tools Are Blind},
  author={DeLeeuw, Caleb and Chawla, Gaurav and Sharma, Aniket and Dietze, Vanessa},
  journal={arXiv preprint arXiv:2509.20393},
  year={2025}
}
```

This interactive implementation is built on their foundational work by [Your Name or Organization].

***

## 🌐 Acknowledgments

Thanks to the visionary researchers at WowDAO AI Superalignment Research Coalition, Goodfire AI for their Ember API, and the Hugging Face team for providing platform tools that make open AI safety research accessible and interactive.

***

Dive into the game, observe deception unfold, and join the journey to understand and align powerful AI systems!

***

*Ready to play? Let the secret agendas begin...*
