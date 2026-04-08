<p align="center">
    <img width="248" height="250" src="https://raw.githubusercontent.com/CyberBro9/aobp/main/Assets/aobp.ico" alt="AOBP logo which was made in 10 minutes">
</p>

# Аккредитации и Другие Бумаги для Бизнеса

### Инструмент для быстрого и лёгкого добавления текста на изображения по типу сертификатов в больших количества

# Особенности:

* Быстрый импорт изображений и документов
* Обширная поддержка форматов изображений (.png, .jpeg., .bmp and others) и документов (.xlsx, .xls, .ods, .csv и другие)
* Базовые средства кастомизации текста (центрирование, цвет, и т.д.)
* Интуитивный интерфейс

# Как использовать:

1. Выберите шаблон вашего документа.
2. Выберите таблицу из которой будут доставаться добавления (должна быть незащищённой).
3. Выберите любое из добавлений, сгенерированных инструментом (первая строка первой страницы вашего документа) и нажмите "Добавить поле на холст".
4. Перетащите  (it automatically follows your mouse).
5. Click when you are satisfied with the placeholder's position.
6. Repeat steps 3-5 until all fields that you need on the final document are pasted in.
7. Press the "Save images" button, select your destination.
8. While saving, data corresponding to every placeholder will be pulled from your document and applied to the final image in the positions you put them on.
9. Enjoy your created accreditations and other business papers. :)

The complete tutorial for the tool can also be found in it, accessible on program launch.

# Build instructions:

If you want to build the project from scratch, do the following:

1. Clone the project using Git:
```
git clone https://github.com/CyberBro9/aobp.git
cd aobp
```
2. Install the project dependencies:
```
pip install -r requirements.txt
```
3. Install pyinstaller (do not ask why we use that instead of pyside-deploy):
```
pip install pyinstaller
```
4. Run the following command:
```
pyinstaller --onefile --icon=Assets/aobp.ico --hiddenimport pyexcel --hiddenimport pyexcel_io --hiddenimport pyexcel_xls --hiddenimport pyexcel_xlsx --hiddenimport pyexcel_ods --hiddenimport xlrd --hiddenimport xlwt main.py
```
You can also find the following command in buildCommand.txt.
5. Add the Assets folder inside the dist folder (it will appear upon compilation finish).
6. The program should now run.

<p align="center">
    <img width="248" height="250" src="https://raw.githubusercontent.com/CyberBro9/aobp/main/PromImage1.png" alt="AOBP promotional image">
</p>
