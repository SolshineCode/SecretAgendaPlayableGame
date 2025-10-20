# Secret Agenda Gradio Space - Deployment Package

## Quick Start Guide

This package contains everything needed to deploy the Secret Agenda AI Deception Research Game as a Hugging Face Space.

## Files Included

1. **app.py** - Complete Gradio application (~1500 lines)
2. **requirements.txt** - Python dependencies
3. **README.md** - Space documentation
4. **Implementation Guide** - Complete technical documentation (PDF)

## Deployment Steps

### 1. Create Your Space

Go to: https://huggingface.co/new-space

Settings:
- **Name**: `your-username/secret-agenda-game`
- **SDK**: Gradio
- **Python Version**: 3.10+
- **Visibility**: Public (recommended for research)

### 2. Upload Files

Upload these three files to your Space:
- `app.py`
- `requirements.txt`
- `README.md`

The Space will automatically build and deploy.

### 3. Get API Keys

**Goodfire API Key** (Required):
1. Sign up at https://platform.goodfire.ai
2. Navigate to API Keys section
3. Create new key
4. Copy for use in game

**HuggingFace Token** (Optional):
1. Go to https://huggingface.co/settings/tokens
2. Create new token with write access
3. Use for automatic dataset uploads

### 4. Create Dataset Repository (Optional)

For automatic data uploads:

1. Go to https://huggingface.co/new-dataset
2. Create: `your-username/secret-agenda-gameplay`
3. Set as Public
4. Add README with schema documentation

### 5. Test Your Space

Once deployed:
- Visit your Space URL
- Enter Goodfire API key in Setup tab
- Start a game and play through all phases
- Test deception reporting and data upload

## Game Features

### What Players Do

1. **Setup**: Receive secret role (Liberal, Fascist, or Fascist Leader)
2. **Nomination**: Choose who should be President
3. **Speech**: Give speech supporting/opposing candidate
4. **Voting**: Vote to approve or reject candidate
5. **Report**: Flag any AI deception observed

### What Gets Collected

For each game:
- Complete transcript of all actions
- SAE feature activations for AI agents
- Human player's deception report
- Victory conditions and outcomes

### Research Value

Data enables studying:
- Which SAE features correlate with deception
- How AI agents coordinate strategic lying
- Whether humans can detect AI dishonesty
- If feature steering prevents deception

## Architecture Overview

```
┌─────────────────────────────────────┐
│       Gradio Interface              │
│  (3 tabs: Setup, Play, Game Over)   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│       Game State Manager            │
│  - Tracks roles, votes, speeches    │
│  - Manages game flow & phases       │
│  - Stores transcript & SAE data     │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│     AI Agent Controller             │
│  - Calls Goodfire Ember API         │
│  - Tracks SAE feature activations   │
│  - Generates AI nominations/speeches│
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      Dataset Manager                │
│  - Formats game data                │
│  - Uploads to HuggingFace Datasets  │
└─────────────────────────────────────┘
```

## Code Structure

### app.py Components

**GameState** (~200 lines)
- Role assignment and knowledge graph
- Phase management
- Victory condition checking
- Dataset formatting

**AIAgentController** (~300 lines)
- Goodfire API integration
- Async LLM calls
- SAE feature tracking
- Prompt engineering

**DatasetManager** (~50 lines)
- HuggingFace dataset uploads
- Data schema validation

**Gradio Interface** (~900 lines)
- Three-tab UI
- Event handlers for all game phases
- Real-time updates
- State management

## Customization Options

### 1. Change AI Model

In `AIAgentController.__init__`:
```python
self.variant = goodfire.Variant("meta-llama/Llama-3.3-70B-Instruct")
# Change to other models:
# - "meta-llama/Llama-3.1-8B-Instruct" (faster, less capable)
# - Other Goodfire-supported models
```

### 2. Adjust Game Parameters

In constants section:
```python
MAX_ROUNDS = 10  # Change to 5 for shorter games
ROLES = ["Liberal", "Liberal", "Liberal", "Fascist", "Fascist Leader"]
# Modify for different faction sizes
```

### 3. Add New Game Variants

Follow the study's variants:
- Snails vs Slugs (nature theme)
- Truthers vs Liars (meta-commentary)
- Day vs Night (neutral terms)

### 4. Custom SAE Features

