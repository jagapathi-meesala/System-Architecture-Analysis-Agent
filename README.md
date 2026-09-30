# System Architecture Analysis Agent

A framework-independent Python agent for deterministic repository architecture profiling, architecture risk detection, and structured reporting.

## Architecture
The system has a contract layer, dynamic registry, domain tools, framework-neutral adapters, configuration, skills, tests, and verification. Core logic does not import CrewAI, LangChain, OpenAI, Claude, or Lyzr.

## Installation
Create a virtual environment and install `requirements.txt`. Runtime configuration is supplied through environment variables; no production secrets are committed.

## Configuration
Required variables are `ARCHITECTURE_MAX_FILES`, `ARCHITECTURE_MAX_FILE_BYTES`, and `ARCHITECTURE_REPORT_FORMAT`. The example file intentionally contains placeholders rather than operational defaults.

## Tools
- `validate_architecture_input.py`: validates analysis targets.
- `analyze_architecture.py`: profiles repository file and language structure.
- `detect_architecture_risks.py`: applies deterministic architecture risk heuristics.
- `generate_architecture_report.py`: produces a structured report.

## Skills
Architecture analysis, risk assessment, and reporting are documented in `skills/`.

## Usage
The Python registry can register the tools as framework-independent contracts and execute them with structured arguments. The tools can also be imported directly for deterministic local analysis.

## Testing
Run `pytest -q`. The suite covers core execution, contracts, registry behavior, adapters, security, documentation, invalid inputs, and manifest validation.

## Portability
The core exposes plain Python interfaces and an adapter boundary. OpenAI SDK, CrewAI, Claude Code, and Lyzr mappings are intentionally not claimed as tested integrations in this repository.

## Limitations
Static repository analysis does not prove runtime topology, deployment behavior, service health, or hidden external dependencies. Findings are evidence-based signals requiring engineering review.
