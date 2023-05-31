# Linkin auto job apply bot

import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver

# Global variables
# ----------------
# Linkin login credentials
LINKIN_EMAIL = os.environ.get("LINKIN_EMAIL")
LINKIN_PASSWORD = os.environ.get("LINKIN_PASSWORD")

# Linkin job search url
LINKIN_JOB_SEARCH_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=103644278&keywords=python%20developer&location=United%20States"

# Linkin job apply url
LINKIN_JOB_APPLY_URL = "https://www.linkedin.com/jobs/view/{}"

# Linkin job apply button xpath
LINKIN_JOB_APPLY_BUTTON_XPATH = "/html/body/div[8]/div[3]/div[3]/div/div/div[2]/div/form/footer/div[2]/button"

# Linkin job apply button xpath
LINKIN_JOB_APPLY_BUTTON_XPATH_2 = "/html/body/div[8]/div[3]/div[3]/div/div/div[2]/div/form/footer/div[2]/button"

# Linkin job apply button xpath
LINKIN_JOB_APPLY_BUTTON_XPATH_3 = "/html/body/div[8]/div[3]/div[3]/div/div/div[2]/div/form/footer/div[2]/button"

# Linkin job apply button xpath
LINKIN_JOB_APPLY_BUTTON_XPATH_4 = "/html/body/div[8]/div[3]/div[3]/div/div/div[2]/div/form/footer/div[2]/button"

# Linkin job apply button xpath
LINKIN_JOB_APPLY_BUTTON_XPATH_5 = "/html/body/div[8]/div[3]/div[3]/div/div/div[2]/div/form/footer/div[2]/button"

# Linkin job apply button xpath
LINKIN_JOB_APPLY_BUTTON_XPATH_6 = "/html/body/div[8]/div[3]/div[3]/div/div/div[2]/div/form/footer/div[2]/button"

# Linkin job apply button xpath
LINKIN_JOB_APPLY_BUTTON_XPATH_7 = "/html/body/div[8]/div[3]/div[3]/div/div/div[2]/div/form/footer/div[2]/button"

# Linkin job apply button xpath
LINKIN_JOB_APPLY_BUTTON_XPATH_8 = "/html/body/div[8]/div[3]/div[3]/div/div/div[2]/div/form/footer/div[2]/button"

# Linkin job apply button xpath
LINKIN_JOB_APPLY_BUTTON_XPATH_9 = "/html/body/div[8]/div[3]/div[3]/div/div/div[2]/div/form/footer/div[2]/button"

# Linkin job apply button xpath
LINKIN_JOB_APPLY_BUTTON_XPATH_10 = "/html/body/div[8]/div[3]/div[3]/div/div/div[2]/div/form/footer/div[2]/button"


def get_job_links():
    """Get all job links from Linkin job search page"""

    # Create a chrome driver
    driver = webdriver.Chrome()

    # Get the Linkin job search page
    driver.get(LINKIN_JOB_SEARCH_URL)

    # Wait for page to load
    time.sleep(5)

    # Get the page source
    page_source = driver.page_source

    # Close the driver
    driver.close()

    # Create a soup object
    soup = BeautifulSoup(page_source, "html.parser")

    # Get all job links
    job_links = soup.find_all("a", class_="result-card__full-card-link")

    # Return the job links
    return job_links


def get_job_id(job_link):
    """Get the job id from the job link"""

    # Get the job id
    job_id = job_link["href"].split("-")[-1]

    # Return the job id
    return job_id


def get_job_apply_link(job_id):
    """Get the job apply link"""

    # Get the job apply link
    job_apply_link = LINKIN_JOB_APPLY_URL.format(job_id)

    # Return the job apply link
    return job_apply_link


def get_job_apply_button(driver):
    """Get the job apply button"""

    # Get the job apply button
    job_apply_button = driver.find_element_by_xpath(LINKIN_JOB_APPLY_BUTTON_XPATH)

    # Return the job apply button
    return job_apply_button


def get_job_apply_button_2(driver):
    """Get the job apply button"""

    # Get the job apply button
    job_apply_button = driver.find_element_by_xpath(LINKIN_JOB_APPLY_BUTTON_XPATH_2)

    # Return the job apply button
    return job_apply_button


def get_job_apply_button_3(driver):
    """Get the job apply button"""

    # Get the job apply button
    job_apply_button = driver.find_element_by_xpath(LINKIN_JOB_APPLY_BUTTON_XPATH_3)

    # Return the job apply button
    return job_apply_button


def get_job_apply_button_4(driver):
    """Get the job apply button"""

    # Get the job apply button
    job_apply_button = driver.find_element_by_xpath(LINKIN_JOB_APPLY_BUTTON_XPATH_4)

    # Return the job apply button
    return job_apply_button


def get_job_apply_button_5(driver):
    """Get the job apply button"""

    # Get the job apply button
    job_apply_button = driver.find_element_by_xpath(LINKIN_JOB_APPLY_BUTTON_XPATH_5)

    # Return the job apply button
    return job_apply_button


def get_job_apply_button_6(driver):
    """Get the job apply button"""

    # Get the job apply button
    job_apply_button = driver.find_element_by_xpath(LINKIN_JOB_APPLY_BUTTON_XPATH_6)

    # Return the job apply button
    return job_apply_button


def get_job_apply_button_7(driver):
    """Get the job apply button"""

    # Get the job apply button
    job_apply_button = driver.find_element_by_xpath(LINKIN_JOB_APPLY_BUTTON_XPATH_7)

    # Return the job apply button
    return job_apply_button


def get_job_apply_button_8(driver):
    """Get the job apply button"""

    # Get the job apply button
    job_apply_button = driver.find_element_by_xpath(LINKIN_JOB_APPLY_BUTTON_XPATH_8)

    # Return the job apply button
    return job_apply_button


def get_job_apply_button_9(driver):
    """Get the job apply button"""

    # Get the job apply button
    job_apply_button = driver.find_element_by_xpath(LINKIN_JOB_APPLY_BUTTON_XPATH_9)

    # Return the job apply button
    return job_apply_button


def get_job_apply_button_10(driver):
    """Get the job apply button"""

    # Get the job apply button
    job_apply_button = driver.find_element_by_xpath(LINKIN_JOB_APPLY_BUTTON_XPATH_10)

    # Return the job apply button
    return job_apply_button
