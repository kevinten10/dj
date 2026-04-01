# MiniMax env template (PowerShell)
# 1) Copy this file to: 13_tools/configs/minimax_env.ps1
# 2) Fill in your key
# 3) Run from repo root:
#    . .\13_tools\configs\minimax_env.ps1

$env:MINIMAX_API_KEY = "PASTE_YOUR_MINIMAX_API_KEY_HERE"

# Optional: API base (the script will append /v1 if needed)
$env:MINIMAX_API_BASE = "https://api.minimax.io"
