# Documentation Fast-Lane Workflow

## When Fast-Lane is Allowed

- **Low-risk documentation or scaffold blocks** only
- **Single approved file** or **one tightly scoped documentation folder**
- **No code behavior changes** - only documentation updates
- **Tests must pass** after changes
- **Only approved files changed** - no unexpected modifications

## When Fast-Lane is Not Allowed

- **Code changes** (any `.py`, `.js`, `.ts` files)
- **Test changes** (any `.py` test files)
- **Architecture changes** (design decisions, structure modifications)
- **Unclear diffs** - changes that are hard to review
- **Failed tests** - any test failures after changes
- **External dependencies** - browser, MCP, APIs, secrets, installs
- **System operations** - delete, reset, clean, force-push commands

## Standard Flow

1. **Check git clean**: `git status -sb`
2. **Edit approved scope only**: Only modify allowed files
3. **Run tests**: `python -m pytest -q`
4. **Inspect diff/status**: `git --no-pager diff --stat` and `git status --short --untracked-files=all`
5. **Commit/push only if all checks pass**: Only proceed with commit if tests pass and changes are clean

## Commit Process

If tests pass, only the approved file changed, and the rule is concise:

```bash
git add .clinerules/doc-fast-lane.md
git --no-pager diff --staged --stat
git commit -m "chore: add documentation fast-lane Cline rule"
git push
git status -sb
git --no-pager log --oneline --max-count=5
```

## Verification

**STOP IMMEDIATELY** if:
- Any file outside the approved scope changes
- Tests fail
- The rule becomes long or too broad
- Staging includes unexpected files
- Commit or push fails

**Only this file is modified or untracked:**
- `.clinerules/doc-fast-lane.md`