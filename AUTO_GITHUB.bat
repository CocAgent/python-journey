@echo off
chcp 65001 >nul
setlocal EnableExtensions

title THANH QUY TECH - GITHUB AUTO SYNC

set "SOURCE=K:\Python"
set "WORK=K:\Python_ThanhQuy"
set "REPO=https://github.com/thanhquycoder/python-journey.git"
set "BRANCH=main"
set "DELAY=5"

echo ==========================================
echo       THANH QUY TECH - AUTO GITHUB
echo ==========================================

if not exist "%SOURCE%" (
    echo [ERROR] Khong tim thay thu muc nguon: %SOURCE%
    pause
    exit /b 1
)

if not exist "%WORK%\.git" (
    if exist "%WORK%" (
        echo [ERROR] Thu muc %WORK% da ton tai nhung khong phai Git repository.
        echo Hay xoa thu muc nay roi chay lai.
        pause
        exit /b 1
    )

    echo [1/4] Dang clone nhanh %BRANCH%...
    git clone --branch "%BRANCH%" --single-branch "%REPO%" "%WORK%"

    if errorlevel 1 (
        echo [ERROR] Clone that bai! Kiem tra lai ten nhanh "%BRANCH%" tren GitHub.
        pause
        exit /b 1
    )
)

:LOOP
echo.
echo ==========================================
echo [%date% %time%]
echo Dang sao chep code tu %SOURCE%...

robocopy "%SOURCE%" "%WORK%" /MIR /XD ".git" ".venv" "venv" "__pycache__" /R:1 /W:1 /NFL /NDL /NJH /NJS /NP

if errorlevel 8 (
    echo [ERROR] Sao chep that bai!
    pause
    exit /b 1
)

pushd "%WORK%"

echo [2/4] Kiem tra thay doi...
git add -A
git diff --cached --quiet

if errorlevel 1 (
    echo [3/4] Dang commit...
    git commit -m "Auto sync %date% %time%"

    if errorlevel 1 (
        echo [ERROR] Commit that bai!
        popd
        pause
        exit /b 1
    )

    echo [4/4] Dang dong bo len GitHub [%BRANCH%]...
    git pull --rebase origin "%BRANCH%"
    if errorlevel 1 (
        echo [ERROR] Phat hien xung dot Git. Hay xu ly thu cong trong %WORK%.
        popd
        pause
        exit /b 1
    )

    git push origin "%BRANCH%"
    if errorlevel 1 (
        echo [ERROR] Push that bai!
        popd
        pause
        exit /b 1
    )

    echo [SUCCESS] Da push code len nhanh %BRANCH%!
) else (
    echo [OK] Khong co thay doi moi.
)

popd

echo Cho %DELAY% giay...
timeout /t %DELAY% /nobreak >nul
goto LOOP