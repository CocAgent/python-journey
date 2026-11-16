
@echo off
chcp 65001 >nul
setlocal EnableExtensions

title THANH QUY TECH - GITHUB AUTO SYNC

set "SOURCE=K:\Python"
set "WORK=K:\Python_ThanhQuy"
set "REPO=https://github.com/thanhquycoder/python-journey.git"
set "BRANCH=ThanhQuy"
set "DELAY=5"

echo ==========================================
echo       THANH QUY TECH - AUTO GITHUB
echo ==========================================

if not exist "%SOURCE%\.git" (
    echo [ERROR] Khong tim thay repository goc!
    pause
    exit /b 1
)

if not exist "%WORK%\.git" (
    if exist "%WORK%" (
        echo [ERROR] Thu muc K:\Python_ThanhQuy da ton tai
        echo nhung khong phai Git repository.
        pause
        exit /b 1
    )

    echo [1/4] Dang clone branch %BRANCH%...

    git clone --branch "%BRANCH%" --single-branch "%REPO%" "%WORK%"

    if errorlevel 1 (
        echo [ERROR] Clone that bai!
        pause
        exit /b 1
    )
)

:LOOP

echo.
echo ==========================================
echo [%date% %time%]
echo Dang sao chep code...

robocopy "%SOURCE%" "%WORK%" /E /XD "%SOURCE%\.git" "%SOURCE%\.venv" "%SOURCE%\venv" /R:1 /W:1 /NFL /NDL /NJH /NJS /NP

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

    git commit --allow-empty-message -m ""

    if errorlevel 1 (
        echo [ERROR] Commit that bai!
        popd
        pause
        exit /b 1
    )
) else (
    echo [OK] Khong co thay doi moi.
)

echo [4/4] Dang dong bo GitHub...

git pull --rebase origin "%BRANCH%"

if errorlevel 1 (
    echo [ERROR] Phat hien xung dot Git.
    echo Hay xu ly thu cong trong %WORK%.
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

echo [SUCCESS] Dong bo hoan tat!

popd

echo Cho %DELAY% giay...
timeout /t %DELAY% /nobreak >nul

goto LOOP
