@echo off


echo 安装环境中...
echo.


echo 安装opencv...
pip install opencv_python-4.1.1.26-cp37-cp37m-win_amd64.whl
echo.

echo 安装PIL...
pip install Pillow-6.2.1-cp37-cp37m-win_amd64.whl
echo.

echo 安装pywin32...
pip install pywin32-227-cp37-cp37m-win_amd64.whl
echo.

echo 安装pyHook...
pip install pyHook-1.5.1-cp37-cp37m-win_amd64.whl
echo.

echo 安装numpy...
pip install numpy-1.17.4-cp37-cp37m-win_amd64.whl
echo.

echo 安装PyUserInput...
pip install PyUserInput
echo.

cls

echo 环境安装完成，请启动start.bat开始挂机...
echo.

pause