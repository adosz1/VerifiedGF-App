$ErrorActionPreference = "Stop"
$dir = Split-Path -Parent $MyInvocation.MyCommand.Path
$sheetUrl = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSmPzTCJkAdZTSjosvyQK-j3RhZ_nBlTkAKTOyKmz3UNkq2wSo0cLubtRZlKqU2l0n0Qc-HRmsXuPT2/pub?output=csv&t=" + [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
$csvFile = Join-Path $dir "coelisafe-google-sheet-template.csv"
$bt = [char]96

try {
  Write-Host "1. Syncing latest rows from your Google Sheet..." -ForegroundColor Cyan
  Invoke-WebRequest -Uri $sheetUrl -OutFile $csvFile -UseBasicParsing -Headers @{ "Cache-Control" = "no-cache" }
  $rawCsv = [System.IO.File]::ReadAllText($csvFile, [System.Text.Encoding]::UTF8).Trim().Replace([string]$bt, "'")
  $pattern = "(?s)var COELISAFE_EMBEDDED_CSV = " + $bt + ".*?" + $bt + ";"
  $replacement = "var COELISAFE_EMBEDDED_CSV = " + $bt + $rawCsv + $bt + ";"

  $idxPath = Join-Path $dir "index.html"
  if (Test-Path $idxPath) {
    $c = [System.IO.File]::ReadAllText($idxPath, [System.Text.Encoding]::UTF8)
    $updated = [regex]::Replace($c, $pattern, $replacement)
    [System.IO.File]::WriteAllText($idxPath, $updated, (New-Object System.Text.UTF8Encoding($false)))
  }

  $chatPath = "C:\Users\kovia\.gemini\antigravity\brain\3adaafdb-e0af-4a64-a056-3893d3825ecf\verifiedgf.html"
  if (Test-Path $chatPath) {
    $c2 = [System.IO.File]::ReadAllText($chatPath, [System.Text.Encoding]::UTF8)
    $updated2 = [regex]::Replace($c2, $pattern, $replacement)
    [System.IO.File]::WriteAllText($chatPath, $updated2, (New-Object System.Text.UTF8Encoding($false)))
  }

  $rowCount = ($rawCsv -split "\r?\n").Count - 1
  Write-Host ("   -> Synced " + $rowCount + " Google Sheet restaurant(s) into index.html & Chat Preview!") -ForegroundColor Green
} catch {
  Write-Host ("   -> Google Sheet sync warning: " + $_.Exception.Message) -ForegroundColor Yellow
}

$cfZip = "C:\Users\kovia\Desktop\CoeliSafe-Cloudflare-Deploy.zip"
if (Test-Path $cfZip) { Remove-Item $cfZip -Force }
Compress-Archive -Path (Join-Path $dir "index.html"), (Join-Path $dir "_redirects") -DestinationPath $cfZip -Force

$desktopBackup = "C:\Users\kovia\Desktop\CoeliSafe-Master-Backup.zip"
Copy-Item $cfZip $desktopBackup -Force
$oneDriveDir = "C:\Users\kovia\OneDrive"
if (Test-Path $oneDriveDir) {
  Copy-Item $cfZip (Join-Path $oneDriveDir "CoeliSafe-Master-Backup.zip") -Force
}

Write-Host "2. Built Desktop\CoeliSafe-Cloudflare-Deploy.zip & Master Backup (0 Credits Used!)" -ForegroundColor Green
Write-Host "3. Opening Cloudflare Pages Upload Screen..." -ForegroundColor Yellow
Start-Process "https://dash.cloudflare.com/61f0e859be9e994822a6cd9c27f4b4f5/pages/view/coelisafe-app"
Write-Host "   -> Click 'Create new deployment' on Cloudflare and drop VerifiedGF-App (or CoeliSafe-Cloudflare-Deploy.zip)!" -ForegroundColor Cyan
