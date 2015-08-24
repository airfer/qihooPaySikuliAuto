:: * the script of the run qihooPaySikuliAuto,if you want to 
:: * run this script, please repalace the source_path with your
:: * own directory
:: * @author: wangyukun-xy airong's home
:: * @email: wangyukun-xy@360.cn airfer@126.com

@echo off
setlocal enabledelayedexpansion

set SIKULI_PATH=E:\Github\qihooPaySikuliAuto\sikuli
set SOURCE_PATH=E:\Github\qihooPaySikuliAuto\data

:: set runscript and the soucedata file
set RUN_SCRIPT=%SIKULI_PATH%\runScript.cmd
set RECHARGE=%SOURCE_PATH%\Recharge\recharge.sikuli
set WITHDRAW=%SOURCE_PATH%\Withdraw\withdraw.sikuli
set CHANGE_PASSWORD=%SOURCE_PATH%\ChangePassword\changePassword.sikuli
set MY_BANKCARD=%SOURCE_PATH%\MyBankcard\myBankcard.sikuli

echo %SOURCE_PATH%
echo %RUN_SCRIPT%
echo %RECHARGE%
::call %RUN_SCRIPT% -c -r %RECHARGE%
::call %RUN_SCRIPT% -c -r %WITHDRAW%

call %RUN_SCRIPT% -c -r %CHANGE_PASSWORD%

::call %RUN_SCRIPT% -c -r %MY_BANKCARD%
