from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import spacy
import traceback


class EmployeeNameGetter:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        # self.s = Service(ChromeDriverManager().install())
        self.web_driver = webdriver.Chrome(executable_path='/home/wintermute/EAH/chromedriver',
                                           options=self.chrome_options)
        self.url = ""
        self.employee_name_list = []

    def get_url(self, company_name):
        # First, Open url
        self.url = 'https://www.google.com/search?q=site%3Alinkedin.com+-inurl%3A%22%2Fcompany%2F%22+%22at+' \
                   + str(company_name) + '22'
        self.web_driver.get(self.url)
        self.web_driver.implicitly_wait(2)

    def get_employee_name(self, company_name):
        # Next, Get employee name by search result
        self.get_url(company_name)
        result_list = self.web_driver.find_elements_by_css_selector('.LC20lb.DKV0Md')
        nlp = spacy.load("en_core_web_sm")

        try:
            for result in result_list:
                title_span = result.find_element_by_tag_name('span')
                candidate_employee_name_word = str(title_span.get_attribute('innerHTML'))

                if candidate_employee_name_word[:1].isalpha():
                    # To convert id, only english name allow
                    parsing_candidate_name_word = nlp(candidate_employee_name_word[:20])

                    employee_name = [ent.text for ent in parsing_candidate_name_word.ents
                                     if ent.label_ == 'PERSON']
                    for emp_name in employee_name:
                        self.employee_name_list.append(emp_name)
        except:
            print("Something Wrong: ", traceback.print_exc())

        finally:
            return self.employee_name_list


if __name__ == "__main__":
    test_employee_name_getter = EmployeeNameGetter()
    print(''.join(test_employee_name_getter.get_employee_name("Yahoo")))
