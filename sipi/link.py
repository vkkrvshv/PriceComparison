import webbrowser
PHARMACY_LINKS = ["https://366.ru/search/?text=","https://planetazdorovo.ru/search/?q=","https://gorzdrav.org/search/?text=","https://budzdorov.ru/search/","https://stolichki.ru/search?name=", "https://www.rigla.ru/search?q=","https://zdravcity.ru/search/?what=","https://www.asna.ru/search/?query=","https://www.eapteka.ru/search/?q="]
#pharm = str(input())

def final_link(name, links=PHARMACY_LINKS):
    """
    Функция получения ссылок указанного товара со всех сайтов аптек

    :param name: название товара
    :param links: ссылки аптек
    :return: final[] -- список ссылок на товар из всех аптек
    """
    final = []
    for i in range(0, len(links)):
        final.append(links[i]+name)
    return final

#print(final_link(pharm))

