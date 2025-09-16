@echo off
set /p main_title=Input Main Title:
set /p second_title=Input Second Title:
echo Input: %main_title% %second_title%
echo Generating...
python generage_cover.py %main_title% %second_title%
exit