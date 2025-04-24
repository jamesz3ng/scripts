from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

seek_link = "https://www.seek.co.nz/Graduate-2026-jobs/in-All-Australia?sortmode=ListedDate"


# --- Configure Chrome Options ----
chrome_options = Options()
#chrome_options.add_argument("--headless")


def main():

	driver = webdriver.Chrome(options = chrome_options)
	driver.get(seek_link)

	WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-automation='jobTitle']"))
	)

	job_title_elements = driver.find_elements(By.CSS_SELECTOR, "a[data-automation='jobTitle']")
	job_titles_list = []
	for element in job_title_elements:
		text = element.text
		if text not in job_titles_list:
			job_titles_list.append(text)

	print(job_titles_list)

if __name__ == "__main__":
	main() 
