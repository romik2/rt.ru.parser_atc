import time
import database
import files
import call
import tagui as r
import configparser
import datetime
import pyautogui

def downloadFile(login, password, domain, dateEnd):
    r.init(visual_automation = True)
    r.url('https://p2.cloudpbx.rt.ru/lk_new/#/admin/history')
    time.sleep(15)
    r.click('//*[@class="logout"]')
    r.type('//*[@name="username"]', login)
    r.type('//*[@name="password"]', password)
    if (r.read('//*[@name="domain"]') != domain):
        r.type('//*[@name="domain"]', domain + '[enter]')
    else:
        r.type('//*[@name="domain"]', '[enter]')
    r.click('//*[@value="'+(datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d.%m.%Y')+'"]')
    time.sleep(35)
    r.type('//*[@placeholder="Период – с"]', dateEnd + '[enter]')
    r.click('//*[@class="sc-bdVaJa jQsuix with-icon"]')
    time.sleep(25)
    r.close()

def main():
    config = configparser.ConfigParser()
    config.sections()
    config.read('config.ini')
    connection = database.create_connection(config['sql']['path'])

    endCall = database.end_call(connection)
    if (endCall == None):
        dateEnd = datetime.datetime.now()
    else:
        dateEnd = datetime.datetime.strptime(endCall[0], '%Y-%m-%d')
        endCallElement = call.set_data_call(endCall)

    downloadFile(config['rt.ru']['login'], config['rt.ru']['password'], config['rt.ru']['domain'], dateEnd.strftime('%d.%m.%Y'))
    calls = files.get_gata_workbook(config['export']['pathFileExport'])
    with connection:
        calls.reverse()
        for row in calls:
            call.set_data_call(row)
            database.create_call(connection, call.get_gata_call())

main()