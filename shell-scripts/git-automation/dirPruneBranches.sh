#!/bin/zsh

# Define colors
BLUE="\033[0;34m"
GREEN="\033[0;32m"
RED="\033[0;31m"
RESET="\033[0m"

# Loop through the directories in the current working directory
for dir in */; do
  # Switch to the repository directory
  cd "$dir"

  # Check if the repository has either main or master branch
  if git branch --list main || git branch --list master; then
    currentRepo=$(pwd | awk -F/ '{print $NF}')
    echo "\n${GREEN}Switched to $currentRepo "
    echo "$(git branch | wc -l | xargs) branch(e)s in this repository"
    branches=$(git branch) && echo "${BLUE}$branches ${RESET}"
    echo "\nPreparing to check $currentRepo for branches"
    echo -n "Waiting" && echo -n "." && sleep 1.5 && echo -n "." && sleep 1.5 && echo -n ".\n"

    # Wipe out all local non master/main branches
    git branch | grep -v "master\|main" | xargs git branch -d

   echo "\n${BLUE}Check on $currentRepo done!${RESET}"
   echo "${BLUE}Moving to next directory...${RESET}"
  else
    echo "\n${RED}$currentRepo repository doesn't have main or master branch, skipping check.${RESET}"
  fi 
  cd ..
done

echo "${GREEN}All deletions complete.${RESET}"
