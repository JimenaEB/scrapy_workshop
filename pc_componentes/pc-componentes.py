import cloudscraper

class PcComponentes():

    start_url = 'https://www.pccomponentes.com/tarjetas-graficas'

    scraper = cloudscraper.create_scraper()
    print(scraper.get("https://www.pccomponentes.com/tarjetas-graficas").text)