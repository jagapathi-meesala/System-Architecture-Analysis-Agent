---
name: architecture-analysis
description: Analyze software repositories and identify their system architecture, components, technology structure, and architectural relationships.
---

# Architecture Analysis

## Purpose

Analyze a software repository and produce a structured description of its system architecture.

## Inputs

- Repository path
- Optional analysis limits such as maximum files and maximum file size

## Process

1. Inspect the repository structure.
2. Identify source files and technology categories.
3. Determine the top-level project organization.
4. Produce a structured architecture profile.
5. Clearly distinguish observed evidence from inferred architecture.

## Outputs

- File count
- Detected technology categories
- Top-level repository distribution
- Representative files
- Architecture observations

## Limitations

Static file-level analysis cannot completely reconstruct runtime topology, deployment behavior, external services, or dynamic dependencies.
