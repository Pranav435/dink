@echo off

:: Define target directories
set LOCAL_DIR=%LOCALAPPDATA%\Dink
set SYSTEM32_DIR=C:\Windows\System32

:: Create the directory for the sound file if it doesn't exist
if not exist "%LOCAL_DIR%" (
    mkdir "%LOCAL_DIR%"
    echo Created directory: %LOCAL_DIR%
)

:: Copy notification.wav to the AppData\Local\Dink folder
copy "%~dp0notification.wav" "%LOCAL_DIR%" /Y
if %errorlevel%==0 (
    echo Successfully copied notification.wav to %LOCAL_DIR%.
) else (
    echo Failed to copy notification.wav. Please ensure the file exists and you have permission.
)

:: Copy dink.exe to System32
copy "%~dp0dink.exe" "%SYSTEM32_DIR%" /Y
if %errorlevel%==0 (
    echo Successfully copied dink.exe to %SYSTEM32_DIR%.
) else (
    echo Failed to copy dink.exe. Please ensure you are running this script as an administrator.
)

pause
