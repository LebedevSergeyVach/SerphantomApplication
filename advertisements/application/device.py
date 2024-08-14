from user_agents import parse
from colorama import Fore, Style, init


init()


def get_info_user(request):
    # Получение IP-адреса
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # Получение информации о браузере, устройстве и ОС
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    user_agent_info = parse(user_agent)

    # Определение типа устройства
    if user_agent_info.is_mobile:
        device_type = 'Мобильный телефон'
    elif user_agent_info.is_tablet:
        device_type = 'Планшет'
    elif user_agent_info.is_pc:
        device_type = 'Компьютер/Ноутбук'
    else:
        device_type = 'Неизвестное устройство'

    # Форматированный вывод информации
    print(f'\n{Fore.GREEN}Информация о пользователе:{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}IP-адрес: {Fore.CYAN}{ip}{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}Браузер: {Fore.CYAN}{user_agent_info.browser}{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}Устройство: {Fore.CYAN}{device_type}{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}Операционная система: {Fore.CYAN}{user_agent_info.os}{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}User-Agent строка: {Fore.CYAN}{user_agent}{Style.RESET_ALL}\n')


def get_info_divace(request) -> str:
    # Получение информации о браузере, устройстве и ОС
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    user_agent_info = parse(user_agent)

    # Определение типа устройства
    if user_agent_info.is_mobile:
        device_type = 'mobile'
    elif user_agent_info.is_tablet:
        device_type = 'tablet'
    elif user_agent_info.is_pc:
        device_type = 'desktop'
    else:
        device_type = 'unknown'

    return device_type
