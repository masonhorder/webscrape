from requests import Session
from bs4 import BeautifulSoup as bs


with Session() as s:
    site = s.get("https://ih.schoolloop.com/portal/login?etarget=login_form")
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name":"form_data_id"})["value"]
    # token1 = bs_content.find("input", {"name":"form_data_id"})["value"]
    # print(token)
    login_data = {
        'login_name': 'mhorder',
    	'password': 'MasonH6',
        'form_data_id': token,
        'event_override': 'login'
        # 'redirect':'',
        # 'forward':'',
        # 'login_form_reverse':'',
        # 'sort':'',
        # 'reverse':'',
        # 'login_form_sort':'',
        # 'login_form_filter':'',
        # 'login_form_letter':'',
        # 'return_url':'',
        # 'login_form_page_index':'',
        # 'login_form_page_item_count':''







        #return_url
    }

    s.post("https://ih.schoolloop.com/portal/login?etarget=login_form", login_data)
    home_page = s.get("https://ih.schoolloop.com/portal/student_home")
    soup = bs(home_page.text, "html.parser")



list = []


row = soup.find_all('table', attrs={'class': 'student_row'})

i = 0

while i < 7:

    course_text = row[i].find('td', attrs={'class': 'course'})
    course = course_text.text

    zero_text = row[i].find('div', attrs={'class': 'float_l zeros'})
    zero = zero_text.text

    grade_text = row[i].find('div', attrs={'class': 'float_l percent'})
    grade = grade_text.text
    zero_num = [int(h) for h in zero.split() if h.isdigit()]

    list.extend([[course.strip(), grade.strip(), zero_num[0]]])

    # print(course.strip(), grade.strip(), zero_num[0])
    i = i+1
