#!/bin/zsh

# Define colors
BLUE="\033[0;34m"
GREEN="\033[0;32m"
RED="\033[0;31m"
RESET="\033[0m"

# Get a count of the number of folders in current working directory
# folderCount=$(ls -d */ | wc -l)
# echo "${BLUE}Let's go${RESET}"
# echo "${GREEN}$folderCount Repositories to be checked${RESET}"

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
    echo "\nPreparing to check $currentRepo for updates"
    echo -n "Waiting" && echo -n "." && sleep 1.5 && echo -n "." && sleep 1.5 && echo -n ".\n"

    # Check if there are uncommitted changes and stash them
    if [ -n "$(git status --porcelain)" ]; then
      git stash # push -m "Stashing uncommitted changes before switching to master branch"
    fi

    # Checkout the main or master branch respectively and perform a pull
    if git branch --list main; then
      git checkout main
      git pull
    elif git branch --list master; then
      git checkout master
      git pull -q
    fi

    # Pop stashed changes if there were any
    if [ -n "$(git stash list)" ]; then
      git stash pop
    fi

   echo "\n${BLUE}Updates on $currentRepo main/master done!${RESET}"
   echo "${BLUE}Moving to next directory...${RESET}"
  else
    echo "\n${RED}$currentRepo repository doesn't have main or master branch, skipping check.${RESET}"
  fi
  cd ..
done
echo "${GREEN}All checks complete.${RESET}"
