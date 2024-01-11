import os
import requests
from colorama import Fore, Style
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import RequestException

def verificar_elemento(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        h3_element = soup.find('h3', class_='_9vd5 _9scr', style='color:#5E5E5E;')

        if h3_element and h3_element.text.strip():
            result = f'[ {Fore.GREEN}✔️{Fore.WHITE} ] {Fore.GREEN}disponível{Fore.WHITE} ~ {Fore.CYAN}{url}{Fore.WHITE}: {h3_element.text}'
        else:
            result = f'[ {Fore.RED}✖️{Fore.WHITE} ] {Fore.RED}inexistente {Fore.WHITE}~{Fore.RED} {url}{Fore.WHITE}'
    except RequestException as e:
        result = f'Erro ao acessar a URL {url}. Detalhes: {str(e)}'

    print(result)

    with open(output_file, 'a') as output:
        print(result, file=output)

    return result



print(f'''{Fore.WHITE}                                                       .
                    |\__/,|   (`\\                      .
                  _.|o o  |_   ) )                     {Fore.WHITE}.
                -(((---(((--------                     {Fore.WHITE}.{Fore.YELLOW}
  ▄████  ▄▄▄     ▄▄▄█████▓ ▒█████                      {Fore.WHITE}.{Fore.YELLOW}
 ██▒ ▀█▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒                    {Fore.WHITE}.{Fore.YELLOW}
▒██░▄▄▄░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒                    {Fore.WHITE}.    Autor: {Fore.CYAN}Gato Preto{Fore.YELLOW}
░▓█  ██▓░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░                    {Fore.WHITE}.    │{Fore.YELLOW}
░▒▓███▀▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░                    {Fore.WHITE}.    └──> {Fore.WHITE}Instagram:{Fore.CYAN} @gato.ads{Fore.YELLOW}
 ░▒   ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░                     {Fore.WHITE}.{Fore.YELLOW}
  ░   ░   ▒   ▒▒ ░   ░      ░ ▒ ▒░                     {Fore.WHITE}.{Fore.YELLOW}
░ ░   ░   ░   ▒    ░      ░ ░ ░ ▒                      {Fore.WHITE}.{Fore.YELLOW}
      ░       ░  ░            ░ ░                      {Fore.WHITE}.{Fore.YELLOW}

Apenas se transforme.

''')
print(f'{Fore.GREEN}Automação para verificar links de WhatsApp em massa.\n{Fore.WHITE}')
print('---------------------------------------------------------------------------------\n\n')

txt_files = [file for file in os.listdir() if file.endswith('.txt')]
file_dict = {index + 1: file for index, file in enumerate(txt_files)}

for number, file in file_dict.items():
    print(f"[ {number} ] = {file}")

selected_number = int(input(f"{Fore.CYAN}\nDigite o número correspondente ao arquivo desejado:{Fore.WHITE} "))
if selected_number in file_dict:
    selected_file = file_dict[selected_number]
    with open(selected_file, 'r') as file:
        urls = file.read().splitlines()

    seen_urls = set()
    processamento = int(input(f'\n--- --- ---\n\n{Fore.CYAN}Quantas threads você deseja utilizar? Quanto maior, mais rápido\nDigite um número:{Fore.WHITE} '))

    output_file = input(f'\n--- --- ---\n\n{Fore.CYAN}Digite o nome do arquivo para salvar o resultado:{Fore.WHITE} ')
    print('\n')

    if 1 <= processamento <= 30:
        with ThreadPoolExecutor(max_workers=processamento) as executor:
            results = [executor.submit(verificar_elemento, url, output_file) for url in urls if url not in seen_urls and (seen_urls.add(url) or True)]
            output_results = [result.result() for result in results]

        print(f'{Fore.GREEN}\nResultados salvos em {output_file}{Fore.RESET}')
    else:
        print(f'{Fore.RED}Número de threads inválido. Por favor, não seja cabeça de xota e escolha um número entre 1 e 30.{Fore.RESET}')
else:
    print('Número inválido. Por favor, selecione um número válido.')
