#!/usr/bin/env bash
# Run after creating an empty private repo: https://github.com/new
# Name: AI_ML_Ops | Visibility: Private | Do NOT add README

set -euo pipefail

OWNER="${1:-RohitJishtu}"
REPO="AI_ML_Ops"
BRANCH="${2:-main}"

echo "Configuring remote for ${OWNER}/${REPO}..."
git remote set-url origin "https://github.com/${OWNER}/${REPO}.git"

echo "Pushing to ${BRANCH}..."
git push -u origin HEAD:"${BRANCH}"

echo "Done. Repository: https://github.com/${OWNER}/${REPO}"
