# Architecture Analysis Skill
## Purpose
Profile a repository using deterministic filesystem evidence.
## Inputs
Repository path plus optional positive analysis limits.
## Processing
Validate the path, skip generated/dependency directories, count analyzable files and technology categories, and record top-level distribution.
## Outputs
Structured architecture profile with counts and a bounded file sample.
## Limitations
Static file structure cannot establish runtime topology or service behavior.
## Expected Behavior
Reject invalid inputs and avoid reading secret values.
