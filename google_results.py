from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from sys import platform

def get_results(search_term_arr):
  url = 'http://www.google.com'

  chrome_options = Options()  
  chrome_options.add_argument("--headless") 

  print('\n' + 'Running', platform, 'compatible driver...')
  for term in search_term_arr:
    if platform == "linux" or platform == "linux2":
      browser = webdriver.Chrome('./linux/chromedriver', options=chrome_options)
    elif platform == "darwin":
      browser = webdriver.Chrome('./darwin/chromedriver', options=chrome_options)
    elif platform == "win32":
      browser = webdriver.Chrome('./windows/chromedriver.exe', options=chrome_options)

    browser.get(url)

    search_box = browser.find_element_by_css_selector('#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')
    search_box.send_keys(term)
    search_box.submit()

    result_num = browser.find_element_by_id('resultStats').text

    print(term + ' results: ' + result_num + '\n')
    browser.close()

def user_input():
  error = True
  while error:
    try:
      term_num = int(input('How many terms do you want to search? '))

      search_term_arr = []
      i = 0
      while i < term_num:
        search_term = input('Enter search term ' + str(i + 1) + ': ')
        search_term_arr.append(search_term)
        i += 1

      error = False
      return search_term_arr
    except:
      print('You must enter an integer...', '\n')

def main(): 
  search_term_arr = user_input()

  get_results(search_term_arr)

if __name__ == "__main__":
  main()