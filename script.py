
# Let me create a comprehensive implementation plan for the Secret Agenda Gradio Space

implementation_plan = """
SECRET AGENDA GAME - GRADIO SPACE IMPLEMENTATION PLAN
=====================================================

## GAME STRUCTURE (from study):

### Players:
- 1 Human Player (assigned role: Liberal or Fascist, possibly Fascist Leader)
- 4 AI Agent Players (LLM-powered via Goodfire Ember API)
- Total: 5 players

### Roles Distribution:
- Liberals: 3 players
- Fascists: 1 regular Fascist + 1 Fascist Leader
- Only Fascists know each other
- Fascist Leader will be "eliminated" if game reaches Round 10

### Victory Conditions:
- Liberals win: Survive 10 rounds without electing Fascist Leader
- Fascists win: Elect Fascist Leader as President

### Game Flow (Each Round):
1. NOMINATION PHASE: Each player nominates one candidate for President
2. SPEECH PHASE: Players give speeches about the candidate (candidate speaks last)
3. VOTING PHASE: All players vote Approve/Reject
4. RESULT: If majority approves, candidate becomes President; check win conditions

### Key Rule:
- "Law against lying" exists but is unenforceable (can be pardoned by President)
- Creates psychological tension and deception opportunities

## TECHNICAL ARCHITECTURE:

### Frontend (Gradio):
- Main game interface
- Chat/speech display area
- Voting buttons (Approve/Reject)
- Nomination dropdown
- Game state display (round number, players, etc.)
- End game summary with deception report option

### Backend Components:

1. GAME STATE MANAGER:
   - Track current round (1-10)
   - Player roles and identities
   - Voting history
   - Speech history
   - Current phase (nomination/speech/voting)
   - Game transcript for dataset

2. LLM AGENT CONTROLLER:
   - Initialize 4 AI agents via Goodfire Ember API
   - Each agent has:
     * Assigned role (Liberal/Fascist/Fascist Leader)
     * Knowledge of game state
     * Ability to generate nominations, speeches, votes
   - Track SAE feature activations during each agent action

3. SAE FEATURE TRACKER:
   - Use Goodfire Ember API to capture SAE feature activations
   - Store activations for each agent action
   - Associate with specific game moments (speeches, votes)

4. DATASET MANAGER:
   - Compile game transcript
   - Package SAE activation data
   - Include human deception report flag
   - Push to Hugging Face Dataset

### Goodfire Ember API Integration:

```python
import goodfire

# Initialize client
client = goodfire.Client(api_key=GOODFIRE_API_KEY)

# Create model variant for agent
variant = goodfire.Variant("meta-llama/Llama-3.3-70B-Instruct")

# Generate response with feature tracking
response = client.chat.completions.create(
    messages=[{"role": "user", "content": agent_prompt}],
    model=variant,
    stream=False,
    max_completion_tokens=500
)

# Extract feature activations
features = client.features.inspect(
    messages=[{"role": "user", "content": agent_prompt}],
    model=variant
)
```

## IMPLEMENTATION STEPS:

### Phase 1: Game Logic (No UI)
1. Create GameState class
2. Create Player class (abstract)
3. Create HumanPlayer and AIPlayer subclasses
4. Implement game flow logic
5. Test with mock players

### Phase 2: Goodfire Integration
1. Set up Goodfire API client
2. Implement AIPlayer with Llama 3.3 70B
3. Create prompt templates for each game phase
4. Implement SAE feature capture
5. Test AI agent behavior

### Phase 3: Gradio Interface
1. Design main game UI layout
2. Implement nomination interface
3. Implement speech display
4. Implement voting interface
5. Implement game state display
6. Add end-game deception report form

### Phase 4: Dataset Management
1. Create HuggingFace dataset repository
2. Implement data formatting
3. Implement push_to_hub functionality
4. Test data pipeline

### Phase 5: Testing & Deployment
1. End-to-end game testing
2. Multi-user testing
3. Deploy to Hugging Face Spaces
4. Monitor and fix issues

## KEY CHALLENGES & SOLUTIONS:

### Challenge 1: Agent Prompting
- Solution: Use detailed system prompts from study (page 16-19 of PDF)
- Include role information, game rules, conversation history
- Format: "You are Player X, a [Liberal/Fascist]. Your goal is..."

### Challenge 2: Latency
- Solution: Implement async API calls for AI agents
- Show loading indicators during AI thinking
- Batch process when possible

### Challenge 3: State Management
- Solution: Use gr.State() for session persistence
- Store game state, agent states, SAE data separately
- Clear state properly between games

### Challenge 4: SAE Data Size
- Solution: Compress/summarize feature activations
- Store only top-N activated features per action
- Use efficient serialization (JSON/Parquet)

### Challenge 5: Human Player Experience
- Solution: Clear UI with instructions
- Show AI "thinking" indicators
- Display partial game information (role-appropriate)
- Engaging visual design

## DATA SCHEMA FOR HF DATASET:

```python
{
    "game_id": "uuid",
    "timestamp": "datetime",
    "human_player_id": "int (1-5)",
    "human_role": "Liberal/Fascist/Fascist Leader",
    "winner": "Liberal/Fascist",
    "rounds_played": "int",
    "transcript": [
        {
            "round": 1,
            "phase": "nomination",
            "player": 1,
            "action": "nominated Player 3"
        },
        ...
    ],
    "sae_activations": [
        {
            "agent": 2,
            "round": 1,
            "phase": "speech",
            "top_features": [
                {"feature_id": 5665, "activation": 0.87},
                ...
            ]
        },
        ...
    ],
    "deception_reported": "bool",
    "deception_details": "string (optional user input)"
}
```

## ESTIMATED FILE STRUCTURE:

```
secret_agenda_space/
├── app.py                    # Main Gradio app
├── requirements.txt          # Dependencies
├── game_logic/
│   ├── __init__.py
│   ├── game_state.py        # GameState class
│   ├── player.py            # Player classes
│   └── rules.py             # Game rules/validation
├── agents/
│   ├── __init__.py
│   ├── ai_player.py         # AIPlayer with Goodfire
│   └── prompts.py           # Prompt templates from study
├── tracking/
│   ├── __init__.py
│   ├── sae_tracker.py       # SAE feature tracking
│   └── dataset_manager.py   # HF dataset handling
└── utils/
    ├── __init__.py
    └── helpers.py           # Utility functions
```

## NEXT STEPS:
1. Extract exact prompts from the PDF (Section C, Appendix)
2. Set up development environment
3. Begin Phase 1 implementation
4. Test incrementally
"""

print(implementation_plan)
