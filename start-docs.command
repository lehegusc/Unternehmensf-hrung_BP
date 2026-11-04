#!/bin/bash
# =============================================
#  BP Analyse Docs
#  Double-click this file to start the wiki.
#  Close this Terminal window to stop it.
# =============================================

# Derive paths from this script's location (works on any Mac)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SERVER="$SCRIPT_DIR/_docs-site/server.py"

echo ""
echo "  Starting BP Analyse Docs..."
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "  Error: python3 is not installed."
    echo "  Install it from python.org or via Homebrew: brew install python3"
    echo ""
    read -p "  Press Enter to close..."
    exit 1
fi

# Check server script
if [ ! -f "$SERVER" ]; then
    echo "  Error: server.py not found at $SERVER"
    echo ""
    read -p "  Press Enter to close..."
    exit 1
fi

# Open browser after a short delay
(sleep 1.5 && open "http://localhost:8000") &

# Run server
python3 "$SERVER"
