import requests

URL = "https://www.pudim.com.br/"
TIMEOUT = 5  # segundos

def check_http(url=URL, timeout=TIMEOUT):
    try:
        resp = requests.get(url, timeout=timeout)
        status = resp.status_code
        ok = 200 <= status < 400
        print(f"URL: {url}")
        print(f"Status code: {status} -> {'OK' if ok else 'Erro'}")
        return ok, status
    except requests.exceptions.SSLError as e:
        print("Erro SSL:", e)
        return False, "SSL error"
    except requests.exceptions.ConnectTimeout:
        print("Tempo de conexão esgotado")
        return False, "timeout"
    except requests.exceptions.ConnectionError as e:
        print("Erro de conexão:", e)
        return False, "connection error"
    except Exception as e:
        print("Outro erro:", e)
        return False, "other error"

if __name__ == "__main__":
    check_http()
