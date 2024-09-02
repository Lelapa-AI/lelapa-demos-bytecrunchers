# TODO: depending on the var returned here, check return value which determines which card to send flow to 
#TODO: only returning `not` when everything is fine i.e expected response is actually received response; name query returns Zinhle


class ArgumentProcessor:
    name_len_limit = 7
    age_limit = 18

    def trait(self, attribute, object):
        
        self.object = object
        default = "None found"

        return getattr(self, 'case_' + str(attribute), lambda: default)()

    def case_name(self):
        if len(self.object.get("name").strip()) > self.name_len_limit:
            return "name found"
        return "name not found"

    def case_age(self):
        if int(self.object.get("age")) >= self.age_limit:
            return "age found"
        return "age not found"
        
        
    def case_surname(self):

        if len(self.object.get("surname").strip()) > self.name_len_limit:
            return "surname found"
        return "surname not found"




my_switch = ArgumentProcessor()
print(my_switch.trait("name", {'name': 'K'}))