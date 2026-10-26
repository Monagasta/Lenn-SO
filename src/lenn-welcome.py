import datetime
import platform

print("="*30)
print("  Lenn SO v0.2 - Booting...")
print("="*30)

nome = input("Qual seu nome? ")
agora = datetime.datetime.now()

print(f"\nFala {nome}, o Lenn SO foi iniciado com sucesso!")
print(f"Data: {agora.strftime('%d/%m/%Y %H:%M')}")
print(f"Sistema base: {platform.system()} {platform.release()}")
print("\n[OK] Sistema pronto para uso.")