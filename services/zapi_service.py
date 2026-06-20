from config import ZAPI_INSTANCE, ZAPI_INSTANCE_TOKEN, ZAPI_API_KEY
from services.supabase_service import Contato
from dataclasses import dataclass
from requests import request, Response

@dataclass
class ZApiStatus:
    connected: bool
    session: bool
    smartphone_connected: bool

@dataclass
class ZApiMessage:
    id: str
    message_id: str
    zaap_id: str

class ZApiError(RuntimeError):
    pass

class ZApiService:
    __URL_FORMAT = "https://api.z-api.io/instances/{}/token/{}"    

    def __init__(self):
        self.__url__ = self.__URL_FORMAT.format(
            ZAPI_INSTANCE,
            ZAPI_INSTANCE_TOKEN
            )
    
    def __request(self, method: str, command: str, body = None) -> any:
        headers = {"Client-Token": ZAPI_API_KEY}

        response = request(
                method,
                f"{self.__url__}/{command}",
                headers = headers,
                json = body
            )
        
        if response.ok:
            return response.json()
        elif response.status_code in (401, 403):
            raise ZApiError(
                    "Failed to connect. Verify the values of instance, token and security token"
                    )
        
        response.raise_for_status()
    
    def status(self) -> ZApiStatus:
        result = self.__request("GET", "status")

        if "connected" in result:
               return ZApiStatus(
                    connected=result["connected"],
                    session=result["session"],
                    smartphone_connected=result["smartphoneConnected"]
                    )
        else:
            raise ZApiError(
                f"{result['error']}: {result['message']}"
                )

    def send(self, phone: str, message: str) -> ZApiMessage:
        body = {
            "phone": phone,
            "message": message
            }

        result = self.__request("POST", "send-text", body)        

        return ZApiMessage(
                id=result["id"],
                message_id=result["messageId"],
                zaap_id=result["zaapId"]
            )

if __name__ == "__main__":
    zapi = ZApiService()
    status = zapi.status()

    if(status.connected):
        print("The z-api is available to use")

        if status.smartphone_connected:
            print("The whatsapp is connected")
        else:
            print("The whatsapp isn't connected")
    else:
        print("The z-api isn't available to use")
