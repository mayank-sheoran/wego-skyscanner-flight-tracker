from bs4 import BeautifulSoup
from selenium import webdriver
from urlMap import SKY_SCANNER_URL_MAP

chromeDriverPath = "/Users/mayanksheoran/Desktop/Root/Coding/Github/wego-skyscanner-flight-tracker/chromedriver"
driver = webdriver.Chrome()

# Skyscanner
flights = {}
for key in SKY_SCANNER_URL_MAP:
    flights[key] = []
    skyScannerUrl = SKY_SCANNER_URL_MAP[key]
    "DEL-BLR | 17:20 -> 19:45 | 2h 25 | $1234"
    driver.get(skyScannerUrl)
    driver.implicitly_wait(30)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    for flightDataContainer in soup.find_all('div', class_='BpkTicket_bpk-ticket__NzNiO'):
        departureContainer = flightDataContainer.find('div', class_='LegInfo_routePartialDepart__NzEwY')
        departureTime = departureContainer.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--subheading__NzkwO').text
        landingContainer = flightDataContainer.find('div', class_='LegInfo_routePartialArrive__Y2U1N')
        landingTime = landingContainer.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--subheading__NzkwO').text
        timeContainer = flightDataContainer.find('div', class_='LegInfo_stopsContainer__NWIyN')
        flightTime = timeContainer.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--xs__ZDJmY Duration_duration__NmUyM').text
        priceContainer = flightDataContainer.find('div', class_='Price_mainPriceContainer__MDM3O')
        mainPrice = priceContainer.find('span', class_='BpkText_bpk-text__MWZkY').text
        flights[key].append(str(key) + ' | ' + str(departureTime) + ' -> ' + str(landingTime) + ' | '
                       + str(flightTime) + ' | ' + str(mainPrice))
print(flights)
driver.quit()

# Wego
# driver.get(wegoUrl)
# driver.implicitly_wait(35)
# html_content = driver.page_source
# soup = BeautifulSoup(html_content, 'html.parser')
# price_div = soup.find('div', {'data-pw': 'tripCard_price', 'class': 'tAoIGESyiBp0wGwZ7ocq uTb5WY3zgAuoA9_1ZlXL'})
# for price in price_div.find_all('span')[1].text:
#     print(price)
# driver.quit()

