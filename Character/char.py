class Character() :
    def __init__(self, role, profile, attribute) -> None:
        self.attribute = attribute
        self.profile = profile
        self.role = role
        self.armor = 0 # need to change
        self.maxHealth = 0 # need to change

    def getAttributeProfile(self) :
            return {"role" : self.role, "attribute" : self.attribute, "profile" : self.profile}