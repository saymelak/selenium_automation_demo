from framework.config import Config


class Home:
    MODAL_BUTTON = '/html/body/div[3]/div[3]/button'


class Forms:
    MODAL_BUTTON = '/html/body/div[3]/div[3]/button'
    NAME_FIELD = '//*[@id="myname"]'
    EMAIL_FIELD = '//*[@id="myemail"]'
    PASSWORD_FIELD = '//*[@id="mypassword"]'
    WEBSITE_FIELD = '//*[@id="myurl"]'
    PHONE_FIELD = '//*[@id="mytelephone"]'
    REFERENCE_FIELD = '//*[@id="reference"]'
    QUESTION_RADIO_BUTTON = '//*[@id="questionitem"]'
    COMMENT_RADIO_BUTTON = '//*[@id="commentitem"]'
    COMMENTS_FIELD = '//*[@id="myComments"]'
    SEND_BUTTON = '//*[@id="sendButton"]'
    OUTPUT_TITLE = '//*[@id="output"]'


class Page:
    HOME = Config.base_url + 'index.html'
    TABLES = Config.base_url + 'tables.html'
    FORMS = Config.base_url + 'forms.html'
    MODALS = Config.base_url + 'modals.html'
    VARIOUS = Config.base_url + 'various.html'
    CHARTS = Config.base_url + 'charts.html'


class To:
    HOME = '//*[@id="responsive-menu"]/div[1]/ul/li[2]/a'
    TABLES = '//*[@id="responsive-menu"]/div[1]/ul/li[3]/a'
    FORMS = '//*[@id="responsive-menu"]/div[1]/ul/li[4]/a'
    MODALS = '//*[@id="responsive-menu"]/div[1]/ul/li[5]/a'
    VARIOUS = '//*[@id="responsive-menu"]/div[1]/ul/li[6]/a'
    CHARTS = '//*[@id="responsive-menu"]/div[1]/ul/li[7]/a'


class Charts:
    CHART_TYPE_FIELD = '//*[@id="chartSelect"]'
    SUBMIT_BUTTON = '//*[@id="myButton1"]'
    CHART_TYPE_FIELD2 = '//*[@id="chartSelect2"]'
    SUBMIT_BUTTON2 = '//*[@id="myButton2"]'
    CHART1 = '//*[@id="myChart"]'
    CHART2 = '//*[@id="myChart2"]'


class Modals:
    QUANTITY_BUTTON = '//button[contains(text(),"Quantity")]'
    ALERT_BUTTON = '//button[contains(text(),"Alert")]'
    SECURITY_BUTTON = '//button[contains(text(),"Security")]'
    SETTINGS_BUTTON = '//button[contains(text(),"Settings")]'
