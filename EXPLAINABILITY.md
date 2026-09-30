## Inputs and Data Sources
The agent accepts a repository path and optional analysis limits such as maximum files and maximum file size. Its data source is the filesystem content visible under that repository path; it uses file names, extensions, sizes, and directory structure rather than external services.

### Input Requirements
The path must exist and resolve to a directory. Optional numeric limits must be positive integers when supplied.

### Failure Handling
Missing paths, non-directory paths, malformed objects, and invalid values are rejected before analysis. Files that cannot be read or exceed the configured size limit are skipped rather than treated as evidence.

## Decision and Reasoning
The agent decides architecture findings from deterministic repository observations such as file counts, technology categories, and top-level distribution. Risk rules are explicit: for example, an empty analyzable source surface is reported as a high-severity evidence gap, while a large or highly polyglot surface is reported as a review signal.

### Rules Applied
Each finding records a rule identifier, severity, finding text, and supporting evidence. The report generator combines the observed architecture profile and risk assessment without changing the underlying evidence.

### Expected Outputs
Outputs are structured dictionaries containing analysis, risks, summaries, and limitations. No output claims that static inspection proves runtime topology, deployment behavior, or external-service behavior.

### Worked Example
A repository containing Python and TypeScript files produces language counts for those categories and a corresponding architecture profile. If the same repository exceeds the configured file threshold, the deterministic large-repository rule may add a medium-severity review signal.

## Limits and Constraints
The agent cannot infer complete runtime architecture from filenames and directory structure alone. Dynamic service discovery, network topology, deployment orchestration, database schemas, and hidden external dependencies require additional evidence that this implementation does not automatically obtain.

### Constraints
The analysis is bounded by maximum file count and maximum file size settings. The implementation also skips common generated or dependency directories such as `.git`, virtual environments, `node_modules`, build output, and Python caches.

### Unsupported Behavior
It does not execute application code during architecture analysis. It does not claim framework certification or HiDevs verification merely because local tests pass.
