
@REM call %~dp0\ecom\Scripts\activate.bat
pytest -v -m "regression"  --html=Reports/report.html testCase/test_login.py --browser chrome
@REM pytest -v -m "sanity"  --html=Reports/report.html testCase/ --browser chrome