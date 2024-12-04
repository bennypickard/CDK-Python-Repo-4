#!/bin/bash



# Check git status
echo "Checking git status..."
git status

# Add all files to the staging area
echo "Adding all changes to staging..."
git add .


# Check git status
echo "Checking git status..."
git status

# Optionally, you can commit as well
# Uncomment the next line to commit after adding
# git commit -m "Your commit message"

echo "All changes have been added to staging."
