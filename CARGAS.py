from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os   
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFilter

# Configuração de estilo e tema personalizado
def setup_styles():
    # Criar estilo personalizado
    style = ttk.Style()
    
    # Configurar o tema clam como base (melhor para personalização)
    style.theme_use('clam')
    
    # Configurações para o Frame
    style.configure('TFrame', background='#1a2a3a')
    
    # Configurações para Label
    style.configure('TLabel', background='#1a2a3a', foreground='white', font=('Segoe UI', 10))
    style.configure('Title.TLabel', background='#1a2a3a', foreground='#7eb6ff', font=('Segoe UI', 14, 'bold'))
    
    # Configurações para Combobox
    style.map('TCombobox', 
        fieldbackground=[('readonly', '#2c3e50')],
        background=[('readonly', '#1a2a3a')],
        foreground=[('readonly', 'white')],
        arrowcolor=[('readonly', '#7eb6ff')],
        bordercolor=[('readonly', '#7eb6ff')])
    style.configure('TCombobox', 
        borderwidth=1, 
        padding=5, 
        relief='flat', 
        background='#2c3e50', 
        arrowcolor='#7eb6ff',
        foreground='white',
        font=('Segoe UI', 10))
    
    # Configurações para o Botão
    style.configure('TButton', 
        background='#3498db', 
        foreground='white', 
        borderwidth=0, 
        focusthickness=3, 
        focuscolor='#2980b9',
        padding=(10, 5),
        font=('Segoe UI', 11, 'bold'))
    style.map('TButton', 
        background=[('active', '#2980b9'), ('pressed', '#1f618d')],
        foreground=[('pressed', 'white'), ('active', 'white')])

# Função para criar bordas arredondadas em um widget canvas
def create_rounded_frame(parent, width, height, corner_radius, fill_color, padding=10):
    # Criar um canvas para desenhar o frame arredondado
    canvas = tk.Canvas(parent, width=width, height=height, highlightthickness=0, bg=parent['background'])
    
    # Desenhar retângulo com cantos arredondados
    canvas.create_rounded_rectangle(
        padding, padding, width-padding, height-padding, 
        radius=corner_radius, fill=fill_color, outline='')
    
    # Criar um frame dentro do canvas para colocar widgets
    inner_frame = ttk.Frame(canvas, style='InnerFrame.TFrame')
    inner_frame.place(x=padding*2, y=padding*2, width=width-padding*4, height=height-padding*4)
    
    return canvas, inner_frame

# Adicionar método para criar retângulos com cantos arredondados
tk.Canvas.create_rounded_rectangle = lambda self, x1, y1, x2, y2, radius=25, **kwargs: self.create_polygon(
    x1+radius, y1,
    x2-radius, y1,
    x2, y1,
    x2, y1+radius,
    x2, y2-radius,
    x2, y2,
    x2-radius, y2,
    x1+radius, y2,
    x1, y2,
    x1, y2-radius,
    x1, y1+radius,
    x1, y1,
    smooth=True, **kwargs)

# Criar uma imagem de fundo com gradiente
def create_gradient_image(width, height, color1="#0a1525", color2="#1e3a5f"):
    # Criar uma imagem com gradiente
    gradient_image = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(gradient_image)
    
    for y in range(height):
        r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
        r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
        
        ratio = y / height
        r = int(r1 * (1 - ratio) + r2 * ratio)
        g = int(g1 * (1 - ratio) + g2 * ratio)
        b = int(b1 * (1 - ratio) + b2 * ratio)
        
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Adicionar um pouco de ruído para textura
    gradient_image = gradient_image.filter(ImageFilter.GaussianBlur(radius=1))
    
    return ImageTk.PhotoImage(gradient_image)

