#!/bin/zsh

FORMAT=$(cd `dirname $0` && pwd)
source ${FORMAT}/formatting.sh

# Get target directory name from command line argument
if [ -z "$1" ]; then
  echo "${RED}Error: Please provide a directory name.${RESET}"
  exit 1
fi

dir="$1"

# Switch to the desired directory
cd "$dir" || { echo "${RED}Error: Directory not found.${RESET}"; exit 1; }
currentRepo=$(pwd | awk -F/ '{print $NF}')
echo "\n${GREEN}Switched to $currentRepo"

# Check if it's a git repository  
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "${RED}Error: $currentRepo is not a git repository.${RESET}"
  exit 1
fi

# Check if the repository has either main or master branch
if git rev-parse --abbrev-ref HEAD | grep -q -E '^\s*[mM]a(?:in|ster)\s*$'; then
  echo "${GREEN}Currently checked out branch is main or master.${RESET}"
elif ! git branch --list | grep -q -E '^\s*[mM]a(?:in|ster)\s*$'; then
  echo "${RED}Error: $currentRepo repository doesn't have main or master branch, skipping check.${RESET}"
  exit 1
fi

# Gather branch information excluding main and master, display branches
targetBranches=$(git branch | grep -v -E '^\s*[mM]a(?:in|ster)\s*$')
echo "$(echo "$targetBranches" | wc -l | xargs) branch(es) in this repository"
echo "${BLUE}$targetBranches ${RESET}"
if [ -z "$targetBranches" ] || [ $(echo "$targetBranches" | wc -l) -le 1 ]; then
  echo "${RED}No valid branches to delete - Exiting.${RESET}"
  exit 0
fi

# Ask for confirmation before deleting branches
echo "\nPreparing to remove branches on $currentRepo"
echo "Are you sure you want to delete these branches? (y/n)"
read -r confirm
if [ "$confirm" != "y" ]; then
  echo "${GREEN}Branch deletion cancelled - Exiting.${RESET}"
  exit 0
# Delete all branches except main and master
else
  echo -n "Waiting" && echo -n "." && sleep 1 && echo -n "." && sleep 1 && echo -n "." && sleep 1 && echo "\n${RESET}"
  echo "$targetBranches" | xargs git branch -D  
fi

echo "${GREEN}Script run on ${1} complete!${RESET}"
