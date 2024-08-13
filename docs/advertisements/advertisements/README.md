# Documentation for the directory advertisement

___

Документация к директории [advertisements]().

Это основное коренное приложение всего проекта на фреймворки [Django](https://www.djangoproject.com).
Отвечает за подключение новых приложений, ссылок и всего остального.

Настройки подключения и другого находятся в файле [settings.py](..%2Fadvertisements%2Fsettings.py).

___

# Python Files

## 1. [settings.py](settings.py)

* все настройки проекта для подключений приложений, директорий и базы данных, а также хосты
* `ALLOWED_HOSTS` - подключение хостов (ссылок) - [settings.py](settings.py) `37`
* `INSTALLED_APPS` - подключение стандартных и новых приложений проекта - [settings.py](settings.py) `48`
* `TEMPLATES` - настройка и подключение директории [templates](..%2Ftemplates) с шаблонами - [settings.py](settings.py) `71`
* `DATABASES` - подключение и настройка базы данных - [settings.py](settings.py) `95`
* `STATIC_URL & STATICFILES_DIRS ` - подключение и указание директории [static](..%2Fstatic) со статическими файлами - [settings.py](settings.py) `143`
* `STATIC_ROOT & STATICFILES_URL & STATICFILES_DIRS_ROOT` - подключение и указание директории [staticfiles](..%2Fstaticfiles)- [settings.py](settings.py) `151`- опциональная штука
* `MEDIA_URL & MEDIA_ROOT` - подключение и указание директории с медиа файлами [media](..%2Fmedia) связанные с базой данных - [settings.py](settings.py) `157`
* `DEFAULT_AUTO_FIELD` - подключение дебага или черт его знает для чего - [settings.py](settings.py) `161`

## 2. [urls.py](urls.py)

* подключение ссылок приложений проекта и администрирования
* `app_advertisements.urls` - приложение [app advertisements](..%2Fapp_advertisements) `25`
* `app_auth.urls` - приложение [app auth](..%2Fapp_auth) `26`
* `settings.DEBUG` - подключение debugging для панели администрирования (показ изображение в товарах) - настройка [models.py](..%2Fapp_advertisements%2Fmodels.py) `121 - 159`

## 3.[secrets.py](secrets.py)

* подключение секретного ключа проекта ([.env](..%2F..%2F.env)) - [settings.py](settings.py) `31`

## 4. [config.py](config.py)

* подключение и настройка проекта для сервера [Website](https://garage.xiver.ru) - админ сервера [Website](https://garage.xiver.ru)

___

[README.md](..%2F..%2FREADME.md)