# A lógica principal da aplicação será executada quando o botão for clicado
def iniciar_aplicacao():
    opcao_selecionada = combo_lojas.get()
    
    if not opcao_selecionada:
        messagebox.showerror("Erro", "Selecione uma opção de lojas!")
        return
    
    # Fecha a janela
    root.destroy()
    
    # Obtém o diretório do arquivo atual
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    os.chdir(caminho_atual)

    log_blue= ''
    senha_blue= ''
    log_zeus=''
    senha_zeus=''

    # selenium+url
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://erp.bluesoft.com.br/minipreco/app/#/menu')

    

    # lojas
    def lojas_PR_minipreco():
        lojas_PR_minipreco=[
        'LJ 01 - JUMBO SANTA FELICIDADE',
        'LJ 02 - JUMBO TORRES',
        'LJ 04 - JUMBO PINHAIS',
        'LJ 06 - JUMBO PARANAGUA',
        'LJ 07 - JUMBO FANNY',
        'LJ 08 - JUMBO FAZ. RIO GRANDE',
        'LJ 10 - JUMBO XAXIM',
        'LJ 11 - JUMBO FAZENDINHA',
        'LJ 12 - JUMBO BOULEVARD',
        'LJ 14 - JUMBO COLOMBO',
        'LJ 19 - JUMBO ARAUCARIA',
        'LJ 20 - JUMBO BACACHERI'
        ]
        for x in lojas_PR_minipreco:
            driver.find_element(By.XPATH, f"//label[contains(., '{x}')]/input[@type='checkbox']").click()

    def lojas_PR_salvados():
        lojas_PR_salvados=[
        'LJ 01 - JUMBO SANTA FELICIDADE',
        'LJ 02 - JUMBO TORRES',
        'LJ 04 - JUMBO PINHAIS',
        'LJ 06 - JUMBO PARANAGUA',
        'LJ 08 - JUMBO FAZ. RIO GRANDE',
        'LJ 09 - JUMBO SALVADOS SITIO CERCADO',
        'LJ 11 - JUMBO FAZENDINHA',
        'LJ 14 - JUMBO COLOMBO',
        'LJ 17 - JUMBO SALVADOS XAXIM',
        'LJ 18 - JUMBO SALVADOS FANNY',
        'LJ 19 - JUMBO ARAUCARIA'
        ]
        for x in lojas_PR_salvados:
            driver.find_element(By.XPATH, f"//label[contains(., '{x}')]/input[@type='checkbox']").click()

    def lojas_SC_salvados():
        lojas_SC_salvados=[
        'LJ 201 - JUMBO SALVADOS BAL CAMBORIU',
        'LJ 202 - JUMBO SALVADOS ITAJAÍ',
        'LJ 203 - JUMBO SALVADOS BLUMENAU',
        'LJ 204 - JUMBO SALVADOS JARAGUA DO SUL',
        'LJ 208 - JUMBO SALVADOS JOINVILLE'
        ]
        for x in lojas_SC_salvados:
            driver.find_element(By.XPATH, f"//label[contains(., '{x}')]/input[@type='checkbox']").click()

    def lojas_ESPIRITO_SANTO_mini_preco():
        lojas_ESPIRITO_SANTO_mini_preco=[
        'LJ 301 - JUMBO VILA VELHA',
        'LJ 303 - JUMBO SERRA',
        'LJ 304 - JUMBO VITORIA',
        'LJ 305 - JUMBO LINHARES',
        'LJ 307 - JUMBO GLORIA',
        'LJ 308 - JUMBO DAY BY DAY'
        ]
        for x in lojas_ESPIRITO_SANTO_mini_preco:
            driver.find_element(By.XPATH, f"//label[contains(., '{x}')]/input[@type='checkbox']").click()   

    def Todas_lojas_minipreco():
        Todas_lojas_minipreco=[
        'LJ 01 - JUMBO SANTA FELICIDADE',
        'LJ 02 - JUMBO TORRES',
        'LJ 04 - JUMBO PINHAIS',
        'LJ 06 - JUMBO PARANAGUA',
        'LJ 07 - JUMBO FANNY',
        'LJ 08 - JUMBO FAZ. RIO GRANDE',
        'LJ 10 - JUMBO XAXIM',
        'LJ 11 - JUMBO FAZENDINHA',
        'LJ 12 - JUMBO BOULEVARD',
        'LJ 14 - JUMBO COLOMBO',
        'LJ 19 - JUMBO ARAUCARIA',
        'LJ 20 - JUMBO BACACHERI',
        'LJ 301 - JUMBO VILA VELHA',
        'LJ 303 - JUMBO SERRA',
        'LJ 304 - JUMBO VITORIA',
        'LJ 305 - JUMBO LINHARES',
        'LJ 307 - JUMBO GLORIA',
        'LJ 308 - JUMBO DAY BY DAY'
        ]
        for x in Todas_lojas_minipreco:
            driver.find_element(By.XPATH, f"//label[contains(., '{x}')]/input[@type='checkbox']").click() 

    # função loguin 
    def loguin_function():
        sleep(1)
        wait = WebDriverWait(driver, 15)  # Espera até 15 segundos
        usuario = wait.until(EC.presence_of_element_located((By.ID, "j_username")))
        usuario.click()
        usuario.send_keys(log_blue)
        password = wait.until(EC.presence_of_element_located((By.ID, "j_password")))
        password.click()
        password.send_keys(senha_blue)
        sleep(3)
        login = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmit"))).click()
        driver.maximize_window()
        sleep(8)

    def cargas_page():
        try:
            driver.switch_to.frame("menu")  #pega o iframe com id/nome menu
            # driver.switch_to.default_content()   # voltar iframe anterior

            alemt = driver.find_element(By.ID, "buscaRapidaFormInput")
            alemt.click()
            alemt.send_keys('170' + Keys.ENTER)
            sleep(8)
            # segundo iframe
            iframes = driver.find_elements(By.TAG_NAME, "iframe")

            driver.switch_to.frame(iframes[-1])  # O índice -2 seleciona o penúltimo elemento
        except Exception as e:
            print('ERRO IFRAMES, em cargas_page: ', e)
        
        somente_alterados=driver.find_element(By.XPATH, '//option[@label="Somente alterados no período"]').click()
        input_pdv = driver.find_element(By.XPATH, "//label[contains(., 'PDVs')]/input[@type='checkbox']").click()
        input_pdv = driver.find_element(By.XPATH, "//label[contains(., 'Terminais de Consulta')]/input[@type='checkbox']").click()
        input_pdv = driver.find_element(By.XPATH, "//label[contains(., 'Promoção Ganhe Pontos')]/input[@type='checkbox']").click()
        input_pdv = driver.find_element(By.XPATH, "//label[contains(., 'PDVs Regras Fiscais (Zanthus)')]/input[@type='checkbox']").click()
        input_pdv = driver.find_element(By.XPATH, "//label[contains(., 'Etiquetas')]/input[@type='checkbox']").click()


    def tempo_loop():
        sleep(20)
        progress1=driver.find_element(By.XPATH, '//div[@class="progress-bar"]//span[@class="ng-binding ng-scope"]').text
        ativo=True
        while ativo ==True:
            try:
                while progress1 != '100%':
                    sleep(30)
                    progress1=driver.find_element(By.XPATH, '//div[@class="progress-bar"]//span[@class="ng-binding ng-scope"]').text
                    print('ainda em laço', progress1)
                print('laço finalizado', progress1)
            except Exception as err:
                ativo=False
                print('laço finalizado, avançando')


    def principal_bluesoft(lojas_estado):
        loguin_function()
        cargas_page()
        lojas_estado()
        sleep(2)
        botao_gerar=driver.find_element(By.XPATH, '//button[@id="gerarArquivos"]')
        botao_gerar.click()
        tempo_loop()
        print('tudo finalizado no lado bluesofit')

    

    # zanthus
    def loguin_function_zanthus():
        print('iniciando no lado Zanthus')
        sleep(2)
        wait = WebDriverWait(driver, 10)  # Espera até 10 segundos
        usuario = wait.until(EC.presence_of_element_located((By.ID, "USUARIO")))
        usuario.click()
        usuario.send_keys(log_zeus)
        password = wait.until(EC.presence_of_element_located((By.ID, "SENHA")))
        password.click()
        password.send_keys(senha_zeus)
        login = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value=" Entrar "]'))).click()
        driver.maximize_window()
        sleep(6)
        driver.find_element(By.XPATH, '//span[@aria-hidden="true"]').click()
        driver.get('https://minipreco.zanthus.bluesoft.com.br/manager/adm_cargaDiretaArquivosSemZMS.php5?id_menu=405')
        sleep(2)
        driver.find_element(By.XPATH, '//input[contains(@value, "1- MINIPRECO SANTA FELICIDADE")]/following-sibling::div[@class="control__indicator"]').click()
        caixas_Box=driver.find_elements(By.XPATH, '//div[@class="control__indicator"]')
        caixas_Box[-1].click()
        sleep(2)

    #  '''listas das lojas ''''

    armazena_loja_PR_minipreco=[
    "1- MINIPRECO SANTA FELICIDADE",
    "2- MINIPRECO TORRES",
    "4- MINIPRECO PINHAIS",
    "6- RDS PARANAGUA",
    "7- MINIPRECO FANNY",
    "8- MINIPRECO FAZENDA RIO GRANDE",
    "10- MINIPRECO XAXIM",
    "11- MINIPRECO FAZENDINHA",
    "12- MINIPRECO EXPRESS BOULEVARD",
    "14- MINIPRECO COLOMBO",
    "19- MINIPRECO ARAUCARIA",
    "20- MINIPRECO BACACHERI"
    ]
    armazena_loja_PR_salvados=[
    "1- MINIPRECO SANTA FELICIDADE",
    "2- MINIPRECO TORRES",
    "4- MINIPRECO PINHAIS",
    "6- RDS PARANAGUA",
    "8- MINIPRECO FAZENDA RIO GRANDE",
    "9- RDS SITIO CERCADO",
    "11- MINIPRECO FAZENDINHA",
    "14- MINIPRECO COLOMBO",
    "17- RDS XAXIM",
    "18- RDS FANNY",
    "19- MINIPRECO ARAUCARIA"
    ]
    armazena_lojas_SC_salvados=[
    "201- RDS BALNEARIO CAMBORIU",
    "202- RDS ITAJAI",
    "203- RDS BLUMENAU",
    "204- RDS JARAGUA DO SUL",
    "208- RDS JOINVILLE"
    ]
    armazena_lojas_ESPIRITO_SANTO_mini_preco=[
    "301- MINIPRECO VILA VELHA",
    "303- MINIPRECO SERRA",
    "304- MINIPRECO VITORIA",
    "305- MINIPRECO LINHARES",
    "307- MINIPRECO GLORIA",
    "308- MINIPRECO DAY BY DAY"
    ]
    armazena_todas_loja_minipreco=[
    "1- MINIPRECO SANTA FELICIDADE",
    "2- MINIPRECO TORRES",
    "4- MINIPRECO PINHAIS",
    "6- RDS PARANAGUA",
    "7- MINIPRECO FANNY",
    "8- MINIPRECO FAZENDA RIO GRANDE",
    "10- MINIPRECO XAXIM",
    "11- MINIPRECO FAZENDINHA",
    "12- MINIPRECO EXPRESS BOULEVARD",
    "14- MINIPRECO COLOMBO",
    "19- MINIPRECO ARAUCARIA",
    "20- MINIPRECO BACACHERI",
    "301- MINIPRECO VILA VELHA",
    "303- MINIPRECO SERRA",
    "304- MINIPRECO VITORIA",
    "305- MINIPRECO LINHARES",
    "307- MINIPRECO GLORIA",
    "308- MINIPRECO DAY BY DAY"
    ]

    #  função principal de gerador de cargas nas lojas
    def cargas_zanthus_fun(lojas_lista):
            for x in lojas_lista:
                a=driver.find_element(By.XPATH, f'//input[contains(@value, "{x}")]/following-sibling::div[@class="control__indicator"]')
                a.click()
                sleep(0.5)
                carga_parcial=driver.find_element(By.XPATH,'//input[@value="Carga Parcial" and @name="GERAR"]').click()
                sleep(10)
                try:
                    tempo=driver.find_element(By.XPATH, f'//td[@id="R_{x.split('-')[0]}_TD_3"]').text
                except Exception as err: print(err)
                sleep(3)
                try:
                    tempo2=driver.find_element(By.XPATH, f'//td[@id="R_{x.split('-')[0]}_TD_3"]').text
                except Exception as err: print(err)
                while tempo != tempo2:
                    sleep(2)
                    tempo=driver.find_element(By.XPATH, f'//td[@id="R_{x.split('-')[0]}_TD_3"]').text
                    sleep(4)
                    tempo2=driver.find_element(By.XPATH, f'//td[@id="R_{x.split('-')[0]}_TD_3"]').text
                print(f'A carga da loja {x}, foi finalizado, indo para o príximo laço.')
                sleep(1)
                a=driver.find_element(By.XPATH, f'//input[contains(@value, "{x}")]/following-sibling::div[@class="control__indicator"]')
                a.click()
                sleep(2)





    def zanthus_lojas_PR_minipreco():
        cargas_zanthus_fun(armazena_loja_PR_minipreco)

    def zanthus_lojas_PR_salvados():
        cargas_zanthus_fun(armazena_loja_PR_salvados)

    def zanthus_lojas_SC_salvados():
        cargas_zanthus_fun(armazena_lojas_SC_salvados)

    def zanthus_lojas_ESPIRITO_SANTO_mini_preco():
        cargas_zanthus_fun(armazena_lojas_ESPIRITO_SANTO_mini_preco)

    def zanthus_Todas_lojas_minipreco():
        cargas_zanthus_fun(armazena_todas_loja_minipreco)
    



    # Executar a função selecionada
    if opcao_selecionada == "Lojas PR MiniPreço":
        principal_bluesoft(lojas_PR_minipreco)
        driver.get('https://minipreco.zanthus.bluesoft.com.br/manager/adm_cargaDiretaArquivosSemZMS.php5?id_menu=405')
        loguin_function_zanthus()
        zanthus_lojas_PR_minipreco()
        print('TUDO FINALIZADO, FECHANDO CÓDIGO EM 10seg')

    elif opcao_selecionada == "Lojas PR Salvados":
        principal_bluesoft(lojas_PR_salvados)
        driver.get('https://minipreco.zanthus.bluesoft.com.br/manager/adm_cargaDiretaArquivosSemZMS.php5?id_menu=405')
        loguin_function_zanthus()
        zanthus_lojas_PR_salvados()
        print('TUDO FINALIZADO, FECHANDO CÓDIGO EM 10seg')

        
    elif opcao_selecionada == "Lojas SC Salvados":
        principal_bluesoft(lojas_SC_salvados)
        driver.get('https://minipreco.zanthus.bluesoft.com.br/manager/adm_cargaDiretaArquivosSemZMS.php5?id_menu=405')
        loguin_function_zanthus()
        zanthus_lojas_SC_salvados()
        print('TUDO FINALIZADO, FECHANDO CÓDIGO EM 10seg')


    elif opcao_selecionada == "Lojas Espírito Santo MiniPreço":
        principal_bluesoft(lojas_ESPIRITO_SANTO_mini_preco)
        driver.get('https://minipreco.zanthus.bluesoft.com.br/manager/adm_cargaDiretaArquivosSemZMS.php5?id_menu=405')
        loguin_function_zanthus()
        zanthus_lojas_ESPIRITO_SANTO_mini_preco()
        print('TUDO FINALIZADO, FECHANDO CÓDIGO EM 10seg')

    elif opcao_selecionada == "Todas as lojas MiniPreço":
        principal_bluesoft(Todas_lojas_minipreco)
        driver.get('https://minipreco.zanthus.bluesoft.com.br/manager/adm_cargaDiretaArquivosSemZMS.php5?id_menu=405')
        loguin_function_zanthus()
        zanthus_Todas_lojas_minipreco()
        print('TUDO FINALIZADO, FECHANDO CÓDIGO EM 10seg')

    sleep(10)

