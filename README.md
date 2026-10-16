
# AtlasResearch

AtlasResearch is a multi-agent AI research pipeline that takes a research question, gathers information from the web, and generates a structured research report.

The goal is to develop a model-agnostic system capable of producing evidence-backed, reproducible research documents with minimal human intervention.

## Current Architecture

The prototype consists of three AI agents:

- **Supervisor:** Coordinates the research workflow, invokes researcher agents, and synthesizes their findings.
- **Positive Researcher:** Investigates arguments, evidence, and perspectives supporting the research question's proposed hypothesis.
- **Negative Researcher:** Investigates counterarguments, limitations, risks, and alternative explanations.

Each researcher has access to Tavily web search with a bounded search budget. The supervisor combines their outputs into a final report.

### Current Workflow

1. Receive a research question.
2. Delegate research to specialized agents.
3. Conduct web searches within predefined budgets.
4. Collect and synthesize the researchers' findings.
5. Return a structured research report.

## Technology Stack

- **Python** — application and orchestration logic
- **LangGraph / LangChain** — agent workflow and model integration
- **Ollama** — local LLM inference
- **Qwen 3.5** — supervisor and researcher models
- **Tavily** — web search

The current setup runs the supervisor on a PC using Qwen 3.5 9B and the two researchers on a MacBook using Qwen 3.5 4B. LLM inference is local, while web search uses an external service.

## Benchmark

The first end-to-end benchmark was completed on October 16, 2026.

| Metric                       | Result                                                                                                                                  |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Research question            | Will AI coding agents fundamentally change software engineering, or will they primarily remain productivity tools for human developers? |
| End-to-end runtime           | Approximately 5 minutes, 10 seconds                                                                                                     |
| Agents                       | 1 supervisor + 2 researchers                                                                                                            |
| Positive researcher searches | 3                                                                                                                                       |
| Negative researcher searches | 4                                                                                                                                       |
| Output                       | Structured report containing 10 counterarguments                                                                                        |

The generated report examined productivity claims, task complexity, human review bottlenecks, software quality, measurement limitations, maintenance costs, and variable ROI.

**Note:** The benchmark measures pipeline execution and generated output, not independently verified research accuracy. Source traceability and claim verification remain areas for improvement.

## Running the Project

From the project root, run:

```bash
python3 -m agent.supervisor
```

Enter a research question when prompted.

The application requires its Python dependencies, Ollama models, appropriate model endpoints, and Tavily credentials to be configured. Refer to the project configuration for the exact setup.

## Planned Improvements

- Preserve source URLs and metadata alongside research findings.
- Verify citations and factual claims automatically.
- Improve balance between researchers' findings.
- Add cross-agent critique and iterative revision.
- Introduce checkpoints, retries, and execution-budget controls.
- Generate reproducible LaTeX and PDF research documents.
- Evaluate factual accuracy, citation validity, research coverage, runtime, and cost.

## Project Status

**Early prototype.** The current implementation demonstrates the core multi-agent research workflow. The next priority is improving evidence traceability, verification, and synthesis quality before treating its outputs as reliable research.
