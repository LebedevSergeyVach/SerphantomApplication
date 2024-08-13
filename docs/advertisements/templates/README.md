# Documentation for the directory Templates

___

Документация к директории [templates]().

Эта папка отвечает за шаблоны .html файлов. Шаблоны отвечают за формирование внешнего вида приложения. 

Настройки подключения и другого находятся в файле [settings.py](..%2Fadvertisements%2Fsettings.py).
___

# Directories

## 1. [app advertisement](app_advertisement)

### Управление бэкендом шаблонов

* формы шаблона для размещения объявления и заноса его в базу данных - [advertisement-post.html](app_advertisement%2Fadvertisement-post.html) находятся в [forms.py](..%2Fapp_advertisements%2Fforms.py)
* управление базой данных для объявлений - [models.py](..%2Fapp_advertisements%2Fmodels.py)
* управление синхронизацией между шаблонами и ссылками - [urls.py](..%2Fapp_advertisements%2Furls.py)
* управление бэкендом и синхронизацией с базой данных страниц (размещение объявлений) - [views.py](..%2Fapp_advertisements%2Fviews.py)

### Шаблоны

* шаблон главной страницы сайта - [index.html](app_advertisement%2Findex.html)
* шаблон страницы топ-продавцов - [top-sellers.html](app_advertisement%2Ftop-sellers.html)
* шаблон страницы с объявлением - [advertisement.html](app_advertisement%2Fadvertisement.html)
* шаблон страницы разместить объявление - [advertisement-post.html](app_advertisement%2Fadvertisement-post.html)
* шаблон от которого идут все наследования - [base.html](../../../advertisements/templates/base.html)

## 2. [app auth](app_auth)

### Управление бэкендом шаблонов
* управление базой данных для аккаунтов - [models.py](..%2Fapp_advertisements%2Fmodels.py)
* управление синхронизацией между шаблонами и ссылками - [urls.py](..%2Fapp_auth%2Furls.py)
* управление бэкендом и синхронизацией с базой данных страниц (регистрация аккаунтов) - [views.py](..%2Fapp_auth%2Fviews.py)


### Шаблоны

* шаблон страницы с регистрацией - [register.html](app_auth%2Fregister.html)
* шаблон страницы входа в аккаунт - [login.html](app_auth%2Flogin.html)
* шаблон страницы просмотра профиля - [profile.html](app_auth%2Fprofile.html)

## 3. [app dop](app_dop)

* дополнительные временные шаблоны для debugging

___

[README.md](..%2F..%2FREADME.md)
