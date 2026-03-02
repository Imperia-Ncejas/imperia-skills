#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Repository root: ${REPO_ROOT}"
echo "Update workflow:"
echo "1) Pull latest changes"
echo "2) Review CHANGELOG.md and VERSION"
echo "3) Run tooling/validate_skills.py"
