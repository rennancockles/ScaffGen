python "C:\Python27\Scripts\pyinstaller-script.py" ^
    --log-level WARN ^
    --distpath "dist\win" --workpath "dist\win\build" --specpath "dist\win\spec" ^
    -cFn "ScaffGen" ^
    scaff.spec

rd /S /Q dist\win\build
REM rd /S /Q dist\win\spec