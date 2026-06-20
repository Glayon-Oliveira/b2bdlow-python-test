from config import SUPABASE_URL, SUPABASE_KEY
from dataclasses import dataclass
from supabase import create_client, Client
from postgrest import APIError

@dataclass
class Contato:
    id: int
    name: str
    phone: str

class SupaService:
    def __init__(self):
        self.__supabase = create_client(SUPABASE_URL, SUPABASE_KEY)    
    
    def get_contatos(self) -> list[Contato]:        
        response = (
            self.__supabase
            .table("contatos")
            .select("id, name, phone")
            .execute()
        )

        return [
            Contato(
                id=item["id"],
                name=item["name"],
                phone=item["phone"]
            )
            for item in response.data
        ]

def get_contatos(): return SupaService().get_contatos()

if __name__ == "__main__":
    for contato in get_contatos():
        print(f"ID: {contato.id}")
        print(f"Name: {contato.name}")
        print(f"Phone: {contato.phone}")