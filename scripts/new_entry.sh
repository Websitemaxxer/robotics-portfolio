#!/usr/bin/env bash
#
# new_entry.sh — insert a fresh, dated entry at the TOP of a project's build diary.
#
# Usage:
#   ./scripts/new_entry.sh <folder-name>
# Example:
#   ./scripts/new_entry.sh 01_arduino-starter-kit
#
# The new entry is inserted immediately AFTER the first "---" line in the diary,
# so it sits below the intro but above all older entries (newest-first).
#
set -euo pipefail

usage() {
  echo "Usage: ./scripts/new_entry.sh <folder-name>" >&2
  echo "Example: ./scripts/new_entry.sh 01_arduino-starter-kit" >&2
}

# --- validate arguments ------------------------------------------------------
if [ "$#" -ne 1 ]; then
  echo "Error: expected 1 argument (folder-name), got $#." >&2
  usage
  exit 1
fi

FOLDER="$1"

# --- resolve repo root relative to this script (works from any cwd) ----------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DIARY="$REPO_ROOT/projects/$FOLDER/01_planning/BUILD_DIARY.md"

if [ ! -f "$DIARY" ]; then
  echo "Error: build diary not found at: $DIARY" >&2
  echo "Check the folder name. Projects that exist:" >&2
  if [ -d "$REPO_ROOT/projects" ]; then
    ls -1 "$REPO_ROOT/projects" 2>/dev/null | sed 's/^/  - /' >&2 || true
  else
    echo "  (no projects/ folder yet — create one with new_project.sh)" >&2
  fi
  exit 1
fi

TODAY="$(date +%Y-%m-%d)"

# --- find the first "---" separator line ------------------------------------
SEP_LINE="$(grep -n '^---[[:space:]]*$' "$DIARY" | head -n 1 | cut -d: -f1)"
if [ -z "${SEP_LINE:-}" ]; then
  echo "Error: no '---' separator line found in $DIARY;" >&2
  echo "cannot tell where the intro ends and entries begin." >&2
  exit 1
fi

# --- rebuild the file: intro (through ---), new entry, then older entries ----
TMP="$(mktemp)"
{
  head -n "$SEP_LINE" "$DIARY"
  printf '\n## %s — <what this session was about>\n\n' "$TODAY"
  printf '%s\n' '- **Time spent:** '
  printf '%s\n' '- **Goal today:** '
  printf '%s\n' '- **What I did:** '
  printf '%s\n' '- **What worked:** '
  printf '%s\n' '- **What failed / surprised me:** '
  printf '%s\n' '- **What I changed because of it:** '
  printf '%s\n' '- **Next step:** '
  printf '%s\n' '- **Photos:** (add images to 05_media/photos/ and link them here)'
  tail -n +"$((SEP_LINE + 1))" "$DIARY"
} > "$TMP"
mv "$TMP" "$DIARY"

echo "Added a new entry dated $TODAY to:"
echo "  $DIARY"
echo "Open it and fill in the fields for today's session."
