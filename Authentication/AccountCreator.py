from InterfaceProcessor.Interface import CreatorProcessor
from Authentication.Authorizer import AccountAuthorizer
from Database.DatabaseGrabber import AddJson

class AccountCreator(CreatorProcessor) :
    def __init__(self, ctx) :
        self.ctx = ctx
    
    async def create(self) :
        id = self.ctx.message.author.id
        accountAuthorizer = AccountAuthorizer(id)

        if not accountAuthorizer.is_authorize() :
            await self.ctx.send('you\'ve already create account!')
            return False

        # hero = Adventurer(fname = nickname)
        # json_object[ctx.message.author.id] = hero.__dict__

        addJson = AddJson()
        addJson.addDatabase(id, data={"Nickname" : self.ctx.message.author.name})

        # del hero
        
        await self.ctx.send('your account successfully created!')