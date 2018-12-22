
            #Management and consulting to be continued from G(1001--5000)



from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

alpha = 'B%2CC'
if alpha == 'D':
    emp_size = '51-200'
elif alpha == 'E':
    emp_size = '201--500'
elif alpha == 'F':
    emp_size = '501--1000'
elif alpha == 'G':
    emp_size = '1001--5000'
elif alpha == 'H':
    emp_size = '5001--10000'
elif alpha == 'I':
    emp_size = '10000+'
else:
    emp_size = '1--50'


driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
sr = 1
err = 1
industry_type = 'Electronic/Electirc manufacturing'
csv_file = open('Electronic-Electirc manufacturing-CSV.csv'.format(emp_size=emp_size), 'a')
fieldnames = ['name', 'job_title', 'company', 'location', 'industry_type', 'emp_size', 'exp', 'detail', 'misc', 'link']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
# writer.writeheader()


driver.get('https://www.linkedin.com/')
time.sleep(2)
username = driver.find_element_by_xpath('//*[@id="login-email"]')
password = driver.find_element_by_xpath('//*[@id="login-password"]')
username.send_keys('afsh35532@gmail.com')
password.send_keys('Admin@2018#')
password.submit()
print('logged in -----------', driver.current_url)
time.sleep(2)
#---------------------------permenant---------------------------------------


for page in range(1, 46):

    url = 'https://www.linkedin.com/sales/search/people?companySize={alpha}&geo=us%3A0&industry=112&logHistory=true&logId=1805621275&page={page}&searchSessionId=nYL4aSEqTv6UELpxHe8Grw%3D%3D&title=IT%2520Manager%3A65%2CDirector%2520of%2520IT%3A163&titleTimeScope=CURRENT'.format(page=str(page), alpha=alpha)
    driver.get(url)
    print(driver.current_url)
    time.sleep(1)
    for i in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.3)
    time.sleep(0.3)
    source = driver.page_source
    time.sleep(0.5)
    soup = BeautifulSoup(source, 'lxml')
    articles = soup.findAll('article')
    for article in articles:
        title = article.find('dt', {'class': 'result-lockup__name'})
        name = title.text.strip()
        link = 'https://www.linkedin.com' + title.a['href']
        position = article.find('dd', {'class': 'result-lockup__highlight-keyword'})
        detail = position.text.strip()
        job_title = position.find('span', {'class': 'Sans-14px-black-75%-bold'}).text.strip()
        company_text = position.find('span', {'class': 'result-lockup__position-company'}).text.strip()
        try:
            company = company_text[:(company_text.find('Go to'))].strip()
        except:
            company = company_text
        try:
            exp = article.find('span', {'class': "Sans-12px-black-60%"}).text.strip()
        except:
            exp = '--'
        misc = article.find('ul', {'class': 'result-lockup__misc-list'}).text.strip()
        location = article.find('ul', {'class': 'mv1'}).text.strip()
        fieldnames = ['name', 'job_title', 'company', 'location', 'exp', 'detail', 'misc', 'link']
        try:
            my_dict = {'name': name, 'job_title': job_title, 'company': company,
                       'location': location, 'industry_type': industry_type, 'emp_size': emp_size,
                       'exp': exp, 'detail': detail, 'misc': misc, 'link': link}
            time.sleep(0.03)
            writer.writerow(my_dict)
            print(sr, '--', my_dict)
            sr += 1
        except:
            print('---------------', err, '-----------------')
            err += 1

    print(len(articles))
    print(emp_size)
    time.sleep(0.5)

print('successfuly saved ', sr, 'records')
print('errors -------------', err)
csv_file.close()
driver.close()








