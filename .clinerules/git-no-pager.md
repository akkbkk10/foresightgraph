# Git No-Pager Policy

Do not run Git commands that can open an interactive pager.

## Use these commands instead:
- `git --no-pager diff --stat`
- `git --no-pager diff`
- `git --no-pager log --oneline --max-count=5`
- `git --no-pager show --stat`

## Avoid these commands:
- `git diff`
- `git log`
- `git show`

## If a Git pager opens and the terminal shows "(END)", stop and ask the user to press "q".