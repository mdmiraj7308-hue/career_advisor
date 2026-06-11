## AI Career Advisor & Agentic Roadmap Generator

An advanced, multi-agent AI career guidance system built with Python, LangGraph, and Streamlit. 

Unlike standard chatbots, this application utilizes a state-machine architecture to conduct real-time web research on local job markets, evaluate career feasibility, extract precise skill gaps from active job postings, and generate a personalized learning roadmap. It also designs a custom portfolio "Bridge Project" to help candidates qualify for their target roles.
---

## Business Value & Key Features
- Real-Time Market Research: Uses Tavily AI Search to bypass cluttered HTML and extract clean, real-time hiring data.
- Multi-Agent Orchestration:** Splits tasks between a "Research Analyst" agent and a "Realism Optimizer" agent to prevent LLM hallucination and ensure high-quality outputs.
- Actionable Roadmaps:** Generates step-by-step learning paths and custom portfolio project ideas based on live market gaps.
- Secure Persistence:** Implements SQLite and Bcrypt for secure user account management and report history tracking.
---

## System Architecture
This project is built around a decoupled **State Machine Architecture**. The workflow splits tasks among specialized agents that cooperatively read and write to a shared "clipboard" state.


                     ┌────────────────────────────────┐
                     │          Streamlit UI          │
                     │  (app.py / Sidebar Inputs)     │
                     └───────────────┬────────────────┘
                                     │
                        1. Invokes   │   4. Reads Final
                        build_graph()│      Roadmap
                                     ▼
                     ┌────────────────────────────────┐
                     │        LangGraph State         │
                     │ (CareerAdvisorState TypedDict) │
                     └───────────────┬────────────────┘
                                     │
                   ┌─────────────────┴─────────────────┐
                   │                                   │
                   ▼                                   ▼
         ┌──────────────────┐                ┌──────────────────┐
         │ 2. Research Node │                │ 3. Optimizer Node│
         │  (research_node) │                │ (optimizer_node) │
         └─────────┬────────┘                └─────────▲────────┘
                   │                                   │
                   ▼                                   │
         ┌──────────────────┐                          │
         │ Research Agent   │                          │
         │(research_analyst)│                          │
         └─────────┬────────┘                          │
                   │ Uses                              │
                   ▼                                   │
         ┌──────────────────┐                          │
         │ Tavily Search    ├──────────────────────────┘
         │ (tavily_search)  │
         └──────────────────┘


## The Workflow Pipeline:
- User Input: The user provides their career_goal, location, and background via the Streamlit sidebar.
- The Shared State: These inputs are initialized in CareerAdvisorState.
- Research Node: Calls the research_analyst agent. This agent utilizes the custom TavilySearch tool to scan the web for    real-time hiring data and updates the state with a detailed research_draft.
- Optimizer Node: Calls the realism_optimizer agent. This node reads both the user's background and the research_draft. It runs an analytical gap-analysis, designs a custom portfolio "Bridge Project", and updates the state with the final_report.
- UI Rendering: Streamlit reads the final_report and renders it cleanly using markdown tabs.

## Project Structure (Separation of Concerns):
'''Text
career-advisor/
├── .env                         # Secret API Keys (ignored by Git)
├── .gitignore                   # Security guard for keys & venv
├── requirements.txt             # Project library dependencies
├── app.py                       # Main Streamlit web application
├── career_advisor.db            # Local SQLite database (ignored by Git)
└── src/
    ├── config/
    │   └── settings.py          # Loads and validates environment variables
    ├── core/
    │   ├── llms/
    │   │   └── llm_factory.py   # Factory pattern for model initialization
    │   ├── state/
    │   │   └── state.py         # Defines strict keys for the shared LangGraph State
    │   └── tools/
    │       └── tavily_search.py # Connects and configures the Tavily search tool
    ├── prompts/                 # Holds raw system instructions for the LLMs
    ├── ui/                      # Layout components for the Streamlit interface
    └── workflow/
        ├── agents/
        │   ├── realism_optimizer.py # Realism Counselor prompt/chain logic
        │   └── research_analyst.py  # Market Analyst prompt/chain logic
        ├── graph/
        │   └── graph_builder.py # Combines nodes/edges into a compiled graph runnable
        └── nodes/
            ├── optimizer_node.py # Executes Realism Optimizer agent logic
            └── research_node.py  # Executes Research Analyst agent logic
'''



##  Local Setup & Installation: Follow these commands to clone, install, and run this project locally,

1. Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/career_advisor.git
cd career_advisor
```

2. Set Up and Activate Virtual Environment
Windows (PowerShell):
```PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
```


3. Install Dependencies
```bash
pip install -r requirements.txt
```

4.Setup Environment Variables:
Create a file named .env in the root directory and add your secret keys.

```Env
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```


5.Run the Application

```bash
streamlit run app.py
```

Open your web browser and navigate to http://localhost:8501.

Author: MD Miraj Islam | AI Engineer & Automation Specialist
Connect on LinkedIn




