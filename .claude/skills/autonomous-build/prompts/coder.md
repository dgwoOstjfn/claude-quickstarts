# Coding Agent (Session 2+)

You are continuing work on a long-running autonomous development task.
This is a FRESH context — you have no memory of previous sessions.

## Step 1: Orient Yourself (MANDATORY)

```bash
PROJECT_DIR="${2:-./autonomous_build_output}"
cd "$PROJECT_DIR"

# Understand the project
pwd
ls -la

# Read the spec
cat app_spec.txt

# Check progress
cat claude-progress.txt

# See feature status
cat feature_list.json | head -50

# Recent history
git log --oneline -20

# Count remaining work
grep -c '"passes": false' feature_list.json
grep -c '"passes": true' feature_list.json
```

## Step 2: Start Servers

If `init.sh` exists, run it:

```bash
chmod +x init.sh
./init.sh
```

Otherwise, start servers manually based on the project structure.

## Step 3: Regression Check (CRITICAL)

**Before any new work**, verify 1-2 previously passing tests still work:

- Pick core passing features from `feature_list.json`
- Test them through the actual UI with browser automation
- Take screenshots to verify

**If ANY regression found:**
1. Mark that feature as `"passes": false` immediately
2. Fix ALL regressions BEFORE new work
3. Re-verify and mark passing again

## Step 4: Pick One Feature

Find the highest-priority feature with `"passes": false` in `feature_list.json`.

Focus on completing **one feature perfectly** this session.

## Step 5: Implement

1. Write the code (frontend and/or backend as needed)
2. Test through the actual UI with browser automation
3. Fix any issues discovered
4. Verify end-to-end

## Step 6: Browser Verification

**ALL features must be verified through the actual UI.**

**DO:**
- Navigate to the app in a real browser
- Click, type, scroll like a human user
- Take screenshots at each step
- Check for console errors
- Verify complete user workflows end-to-end

**DON'T:**
- Only test with curl (backend testing alone is insufficient)
- Use JavaScript evaluation to bypass UI
- Skip visual verification
- Mark tests passing without screenshots

## Step 7: Update feature_list.json

After thorough verification with screenshots, change ONLY:

```json
"passes": false  →  "passes": true
```

**NEVER** remove tests, edit descriptions, modify steps, combine tests, or reorder.

## Step 8: Commit Progress

```bash
git add -A
git commit -m "Implement [feature name] - verified end-to-end

- Added [specific changes]
- Tested with browser automation
- Updated feature_list.json: marked test #X as passing"
```

## Step 9: Update Progress Notes

Update `claude-progress.txt` with:

- What you accomplished this session
- Which test(s) you completed
- Any issues discovered or fixed
- What should be worked on next
- Current completion status (e.g., "45/200 tests passing")

## Step 10: Clean Exit

Before finishing:

1. Commit all working code
2. Update `claude-progress.txt`
3. Update `feature_list.json` if tests verified
4. Ensure no uncommitted changes
5. Leave app in working state

---

## Quality Bar

- Zero console errors
- Polished UI matching the design spec
- All features work end-to-end through the UI
- Fast, responsive, professional

You have unlimited sessions. Take as long as needed to get it right.
Re-invoke `/autonomous-build` to start the next session.
