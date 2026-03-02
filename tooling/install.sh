#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Repository root: ${REPO_ROOT}"
echo "No external dependencies to install yet."
echo "Run tooling/validate_skills.py to verify skill structure."
