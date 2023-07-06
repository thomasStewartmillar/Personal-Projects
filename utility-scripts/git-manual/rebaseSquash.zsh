#!/bin/zsh

rebaseSquash() {
  # Rebase and squash the commits
  git rebase -i $targetCommit

  # Remove commit messages from non-target commits
  git filter-branch --msg-filter 'if [ "$GIT_COMMIT" != "$targetCommit" ]; then echo ""; else cat; fi' -- --all

  # Rewrite commit messages for the target commit
  git commit --amend
}

# Get the target commit from the command line argument
targetCommit="$1"

# Check if the target commit is provided
if [ -z "$targetCommit" ]; then
  echo "Please provide the base commit as an argument."
  exit 1
fi

# Call the function to perform the rebase, remove commit messages, and rewrite the target commit message
rebaseSquash
