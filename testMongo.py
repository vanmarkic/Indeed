import re
import json
from bs4 import BeautifulSoup
from selenium import webdriver


def get_soup():
    """
    Given the url of a page, this function returns the soup object.
    
    Parameters:
        url: the link to get soup object for
    
    Returns:
        soup: soup object
    """
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get('https://be.indeed.com/cmp/Volta/jobs/Sp%C3%A9cialiste-%C3%89lectrotechnique-637102822a1379a1?sjdu=D9rABwEJMPTiYRcsWcX6lu9G9vLFEDSXKKTM3k_aLi9qLCcXzSbx9765DkYRgH9ggSO2GX7fIZWJYghd7Bda1skNcZ31vB5yYNlwz1hRQjEyJCYn0CScg1L3NPkyM4Lt&tk=1cugrbj10agps802&vjs=3')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()
    
    job = {}
    title = soup.find(name='h3', attrs={'class': "icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title"}).getText()
    posting = soup.find(name='div', attrs={'class': "jobsearch-JobComponent-description icl-u-xs-mt--md"}).get_text()
    contract = soup.find(name='div', attrs={'class': "jobsearch-JobMetadataHeader-item icl-u-xs-mt--xs"}).get_text()
    company = soup.find(name='div', attrs={'class': "icl-u-lg-mr--sm icl-u-xs-mr--xs"}).get_text()
    companyloc = soup.find(text=company).findNext('div').findNext('div').get_text()
    posttime = soup.find(name='div', attrs={'class': "jobsearch-JobMetadataFooter"}).contents[0]
    jobid = soup.find(name='span', attrs={'class': "indeed-apply-widget indeed-apply-button-container indeed-apply-status-not-applied"})['data-indeed-apply-jobid']

    job['title'], job['posting'], job['company'], job['Location'], job['contractType'], job['jobId'], job['postTime'] = \
    title, posting, company, companyloc, contract, jobid, posttime            

    print(job)       


    # output = inputTag['data-indeed-apply-jobid']
    # print(output)

get_soup()



