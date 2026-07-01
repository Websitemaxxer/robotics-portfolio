#!/usr/bin/env bash
#
# new_project.sh — start a new portfolio project from the reusable template.
#
# Usage:
#   ./scripts/new_project.sh <folder-name> "Display Name"
# Example:
#   ./scripts/new_project.sh 02_line-follower "Line Follower Robot"
#
set -euo pipefail

usage() {
  echo "Usage: ./scripts/new_project.sh <folder-name> \"Display Name\"" >&2
  echo "Example: ./scripts/new_project.sh 02_line-follower \"Line Follower Robot\"" >&2
}

# --- validate arguments ------------------------------------------------------
if [ "$#" -ne 2 ]; then
  echo "Error: expected 2 arguments (folder-name and \"Display Name\"), got $#." >&2
  usage
  exit 1
fi

FOLDER="$1"
DISPLAY="$2"

if [ -z "$FOLDER" ] || [ -z "$DISPLAY" ]; then
  echo "Error: both <folder-name> and \"Display Name\" must be non-empty." >&2
  usage
  exit 1
fi

# --- resolve repo root relative to this script (works from any cwd) ----------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TEMPLATE="$REPO_ROOT/_TEMPLATE_PROJECT"
DEST="$REPO_ROOT/projects/$FOLDER"

if [ ! -d "$TEMPLATE" ]; then
  echo "Error: template folder not found at: $TEMPLATE" >&2
  exit 1
fi

if [ -e "$DEST" ]; then
  echo "Error: projects/$FOLDER already exists. Pick a different folder name." >&2
  exit 1
fi

# --- copy the template -------------------------------------------------------
mkdir -p "$REPO_ROOT/projects"
cp -R "$TEMPLATE" "$DEST"

# --- replace the [PROJECT NAME] placeholder in every .md file ---------------
# Escape characters that are special in a sed replacement (& / \) so display
# names containing them still work. We write .bak files then delete them, which
# is the portable form of in-place sed that works on both GNU (Linux) and BSD
# (macOS) sed.
ESCAPED_DISPLAY="$(printf '%s' "$DISPLAY" | sed -e 's/[&/\]/\\&/g')"
find "$DEST" -type f -name '*.md' -exec sed -i.bak "s/\[PROJECT NAME\]/$ESCAPED_DISPLAY/g" {} +
find "$DEST" -type f -name '*.bak' -delete

# --- done --------------------------------------------------------------------
echo "Created projects/$FOLDER from the template (\"$DISPLAY\")."
echo
echo "Next steps:"
echo "  1. Fill in projects/$FOLDER/README.md (status, dates, hero photo, results)."
echo "  2. Add a row for this project to the top-level README.md Projects table."
echo "  3. Start your build log:  ./scripts/new_entry.sh $FOLDER"
