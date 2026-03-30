# Initializer Agent (Session 1)

You are the FIRST agent in a long-running autonomous development process.
Your job is to set up the foundation for all future coding sessions.

**All files are created in the current working directory (CWD).**

## Step 1: Read the Specification

Read the spec file provided as `$ARGUMENTS`. This contains the complete
requirements for the application you will build. Study it carefully.

If no spec file argument was provided, stop and ask the user for one.

Then **copy it into CWD** as `app_spec.txt` so future sessions can always find it:

```bash
cp "$ARGUMENTS" ./app_spec.txt
```

## Step 2: Create feature_list.json

Based on the spec, create `feature_list.json` in CWD with **200 detailed
end-to-end test cases**. This file is the single source of truth for what
needs to be built.

**Format:**

```json
[
  {
    "category": "functional",
    "description": "Brief description of the feature and what this test verifies",
    "steps": [
      "Step 1: Navigate to relevant page",
      "Step 2: Perform action",
      "Step 3: Verify expected result"
    ],
    "passes": false
  },
  {
    "category": "style",
    "description": "Brief description of UI/UX requirement",
    "steps": [
      "Step 1: Navigate to page",
      "Step 2: Take screenshot",
      "Step 3: Verify visual requirements"
    ],
    "passes": false
  }
]
```

**Requirements:**

- Minimum **200 features** total with testing steps for each
- Both `"functional"` and `"style"` categories
- Mix of narrow tests (2-5 steps) and comprehensive tests (10+ steps)
- At least **25 tests MUST have 10+ steps** each
- Order features by priority: fundamental features first
- ALL tests start with `"passes": false`
- Cover every feature in the spec exhaustively

**CRITICAL:** It is CATASTROPHIC to remove or edit features in future sessions.
Features can ONLY be marked as passing. Never remove, edit descriptions, or modify steps.

## Step 3: Create init.sh

Create `init.sh` in CWD that:

1. Installs required dependencies
2. Starts necessary servers/services
3. Prints information about how to access the running application

Base the script on the technology stack in the spec.

## Step 4: Initialize Git

```bash
git init
git add app_spec.txt feature_list.json init.sh
git commit -m "Initial setup: app_spec.txt, feature_list.json, and init.sh"
```

## Step 5: Create Project Structure

Set up the project skeleton based on the spec (directories for frontend,
backend, configs, etc.).

## Step 6 (Optional): Start Implementation

If you have capacity remaining, begin implementing the highest-priority
features from feature_list.json. Remember:

- Work on ONE feature at a time
- Test thoroughly before marking `"passes": true`
- Commit progress before finishing

## Ending This Session

Before finishing:

1. Commit all work with descriptive messages
2. Create `claude-progress.txt` summarizing what you accomplished
3. Ensure feature_list.json is complete and saved
4. Verify `app_spec.txt` exists in CWD
5. Leave the environment in a clean, working state

The next `/autonomous-build` invocation will continue from here.
