# Documentation for the directory app advertisements

___

Документация к директории [app_advertisements]().

Это приложение отвечает работу сайта, связанную с базой данных (миграции), администрированием сайта, 
показом главной страницы и объявлений, размещением новых объявлений и размещением страниц на сайте: 
Главная, Топ продавцов, Объявление и Разместить объявление.

Настройки подключения и другого находятся в файле [settings.py](..%2Fadvertisements%2Fsettings.py).

___

# Directories & Python Files

## 1. [admin.py](admin.py)

* `class AdvertisementAdmin()` - настройка управления и отображения столбцов в панели администратора - [admin.py](admin.py) `6`
* `list_display` - показ таблицы объявлений из базы данных - [admin.py](admin.py) `9`
* `list_filter` - добавление фильтров просмотра - [admin.py](admin.py) `15`
* `actions` - показ функций "добавление и удаление функции аукциона" у объявлений - [admin.py](admin.py) `19`
* `fieldsets` - добавление списка общей информации и цен (необязательно) - [admin.py](admin.py) `23`
* `make auction as false()` - функция, убирающая возможность аукциона у объявлений - [admin.py](admin.py) `35`
* `make auction as true()` - функция, добавляющая возможность аукциона у объявлений - [admin.py](admin.py) `40`
* `admin.site.register` - регистрация админа сайта "superuser" - [admin.py](admin.py) `45`

## 2. [models.py](models.py)

* `class Advertisement()` - главный класс модели (колоны) базы данных - [models.py](models.py) `17`
* `created date()` - функция изменения стиля показа добавленных объявлений, изменение цвета и формата выведения даты - [models.py](models.py) `86`
* `updated date()` - функция изменения стиля показа обновленных объявлений, изменение цвета и формата выведения даты - [models.py](models.py) `98`
* `show auction()` - функция изменения стиля показа наличия и отсутствия аукциона - [models.py](models.py) `110`
* `show image 1-3()` - функции показа изображений объявлений и изображения отсутствия их - [models.py](models.py) `122-159`
* `show email()` - функция изменения показа почты аккаунта если администратор - [models.py](models.py) `162`
* `show user()` - функция изменения показа аккаунта если администратор - [models.py](models.py) `174`
* `show contact()` - функция изменения показа контактов если администратор - [models.py](models.py) `186`
* `get absolute url()` - настройка абсолютной ссылки для шаблона [advertisement.html](..%2Ftemplates%2Fapp_advertisement%2Fadvertisement.html) - [models.py](models.py) `201`
* `class Meta` - класс для настройки базы данных "Товары" - [models.py](models.py) `207`

## 3. [forms.py](forms.py)

* `class AdvertisementForm()` - класс со всеми формами для POST запроса с размещением объявления - [forms.py](forms.py) `5`
* `class Meta` - класс для шаблона [advertisement-post.html](..%2Ftemplates%2Fapp_advertisement%2Fadvertisement-post.html) с размещением объявления (POST запросом) - [forms.py](forms.py) `7`
* `clean title()` - функция выводящая ошибку если title (заголовок) объявления начинается с "?" - [forms.py](forms.py) `24`

## 4. [urls.py](urls.py)

* `urlpatterns` - настройка синхронизации между ссылками на сайте, шаблонами в директории [app advertisement](..%2Ftemplates%2Fapp_advertisement)[templates](..%2Ftemplates) и классом `class WebViews()` в файле [views.py](views.py) - [urls.py](urls.py) `6`

## 5. [views.py](views.py)

* `class WebViews()` - класс со всеми функциями относящиеся к шаблонам для файла [urls.py](urls.py) и заполнения базы данных [models.py](models.py) - [views.py](views.py) `15`
* `index()` - функция, возвращающая шаблон главной страницы [index.html](..%2Ftemplates%2Fapp_advertisement%2Findex.html); 
   имеет функцию поиска по объявлениям на сайте - [views.py](views.py) `18`
* `top sellers()` - функция, возвращающая шаблон страницы со лучшими продавцами [top-sellers.html](..%2Ftemplates%2Fapp_advertisement%2Ftop-sellers.html); 
   имеет функцию вычисления количество объявлений каждого продавца - [views.py](views.py) `35`
* `advertisement view()` - функция, возвращающая шаблон страницы с самим объявлением [advertisement.html](..%2Ftemplates%2Fapp_advertisement%2Fadvertisement.html); 
   имеет настройку абсолютной ссылки для шаблона - [views.py](views.py) `47` 
* `advertisement post()` - функция, возвращающая шаблон страницы с размещением объявлений [advertisement-post.html](..%2Ftemplates%2Fapp_advertisement%2Fadvertisement-post.html);
   имеет несколько функций - [views.py](views.py) `60`
   - POST запрос, заносящий всю информацию о новом объявлении в базу данных
   - не допускает и переносит не зарегистрированных пользователей на страницу с шаблоном [login.html](..%2Ftemplates%2Fapp_auth%2Flogin.html)
   - сохраняет новое объявление в базе данных [db.sqlite3](..%2F..%2Fdata%2Fdb.sqlite3) через файл со всеми формами [forms.py](forms.py)
   - выводит ошибку и не дает разместить объявлении без внесенных данных в заголовке "title", описании "description", цене "price" - настройка находится в файле [models.py](models.py)
   - выводит ошибку, если заголовок "title" начинается с "?" - настройка находится в файле со всеми формами [forms.py](forms.py)
   - debugging: выводит в консоль закрытого сервера дату, время, пользователя и данные нового размещенного объявления

## 6. [apps.py](apps.py)

* `class AppAdvertisementsConfig()` - класс для изменения названия приложения с базой данных в панели администратора сайта - [apps.py](apps.py) `4`
* `INSTALLED_APP` - обязательно добавить все изменения в файл [settings.py](..%2Fadvertisements%2Fsettings.py) `48` - данное приложение `55` 

## 7. [migrations](migrations)

* директория со всеми миграции данного приложения [app advertisements]()

___

[README.md](..%2F..%2FREADME.md)
