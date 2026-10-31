@echo off
title CoeliSafe 1-Click Live Publisher (Cloudflare Pages + Google Sheet Sync)
echo ========================================================
echo   COELISAFE.COM - CLOUDFLARE PAGES ^& GOOGLE SHEET SYNC
echo ========================================================
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0Sync-And-Publish.ps1"
echo.
pause
