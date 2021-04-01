from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\\Users\\user\\Desktop\\geckodriver-v0.29.0-win64\\geckodriver.exe"
        )

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)#importante colocar, ele é o tempo de carregar a pagina
        #//input [@name="username"] informacao retirada do browser 
        #//input[@name ="password"]

        campo_usuario = driver.find_element_by_xpath("//input [@name='username']")
        campo_usuario.click() #clicando no campo de usuario
        campo_usuario.clear() #limpando campo do usuario para que esteja 100% pronto pra receber outra teclas
        campo_usuario.send_keys(self.username)

        campo_senha = driver.find_element_by_xpath("//input[@name ='password']")#colocar aspas simples no meio 
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)#simulacao do enter pra entrar na conta
        
        #agora_nao = driver.find_element_by_class_name("cmbtv") 
        #agora_nao.click()
        self.comente_nas_fotos_com_a_hashtag()




    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("Digitando comentário...")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1,3))

    def comente_nas_fotos_com_a_hashtag(self):
        a = 0
        while (1):
            sorteio_ganhar = "https://www.instagram.com/p/CMu3zVlHt6v/"
            ''' Aqui você coloca uma variável e atribui no valor o link do post da promoção. Por exemplo:
            sorteio_cozinha = "https://www.instagram.com/ ......"
            '''
            ##Nessa lista de sorteios, você insere todos as variáveis que você criou acima.
            sorteios = [
                sorteio_ganhar
            ]
            '''
            Este random existe para que a cada execução ele pegue um sorteio diferente. 
            Para minimizar a sensação que é um robô comentando
            '''
            sorteio_da_vez = random.choice(sorteios)
            driver = self.driver
            time.sleep(5)
            driver.get(sorteio_da_vez)
            #driver.execute_(
               # "window.scrollTo(0, document.body.scrollHeight);")
            try:
                '''
                Dentro dessa lista comments, você insere diversos @, para que a cada comentário ele sorteie algum e nunca repita o comentário.
                Dica: Se você for em algum video do youtube que fale sobre comentar em sorteio, nos comentários terão várias pessoas dizendo: "Pode me marcar, eu não me importo"
                Pegue o @ delas e coloque nessa lista, igual o exemplo abaixo.
                Coloque bastante @, tipo uns 30, 40, 50!!
                '''
                comments = [
                    "@gabrigabrielas", "@douglashenr979", "@gaby_p1997", "@gabriela.gabri199",
                     "@nagilayane", "@days2lara", "@efraimceciliano", "@nathfraga3785", "@sensitivez_z", "@letiiciafontes",
                     "@fernanda.sealed", "@_beto.veiga", "@_chavesju", "@tatai.17", "@oushirley_", "@deb.pim", "@gabyriibeir0",
                     "@prettamacedo", "@kaio_ligia_fabio", "@fabio_ligia_kaio", "@nataliaa_gabrielle", "@viictorya_marya_ofcl",
                     "@pedrafabricio", "@_yas_limma", "@ivna_furtado", "@eudeebora", "@jessycallima_", "@caiane.ferreira", "@ingeneraloficialff"

                ]
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(1, 20))
                '''
                Essa lógica abaixo, pessoa_1, pessoa_2 (...) existe pois em cada sorteio as pessoas pedem algo diferente
                Ou precisa marcar 1 pessoa, ou 2, 3, uma palavra qualquer, enfim. Então, dependendo do sorteio da vez, você precisará 
                definir qual das variáveis pessoa irá utilizar.
                '''
                pessoa_1 = random.choice(comments)
                pessoa_2 = random.choice(comments)
                pessoa_3 = random.choice(comments)
                marcar_3_pessoas = pessoa_1 + " " + pessoa_2 + " " + pessoa_3
                marcar_2_pessoas = pessoa_1 + " " + pessoa_2
                marcar_1_pessoa = pessoa_1
                '''Isto é o que comentei acima. Se for o sorteio da cozinha por exemplo, então comente utilizando a variável marcar_2_pessoas'''
                if sorteio_da_vez == sorteio_ganhar:
                    self.type_like_a_person(marcar_1_pessoa, comment_input_box)
                    #driver.find_element_by_class_name("sqdOP yWX7d y3zKF").click()
                    print("Comentei: ", marcar_1_pessoa, " no post: ", sorteio_da_vez, "sorteiozin do pai")

               # if sorteio_da_vez == variavel_com_url_do_post:
                   # self.type_like_a_person(marcar_2_pessoas, comment_input_box)
                   # print("Comentei: ", marcar_2_pessoas, " no post: ", sorteio_da_vez, "")
                #time.sleep(random.randint(1, 15))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                a = a + 1
                '''Aqui ele te informará quantas vezes já comentou o todo, desde o momento do start do '''
                print('Vezes comentadas:')
                print(a)
                if (a==200):
                    driver.quit()
                #A linha abaixo foi colocada a partir de uma sugestão no Youtube. Ela pode ser removida, caso você queira.
                #for i in range(1, 3): driver.execute_("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randint(1, 15)) 
                time.sleep(75)
                #Sugestão: Mude o trecho acima para time.sleep(60) para fazer um comentário a cada minuto e diminuir a possibilidade de ser bloqueado. 
            except Exception as e:
                print(e)
                time.sleep(5)



matheusBot = InstagramBot('email', 'senha')
matheusBot.login()
