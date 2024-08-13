# Documentation for the directory app auth

___

Документация к директории [app_auth]().

Это приложение отвечает работу сайта, связанную с базой данных (миграции), 
регистрацией и входом в аккаунт, размещением страниц на сайте: 
Регистрация, Вход, Профиль и Выход.

Настройки подключения и другого находятся в файле [settings.py](..%2Fadvertisements%2Fsettings.py).

___

# Directories & Python Files

## 1. [forms.py](forms.py)

* `class MyUserCreationForm()` - класс со всеми формами для POST запроса регистрации пользователя - [forms.py](forms.py) `8`
* `class Meta` - класс для шаблона [register.html](..%2Ftemplates%2Fapp_auth%2Fregister.html) с регистрацией новых пользователей (POST запрос) - [views.py](views.py) `30`

## 2. [urls.py](urls.py)

* `urlpatterns` - настройка синхронизации между ссылками на сайте, шаблонами в директории [app auth](..%2Ftemplates%2Fapp_auth) и классом `class WebViews()` в файле [views.py](views.py) - [urls.py](urls.py) `6`

## 3. [views.py](views.py)

* `class WebViews()` - класс со всеми функциями относящиеся к шаблонам для файла [urls.py](urls.py) и заполнения базы данных [models.py](..%2Fapp_advertisements%2Fmodels.py) - [views.py](views.py) `14`
* `profile view()` - функция, возвращающая шаблон страницы профиля пользователя [profile.html](..%2Ftemplates%2Fapp_auth%2Fprofile.html) - [views.py](views.py) `18`
* `logout view()` - функция, отвечающая за выход пользователя из своего аккаунта - [views.py](views.py) `58`
* `login view()` - функция, возвращающая шаблон страницы входа пользователя в свой аккаунт [login.html](..%2Ftemplates%2Fapp_auth%2Flogin.html);
   имеет несколько функций - [views.py](views.py) `24`
   - запрашивающая у пользователя "username" и "password" для входа в свой аккаунт POST запросом
   - проводит проверку соответствия с базой данных
   - выводит ошибку при неверных введенных данных "username" или "password" или не зарегистрированному пользователю
   - debugging: выводит в консоль закрытого сервера дату, время и данные вошедшего пользователя в свой аккаунт для проверки без записи в базу данных - [views.py](views.py) `41`
   - открывается данная страница, если не зарегистрированный пользователь откроет страницу с размещением нового объявления [advertisement-post.html](..%2Ftemplates%2Fapp_advertisement%2Fadvertisement-post.html)
   - после прохождения входа пользователя в свой аккаунт перекидывает на страницу профиля пользователя [profile.html](..%2Ftemplates%2Fapp_auth%2Fprofile.html)
* `register wiew()` - функция, возвращающая шаблон с регистрацией нового пользователя в базу данных [register.html](..%2Ftemplates%2Fapp_auth%2Fregister.html); имеет несколько функций - [views.py](views.py) `68`
   - POST запрос, запрашивающий у пользователя "username", "email", "password1", "first name", "last name", "password2" для регистрации в базе данных
   - все формы шаблона страницы [register.html](..%2Ftemplates%2Fapp_auth%2Fregister.html) находятся в файле [forms.py](forms.py)
   - сохраняет нового пользователя
   - выводит ошибки в случаях: 
      - если пользователь с таким же "username" уже зарегистрирован; 
      - в "email" отсутствуют "@" и ".com/ru/org/net" и другие, связанные с почтой;
      - если пароль слабо защищенный, совпадает с именем, не имеет доп знаков;
      - если "password1" и "password2" (Password confirmation) не совпадают;
   - debugging: выводит в консоль закрытого сервера дату, время и данные нового зарегистрировавшегося пользователя - [views.py](views.py) `80`
   - после прохождения регистрации перекидывает на страницу профиля пользователя [profile.html](..%2Ftemplates%2Fapp_auth%2Fprofile.html)

## 4. [apps.py](apps.py)

* `class AppAuthConfig()` - класс для изменения названия приложения в панели администратора сайта - [apps.py](apps.py) `4`
* `INSTALLED_APP` - обязательно добавить все изменения в файл [settings.py](..%2Fadvertisements%2Fsettings.py) `48` - данное приложение `56` 

___

[README.md](..%2F..%2FREADME.md)
