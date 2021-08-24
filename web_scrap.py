import requests
from bs4 import BeautifulSoup
import time



print('pleaser enter the skills which you are not familiar with(separate them with space)')
unfamiliar_skills = input('>').split(' ')
print(f'filtering out: {unfamiliar_skills}')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=statistics&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')

def find_job():
    for job in soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx'):
        time = job.find('span', class_ = 'sim-posted').text
        if 'month' not in time:
            job_skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            familiar = True
            for skill in unfamiliar_skills:
                if skill in job_skills:
                    familiar = False
                    break
            if familiar:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
                link = job.header.h2.a['href']
                with open(f'result.txt', 'a') as f:
                    f.write(f'company: {company_name}')
                    f.write(f'skills requierd: {job_skills}')
                    f.write(f'more_info: {link}')
                    f.write('------------------------------------------------------------------')
    print(f'result.txt is created')


if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)


