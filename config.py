import os
from dotenv import load_dotenv

load_dotenv()

#Supabase enviroments
SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

ZAPI_INSTANCE: str = os.getenv("ZAPI_INSTANCE")
ZAPI_INSTANCE_TOKEN: str = os.getenv("ZAPI_INSTANCE_TOKEN")
ZAPI_API_KEY: str = os.getenv("ZAPI_API_KEY")