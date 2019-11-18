@echo off

echo -----处理脚本-----
echo.
echo 补充环境中...
echo.


echo 安装opencv...
pip install opencv-python
echo.

echo 安装PIL...
pip install Pillow
echo.

echo 安装pywin32...
pip install pywin32
echo.

echo 安装pyHook...
pip install pyHook
echo.

echo 安装numpy...
pip install numpy
echo.

echo 安装PyUserInput...
pip install PyUserInput
echo.

cls

echo 环境完成，开始处理...
echo.

python login_script.py

pause