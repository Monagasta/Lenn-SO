import datetime
import platform
import sys

def mostrar_ajuda():
    print("""
Lenn SO - Comandos:
  python3 src/lenn-welcome.py --help      Mostra essa ajuda
  python3 src/lenn-welcome.py --version   Mostra a versão
  python3 src/lenn-welcome.py             Inicia o sistema
""")

if "--help" in sys.argv:
    mostrar_ajuda()
elif "--version" in sys.argv:
    print("Lenn SO v0.3 - Alpha")
else:
    print("="*30)
    print("  Lenn SO v0.3 - Booting...")
    print("="*30)
    nome = input("Qual seu nome? ")
    agora = datetime.datetime.now()
    print(f"\nFala {nome}, o Lenn SO foi iniciado com sucesso!")
    print(f"Data: {agora.strftime('%d/%m/%Y %H:%M')}")
    print(f"Base: {platform.system()} {platform.release()}")
    print("\n[OK] Sistema pronto.")