# TODO: set the name, surname, consent, language & location properties of the user on the profile


class UserProfile:
    w_id = f_name = s_name = consent_given = language = location = request_object = None

    def __init__(self, request_object):
        self.request_object = request_object
        # print("[][][][][][][][]", request_object)
        self.processArgs()
        
    def processArgs(self):
        r = self.request_object
        self.f_name = r.args.get("name")
        self.s_name = r.args.get("surname")
        self.w_id = r.args.get("whatsapp_id")
        self.consent_given = r.args.get("consent")
        self.language = r.args.get("language")
        self.location = r.args.get("location")
        # print(">>>>>>>>>", self.w_id)

    def __str__(self):
        return f"{self.f_name} - {self.s_name} - {self.language} - {self.language} - {self.w_id}"
