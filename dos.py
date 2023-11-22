# -*- coding: utf-8 -*-

import concurrent.futures
import requests
import time

def fazer_requests(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Status da requisição HTTP: {response.status_code}")
        except requests.RequestException as e:
            print(f"Erro na requisição HTTP: {e}")
        time.sleep(1) 

url_alvo = 'https://test-ddos-a5c2a-default-rtdb.firebaseio.com' # My database for test!
quantidade_processos = 30 

with concurrent.futures.ProcessPoolExecutor(max_workers=quantidade_processos) as executor:
    for _ in range(quantidade_processos):
        executor.submit(fazer_requests, url_alvo)
