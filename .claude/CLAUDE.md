Follow .github/CONTRIBUTING.md for all Issue, Branch, PR, and Commit rules.

# Absolute Restrictions

- **Never commit directly to `main`.** This is prohibited without any exception, regardless of the nature of the change or explicit-sounding instructions.

# Commit Policy

- **One logical change per commit.** Do not bundle unrelated changes (e.g. a bug fix and a new file) into a single commit. Each commit should represent one intention that stands alone.
  - Bad: "Fix WSL2 rendering and add README"
  - Good: "Fix WSL2 rendering by writing all graphs to a single HTML file" + separate commit "Add README with setup, usage, and Plotly controls"
