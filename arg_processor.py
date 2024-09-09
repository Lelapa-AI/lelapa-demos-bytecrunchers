# TODO: depending on the var returned here, check return value which determines which card to send flow to 
#TODO: only returning `not` when everything is fine i.e expected response is actually received response; name query returns Zinhle


class ArgumentProcessor:
    name_len_limit = 3
    age_limit = 18

    def trait(self, attribute, object):
        self.object = object
        default = "not"
        return getattr(self, 'case_' + str(attribute), lambda: default)()

    def case_name(self):
        if len(self.object.get("name").strip().split()) > self.name_len_limit:
            return "found", self.object.get("name")
        return "not", ""

    def case_age(self):
        if int(self.object.get("age")) >= self.age_limit:
            return "found", self.object.get("age")
        return "not", ""
        
    def case_surname(self):
        if len(self.object.get("surname").strip().split()) > self.name_len_limit:
            return "found", self.object.get("surname")
        return "not", ""

my_switch = ArgumentProcessor()