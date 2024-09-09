from config import VULA_VULA as vula_token
import json
import requests


def test():

    entityRec("Diepkloof. My name is Zinhle Keswa. WeThinkCode", "27671401556")



def entityRec(sentence, contact):
    print("Found the sentence ===> ", sentence)

    # Endpoint URL
    url = 'https://vulavula-services.lelapa.ai/api/v1/entity_recognition/process'

    # Headers
    headers = {
        'Content-Type': 'application/json',
        'X-CLIENT-TOKEN': vula_token # Replace '<INSERT_TOKEN>' with your actual client token
    }

    # Request body
    data = {
        "encoded_text": sentence
    }

    # Sending POST request
    response = requests.post(url, headers=headers, json=data)
    print("")

    for entity in response.json()['entities']:

        entity = dict(entity)
        try:
            comp = entity['entity']
            match (comp):
                case "person":
                    # person = entity['person']
                    person = entity.get('word', None)
                    print("person", person)

                case "location":
                    # location = entity['location']
                    location = entity.get('word', None)
                    print("location", location)

                case "organisation":
                    organisation = entity.get('word', None)
                    # organisation = entity['organisation']
                    print("organisation", organisation)

        except KeyError:
            continue
    



    print("Found these values", person, location, organisation)
    
    return person, location, organisation





    



    # TODO: figure out how to access entity rec response
    

        




if __name__ == "__main__":
    test()