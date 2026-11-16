
@echo off
chcp 65001 >nul
title THANH QUY TECH - AUTO GITHUB SYNC
color 0B

cd /d "%~dp0"

echo ==========================================
echo       THANH QUY TECH - GITHUB AUTO
echo ==========================================
echo.

where git >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git chua duoc cai dat!
    pause
    exit /b
)

if not exist ".git" (
    echo [ERROR] Thu muc nay chua duoc khoi tao Git!
    pause
    exit /b
)

:LOOP
echo.
echo [%date% %time%] Dang dong bo...

if exist ".git\MERGE_HEAD" (
    echo [ERROR] Ban dang co merge chua hoan tat.
    echo Hay xu ly merge truoc khi chay lai file BAT.
    pause
    exit /b
)

if exist ".git\rebase-merge" (
    echo [ERROR] Dang co rebase chua hoan tat.
    pause
    exit /b
)

git pull --rebase --autostash origin main
if errorlevel 1 goto ERROR

git add -A

git diff --cached --quiet
if errorlevel 1 (
    echo [INFO] Phat hien thay doi, dang commit...
    git commit --allow-empty-message -m ""
    if errorlevel 1 goto ERROR

    echo [INFO] Dang upload len GitHub...
    git push origin main
    if errorlevel 1 goto ERROR

    echo [SUCCESS] Da dong bo GitHub!
) else (
    echo [INFO] Khong co thay doi.
)

echo.
echo [WAIT] Cho 30 giay de dong bo tiep...
timeout /t 30 /nobreak >nul
goto LOOP

:ERROR
echo.
echo [ERROR] Dong bo that bai!
echo Hay kiem tra ket noi, conflict hoac quyen truy cap GitHub.
echo.
pause
exit /b
