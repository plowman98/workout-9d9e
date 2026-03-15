# Contributing Guidelines

This document defines the development workflow using GitHub for this project.

As the project matures, these guidelines will evolve.
Rule changes must be submitted as a PR so that the history remains traceable.

## 1. Roles

**Maintainer:**
The user with final decision-making authority.
AI agents shall interpret *"Maintainer"* as *"the User."*

## 2. Issue Management

Every Issue must be categorized as one of the following:

- **Epic**
- **Task** (linked to an Epic)
- **Fast Track** (a lightweight Task that does *not* require an Epic)

Epic is the foundation of the workflow.
Fast Track exists as a controlled exception for small, self-contained work items.

> **Note:** Before creating the first Issue in a new repository, verify that all required labels (`epic`, `feature`, `bug`, `docs`, `refactor`, `chore`, `fast-track`) exist. Create any missing labels before proceeding.

### 2.1 Epic Issues

Epic Issues represent large, multi-step units of work.

Must use `.github/ISSUE_TEMPLATE/epic_template.md`.

- **Label:** `epic`
- **Rules:**
  - Files must *not* be modified directly on the Epic Branch.
  - The Epic Branch should only receive merge commits from Task Branches.
  - **Exceptions:**
    - Minor metadata fixes (e.g., labels, README typos)
    - Urgent fixes explicitly authorized by the Maintainer

### 2.2 Task Issues

Task Issues represent work items that belong to a specific Epic.

Must use `.github/ISSUE_TEMPLATE/task_template.md`.

- **Reference:** Must include `ref: #Epic_Number`
- **Labels:** One of `feature`, `bug`, `docs`, `refactor`, `chore`

### 2.3 Fast Track Issues (Epic-less Lightweight Tasks)

Fast Track Issues are a special category for small, self-contained changes that do not justify creating an Epic.
They exist as an exception to the Epic-first workflow.

Must use `.github/ISSUE_TEMPLATE/fast_track_template.md`.

#### Allowed Scope

A Fast Track Issue must satisfy **both** of the following:

- Self-contained — no dependencies on other open Issues
- Expected to be completed within **half a day**

#### Escalation to Epic

If a Fast Track Issue grows beyond its allowed scope during implementation, it must be escalated:

1. Stop work on the Fast Track Branch.
2. Create a new Epic Issue that absorbs the remaining work.
3. Open a Task Issue under the new Epic and continue from there.
4. Close the original Fast Track Issue with a reference to the new Epic (e.g., `Superseded by #Epic_Number`).

#### Rules

- **Label:** `fast-track` (mandatory), plus optionally one of `feature`, `bug`, `docs`, `refactor`, `chore`
- **Reference:** No Epic reference required

### 2.4 Summary of Issue Types

| Type           | Requires Epic | Labels                                        | Typical Use Case                  |
|----------------|---------------|-----------------------------------------------|-----------------------------------|
| **Epic**       | —             | `epic`                                        | Large features or multi-step work |
| **Task**       | Yes           | `feature`, `bug`, `docs`, `refactor`, `chore` | Work belonging to an Epic         |
| **Fast Track** | No            | `fast-track`                                  | Small, self-contained changes     |

## 3. Branching Strategy

All branches must be created as development branches linked to a GitHub Issue.
Exceptions are granted only under explicit instructions from the Maintainer or during emergency merge conflict resolutions.

### 3.1 Naming Convention

Branches must follow the format:

`{issue_number}-{brief-description}`

Examples: `12-user-auth`, `45-fix-header-style`

### 3.2 Branch Rules by Issue Type

- **Epic Branch:** Created from `main` when an Epic Issue is opened. Must only receive merge commits from Task Branches — direct file modifications are prohibited (see Section 2.1 for exceptions).
- **Task Branch:** Created from the parent Epic Branch. Merged back into the Epic Branch via a Task PR.
- **Fast Track Branch:** Created from `main`. Merged directly into `main` via a Fast Track PR.

### 3.3 Merging

All branches must be merged via a Pull Request (PR).
Direct commits to `main` are prohibited.

## 4. Pull Request Workflow

All merges must go through a PR.
Only the Maintainer can approve and merge PRs.

### 4.1 Task PRs

- Must include `Closes #Issue_Number` to automate issue closing.
- Must use `.github/PULL_REQUEST_TEMPLATE/task_pr_template.md`.

### 4.2 Fast Track PRs

- Must include `Closes #Issue_Number`.
- Must use `.github/PULL_REQUEST_TEMPLATE/fast_track_pr_template.md`.

### 4.3 Epic PRs

Epic PRs are created when merging an Epic Branch into `main`.

- Only allowed after all associated Task Issues are completed.
- The Maintainer must verify the Epic before merging.
- Must use `.github/PULL_REQUEST_TEMPLATE/epic_pr_template.md`.

## 5. Commit Policy

- Commit messages must include the Issue number in the format `#ISSUE_NUMBER`.
- Commit messages must reference exactly one Issue.
- Commit messages must be written in English.
- This rule applies to Epic, Task, and Fast Track Issues.
- Commits that do not reference an Issue are prohibited.

**Examples:**

- `#12 Add validation for user input`
- `#45 Fix header alignment issue in navigation bar`
- `#33 Update README with installation steps`
- `#58 Refactor config loader for better readability`
- `#77 Fix typo in CONTRIBUTING.md`

## 6. Language Policy

All project artifacts must be written exclusively in English. This includes:

- Commit messages
- Pull Request titles and descriptions
- Issue titles and descriptions (Epic, Task, Fast Track)
- Documentation, comments, and all repository content

Team communication (e.g., chat discussions) may be conducted in either Japanese or English, depending on participants' preferences.
This flexibility does not affect the requirement that all project deliverables remain in English.
