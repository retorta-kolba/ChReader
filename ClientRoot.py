api_id = 447894
api_hash = 'cc5a0328d85995641668b0beb131e5e6'
class ClientRoot:
    @staticmethod
    def connect():
        default.connect()
    default = TelegramClient('session_name', api_id, api_hash)
    