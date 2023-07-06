#!/bin/zsh

# D colours
GREEN=$(tput setaf 2)
BLUE=$(tput setaf 4)
RED=$(tput setaf 1)
RESET=$(tput sgr0)

# Loop through the directories in the current working directory
for dir in */; do
  # Check if the target Adirectory is a git repository
  if [ -d "${dir}/.git" ]; then
    cd "$dir"
    currentRepo=$(pwd | awk -F/ '{print $NF}')
    printf "\n%sSwitched to %s\n" "$GREEN" "$currentRepo"

    # Check if the repository has either main or master branch
    if git branch --list | grep -q -E '^\s*(main|master)\s*$'; then
      echo "$(git branch | wc -l | xargs) branch(e)s in this repository"
      branches=$(git branch) && echo "${BLUE}$branches ${RESET}"
      printf "\nPreparing to run checks on: %s\n" "$currentRepo"
      printf "Waiting" && sleep 1 && printf "." && sleep 1 && printf "." && sleep 1 && printf ".\n"
    else
      printf "%s%s repository doesn't have main or master branch, skipping check.%s\n" "$RED" "$currentRepo" "$RESET"
    fi
    printf "%sCheck on %s done!%s\n" "$BLUE" "$currentRepo" "$RESET"
    printf "%sMoving to next directory...%s\n" "$BLUE" "$RESET"
    cd ..
  else
    printf "%s%s not a git repository.%s\n" "$RED" "$currentRepo" "$RESET"
    cd "$dir"  
  fi
  # printf "%sCheck on %s done!%s\n" "$BLUE" "$currentRepo" "$RESET"
  # printf "%sMoving to next directory...%s\n" "$BLUE" "$RESET"
  # cd ..
done

printf "\n%sAll checks complete.%s\n" "$GREEN" "$RESET"