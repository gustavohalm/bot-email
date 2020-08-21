from utils.bot import Bot
import time, os

bot = Bot('https://webmail-seguro.com.br')


def login(auth):
    bot.insert_input('//*[@id="rcmloginuser"]', auth['email'])
    bot.insert_input('//*[@id="rcmloginpwd"]', auth['pass'])
    bot.click('//*[@id="submitloginform"]')
    time.sleep(3)


def send_email(receiver, topic):
    #//*[@id="_to"]
    bot.click('//*[@id="rcmbtn110"]')
    time.sleep(3)
    bot.insert_input('//*[@id="_to"]', receiver)
    bot.insert_input('//*[@id="compose-subject"]', topic)
    bot.click('//*[@id="fileuploadbtn"]')
    bot.upload_file(xpath='//*[@id="uploadformInput"]', file_path='/home/gustavo/projects/bot-email/teste.txt')
    bot.click('//*[@id="rcmbtn110"]')
    time.sleep(1)
    bot.click('//*[@id="rcmbtn108"]')
    time.sleep(3)


def read_email():
    time.sleep(1)
    table_emails = bot.capture_table('//*[@id="messagelist"]')
    emails_rows = bot.list_itens(table_emails)
    id = emails_rows[0].get_attribute('id')
    bot.click_js(id)


if __name__  == "__main__":
    time.sleep(10)
    auth = {
        'email': os.environ['USER_MAIL'],
        'pass': os.environ['PASS_EMAIL']
    }
    login(auth)
    send_email('gustavo.almeida@cadmus.com.br', 'teste')
    time.sleep(10)