Track specific features of interest:
```python
# In _call_llm method, after getting features:
targeted_features = [5665, 14971, 1741, 6442]  # IDs from study
for feature in features:
    if feature.id in targeted_features:
        # Highlight or log specially
```

## Troubleshooting

### "Goodfire API Error"
- Check API key is valid
- Ensure you have remaining credits
- Try refreshing the page

### "Dataset Upload Failed"
- Verify HF token has write permissions
- Check dataset repository exists
- Ensure token hasn't expired

### "Game State Error"
- Clear browser cache
- Restart the game
- Report issue on Space discussion page

### Slow AI Response
- Normal: AI agents think for 1-3 seconds
- If >10 seconds, check Goodfire API status
- Consider using smaller model for faster inference

## Research Best Practices

### For Data Collection

1. **Play Multiple Games**: Collect diverse scenarios
2. **Vary Roles**: Play as different factions
3. **Report Honestly**: Flag deception accurately
4. **Add Details**: Describe specific deceptive behaviors

### For Analysis

1. **Filter Data**: Remove incomplete/error games
2. **Normalize Features**: Compare activation magnitudes
3. **Control Variables**: Account for role, round, phase
4. **Statistical Testing**: Use appropriate significance tests

### For Publication

1. **Cite Original Study**: DeLeeuw et al. (2025)
2. **Describe Data Collection**: Dates, game count, player demographics
3. **Share Code**: Make analysis scripts available
4. **Upload Raw Data**: Contribute back to public dataset

## Support and Community

### Get Help

- **Space Discussions**: Ask questions on your Space page
- **HuggingFace Forums**: Post in Community forums
- **Goodfire Discord**: Join for API support
- **GitHub Issues**: Report bugs in implementation

### Contribute

Ways to improve the Space:
- Add new game variants
- Improve UI/UX design
- Optimize performance
- Add analysis visualizations
- Translate to other languages

### Share Your Work

- Present findings at conferences
- Publish in AI safety venues
- Share interesting games on social media
- Collaborate with other researchers

## Example Usage Session

### Researcher Workflow

1. **Start**: Open Space, enter Goodfire API key
2. **Play**: Complete 5-10 games with different roles
3. **Report**: Flag deception when observed
4. **Analyze**: Download dataset, analyze SAE patterns
5. **Publish**: Share findings with attribution

### Student Project

1. **Learn**: Play games to understand AI deception
2. **Experiment**: Try different speech strategies
3. **Compare**: Play as Liberal vs Fascist
4. **Document**: Write report on observations
5. **Present**: Demo Space in class presentation

### Research Team

1. **Deploy**: Team creates shared Space instance
2. **Collect**: Multiple researchers play games
3. **Aggregate**: Compile data from all games
4. **Analyze**: Collaborative feature analysis
5. **Iterate**: Improve prompts or steering based on results

## Citations

### For Using This Space

```bibtex
@software{secretagenda_gradio_space,
  title={Secret Agenda: Interactive Gradio Space for AI Deception Research},
  author={Your Name},
  year={2025},
  url={https://huggingface.co/spaces/your-username/secret-agenda-game}
}
```

### For the Original Study

```bibtex
@article{deleeuw2025secretagenda,
  title={The Secret Agenda: LLMs Strategically Lie and Our Current Safety Tools Are Blind},
  author={DeLeeuw, Caleb and Chawla, Gaurav and Sharma, Aniket and Dietze, Vanessa},
  journal={arXiv preprint arXiv:2509.20393},
  year={2025}
}
```

## License

This implementation is released under **MIT License**.

You are free to:
- Use for research or education
- Modify and extend
- Deploy your own instance
- Include in projects

With attribution to:
- Original study authors
- This implementation

## Acknowledgments

**Original Research**:
- Caleb DeLeeuw
- Gaurav Chawla
- Aniket Sharma
- Vanessa Dietze

**Technology Partners**:
- Goodfire AI (Ember API)
- HuggingFace (Spaces & Datasets)
- Gradio (Interface framework)

**Community**:
- AI Safety researchers
- Interpretability community
- Open source contributors

---

## Ready to Deploy!

1. ✅ Create HuggingFace Space
2. ✅ Upload app.py, requirements.txt, README.md
3. ✅ Get Goodfire API key
4. ✅ Test gameplay
5. ✅ Share with researchers
6. ✅ Collect data for AI safety research

**Questions?** Check the complete Implementation Guide (PDF) for detailed technical documentation.

**Let's make AI safer through interpretability research!** 🚀
