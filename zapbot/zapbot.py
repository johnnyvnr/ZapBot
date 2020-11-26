from selenium import webdriver
import time

# Necesário estar instalado o Selenium e o ChromeWebDriver no PC
# Substitua o Grupo de Exemplo1 e Grupo de Exemplo2

class zapBot:
    def __init__(self):
        self.message = "Bom dia família, to testando um bot aqui."
        self.groups = ["Grupo de Exemplo1", "Grupo de exemplo2"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    def sendMsg(self):
#<span dir="auto" title="Grupo de Exemplo1" class="xxxxx">Grupo de Exemplo1</span>
#<div tabindex="-1" class="xxx">
#<span data-testid="send" data-icon="send" class="">
#É necessário trocar os códigos HTML pelos códigos presentes em seu PC
        self.driver.get('https://web.whattsapp.com')
        time.sleep(30)
        for group in self.groups:
            group = self.driver.find_element_by_xpath(f"//span[@title={group}]")
            time.sleep(3)
            group.click()
            chatBox = self.driver.find_elements_by_class_name('xxx')
            time.sleep(3)
            chatBox.click()
            chatBox.send_keys(self.message)
            sendButton = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            sendButton.click()
            time.sleep(3)

bot = zapBot()
bot.sendMsg()