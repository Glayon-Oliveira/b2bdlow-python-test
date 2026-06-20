import logging
from services.supabase_service import get_contatos
from services.zapi_service import ZApiService

if __name__ == "__main__":
    print("Iniciando")
    
    zapi = ZApiService()
    
    print("Buscando contatos...")

    contatos = get_contatos()[:3]

    print(f"{len(contatos)} contatos encontrados")

    if contatos:
        print("\nEnviando mensagens (limitado a três)...")

        for contato in contatos:
            print(f"\nEnviando para {contato.name}, {contato.phone}")
            try:
                message = zapi.send(
                    contato.phone,
                    f"Olá, {contato.name} tudo bem com você?"
                    )

                print(f"Mensagem enviada para API:")
                print(f"- ID: {message.id}")
                print(f"- Message ID: {message.message_id}")
                print(f"- Z-API ID: {message.zaap_id}")
            except Exception as e: 
                print(f"Falha ao enviar para {contato.name}: {e}")

    print("\nEncerrando...")