# Criar a interface gráfica
root = tk.Tk()
root.title("Bluesoft Zeus - Seleção de Lojas")
root.geometry("500x400")
root.minsize(500, 400)
root.configure(bg="#0a1525")

# Configurar estilos personalizados
setup_styles()

# Criar frame de fundo com gradiente
width, height = 500, 400
background_image = create_gradient_image(width, height)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Criar o frame principal com cantos arredondados
main_canvas, main_frame = create_rounded_frame(root, width-40, height-40, 15, "#1a2a3a", padding=0)
main_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Adicionar título com um estilo especial
title_label = ttk.Label(main_frame, text="Bluesoft Zeus", style='Title.TLabel')
title_label.pack(pady=(30, 5))

subtitle_label = ttk.Label(main_frame, text="Selecione o grupo de lojas para carga", font=('Segoe UI', 10))
subtitle_label.pack(pady=(0, 25))

# Criar frame para combobox com borda especial
combo_frame = ttk.Frame(main_frame, style='TFrame', padding=(20, 10))
combo_frame.pack(fill=tk.X, padx=30, pady=10)

# Combobox para seleção de lojas com estilo personalizado
opcoes_lojas = [
    "Lojas PR MiniPreço",
    "Lojas PR Salvados",
    "Lojas SC Salvados",
    "Lojas Espírito Santo MiniPreço",
    "Todas as lojas MiniPreço"
]

combo_lojas = ttk.Combobox(combo_frame, values=opcoes_lojas, width=30, state="readonly")
combo_lojas.pack(fill=tk.X, expand=True)
combo_lojas.bind('<FocusIn>', lambda e: root.focus_set())  # Evitar o destacamento da borda ao focar

# Botão para iniciar com efeito de relevo e cores personalizadas
btn_frame = ttk.Frame(main_frame, style='TFrame', padding=(20, 10))
btn_frame.pack(fill=tk.X, padx=30, pady=(30, 0))

btn_iniciar = ttk.Button(btn_frame, text="INICIAR CARGA", command=iniciar_aplicacao)
btn_iniciar.pack(fill=tk.X)

# Adicionar informações sobre versão
version_label = ttk.Label(main_frame, text="v1.0.0", font=('Segoe UI', 8))
version_label.pack(side=tk.BOTTOM, pady=10)

# Configurar para que a janela apareça no centro da tela
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

# Executar a interface
root.mainloop()



