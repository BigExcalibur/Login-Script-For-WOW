@echo off

echo -----����ű�-----
echo.
echo ���价����...
echo.


echo ��װopencv...
pip install opencv-python
echo.

echo ��װPIL...
pip install Pillow
echo.

echo ��װpywin32...
pip install pywin32
echo.

echo ��װpyHook...
pip install pyHook
echo.

echo ��װnumpy...
pip install numpy
echo.

echo ��װPyUserInput...
pip install PyUserInput
echo.

cls

echo ������ɣ���ʼ����...
echo.

python login_script.py

pause