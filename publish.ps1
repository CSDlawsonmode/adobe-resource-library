# Rebuild the pages and push them to GitHub Pages.
# Usage (from this folder):   .\publish.ps1
#    or with a message:       .\publish.ps1 "Added Photoshop logo"
param([string]$Message = "Update site")

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

python model/make_theme_assets.py
python model/module-1-getting-started/make_pages.py
python model/module-2-photoshop/make_pages.py
python model/check_canvas.py
if ($LASTEXITCODE -ne 0) { Write-Host "Canvas check failed; nothing was pushed." -ForegroundColor Red; exit 1 }
python model/build_preview.py

git add -A
git diff --cached --quiet
if ($LASTEXITCODE -eq 0) { Write-Host "No changes to publish." -ForegroundColor Yellow; exit 0 }

git commit -m $Message
git push
Write-Host ""
Write-Host "Pushed.  The site updates in about a minute:" -ForegroundColor Green
Write-Host "https://csdlawsonmode.github.io/adobe-resource-library/"
