from InterfaceProcessor.Interface import Authorizer
from Database.DatabaseGrabber import GetJson



class AccountAuthorizer(Authorizer) :
    
    def __init__(self, account_id) :
        self.account_id = account_id
        pass

    def is_authorize(self) -> bool:
        json_object = GetJson().getDatabase()

        if str(self.account_id) in json_object :
            return False
        return True    