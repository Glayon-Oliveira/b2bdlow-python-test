import os
from dotenv import load_dotenv

load_dotenv()

#Supabase enviroments
SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")