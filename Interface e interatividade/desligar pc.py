import time
import os
import platform

def shutdown():
    # Detecta o sistema operacional
    sistema = platform.system().lower()
    
    try:
        if "windows" in sistema:
            # /s = shutdown, /t 1 = em 1 segundo
            os.system("shutdown /s /t 1")
        elif "linux" in sistema or "darwin" in sistema: # darwin é o Mac
            os.system("shutdown -h now")
        else:
            print("\nSistema operacional não reconhecido.")
    except Exception as e:
        print(f"\nErro ao tentar o shutdown: {e}")

def temporizador_com_shutdown():
    print("=== Temporizador com Shutdown ===")
    try:
        entrada = input("Digite o tempo em segundos: ")
        segundos = int(entrada)
        
        while segundos > 0:
            # Transforma segundos em formato MM:SS
            mins, secs = divmod(segundos, 60)
            timer = f"{mins:02d}:{secs:02d}"
        
            # "\a" faz o computador dar um "Bip" sonoro
            bip = "\a" if 0 < segundos < 10 else ""
            
            # \r faz o texto sobrescrever a linha atual em vez de pular linha
            print(f"\rTempo restante: {timer} {bip}", end="", flush=True)
            
            time.sleep(1) # Espera 1 segundo
            segundos -= 1
        
        print("\n\nIniciando o desligamento... Tchau!")
        shutdown()

    except ValueError:
        print("\nErro: por favor, digite apenas números inteiros.")
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")

if __name__ == "__main__":
    temporizador_com_shutdown()