# Contributing Guidelines

This document defines the development workflow using GitHub for this project.

## 1. Roles
**Maintainer:**  
The user with final decision-making authority.  
AI agents shall interpret *“Maintainer”* as *“the User.”*

## 2. Branching Strategy
All branches must be created as development branches linked to a GitHub Issue.  
Exceptions are granted only under explicit instructions from the Maintainer or during emergency merge conflict resolutions.

### 2.1 Naming Convention
Branches must follow the format:

`{issue_number}-{brief-description}`

Examples:
`12-user-auth`
`45-fix-header-style`

### 2.2 Merging
All branches must be merged via a Pull Request (PR).
Direct commits to `main` are prohibited.

## 3. Issue Management
Every Issue must be categorized as one of the following:

- **Epic**
- **Task** (linked to an Epic)
- **Fast Track** (a lightweight Task that does *not* require an Epic)

Epic is the foundation of the workflow.  
Fast Track exists as a controlled exception for small, isolated work items.

### 3.1 Epic Issues
Epic Issues represent large, multi-step units of work.

Must use `.github/ISSUE_TEMPLATE/epic_template.md`.
- **Label:** `epic`
- **Branch:** Create a corresponding Epic Branch using the naming convention.
- **Rules:**  
  - Files must *not* be modified directly on the Epic Branch.  
  - The Epic Branch should only receive merge commits from Task Branches.
  - **Exceptions:**  
    - Minor metadata fixes (e.g., labels, README typos)  
    - Urgent fixes explicitly authorized by the Maintainer

### 3.2 Task Issues
Task Issues represent work items that belong to a specific Epic.

Must use `.github/ISSUE_TEMPLATE/task_template.md`.
- **Reference:** Must include `ref: #Epic_Number`
- **Labels:** One of  
  `feature`, `bug`, `docs`, `refactor`, `chore`
- **Branch:** Create a Task Branch linked to the Task Issue.

### 3.3 Fast Track Issues (Epic-less Lightweight Tasks)
Fast Track Issues are a special category for small, isolated changes that do not justify creating an Epic.  
They exist as an exception to the Epic-first workflow.

#### Allowed Scope
A Fast Track Issue must satisfy **all** of the following:

- No changes to application logic or behavior
- No impact on specifications, architecture, or dependencies
- Expected to be completed within **30–60 minutes**

#### Rules
Must use `.github/PULL_REQUEST_TEMPLATE/fast_track_pr_template.md`.
- **Label:** `fast-track` (mandatory), `feature`, `bug`, `docs`, `refactor`, `chore` (optional)
- **Reference:** No Epic reference required
- **Branch:** Same naming convention as other Issues
- **PR:** Must still be reviewed and approved by the Maintainer

Fast Track provides a streamlined path for trivial work while preserving the integrity of the Epic–Task hierarchy.

## 4. Pull Request Workflow
All merges must go through a PR.

### 4.1 Task PRs
- Only the Maintainer can approve and merge Task PRs.
- Must include `Closes #Issue_Number` to automate issue closing.
- Must use `.github/PULL_REQUEST_TEMPLATE/task_pr_template.md`.

### 4.2 Fast Track PRs
- Same rules as Task PRs.
- Must include `Closes #Issue_Number`.
- Must use `.github/PULL_REQUEST_TEMPLATE/fast_track_pr_template.md`.

### 4.3 Epic PRs
Epic PRs are created when merging an Epic Branch into `main`.

- Only allowed after all associated Task Issues are completed.
- The Maintainer must verify the Epic before merging.
- Must use `.github/PULL_REQUEST_TEMPLATE/epic_pr_template.md`.

## 5. Language Policy
All project artifacts must be written exclusively in English. This includes:

- Commit messages
- Pull Request titles and descriptions
- Issue titles and descriptions (Epic, Task, Fast Track)  
- Documentation, comments, and all repository content

Team communication (e.g., chat discussions) may be conducted in either Japanese or English, depending on participants’ preferences.  
This flexibility does not affect the requirement that all project deliverables remain in English.

## 6. Summary of Issue Types

| Type          | Requires Epic | Labels                                        | Typical Use Case |
|---------------|---------------|-----------------------------------------------|------------------|
| **Epic**      | —             | `epic`                                        | Large features or multi-step work |
| **Task**      | Yes           | `feature`, `bug`, `docs`, `refactor`, `chore` | Work belonging to an Epic |
| **Fast Track**| No            | `fast-track`                                  | Small, isolated changes |

## 7. Commit Policy
- Commit messages must include the Issue number in the format `#ISSUE_NUMBER`.
- Commit messages must reference exactly one Issue.
- Commit messages must be written in English.
- This rule applies to Epic, Task, and Fast Track Issues.
- Commits that do not reference an Issue are prohibited.
**Example:**
- #12 Add validation for user input
- #45 Fix header alignment issue in navigation bar
- #33 Update README with installation steps
- #58 Refactor config loader for better readability
- #77 Fix typo in CONTRIBUTING.md

## 8. AI Agent Operational Rules
AI agents must not directly create Issues or Pull Requests on GitHub.

When creating an Issue or Pull Request, the AI must:
1. Generate a shell script under `tmp/` with an appropriate filename.
2. The script must contain the necessary GitHub CLI commands to create the Issue or PR.
3. The Maintainer will review and execute the script.
