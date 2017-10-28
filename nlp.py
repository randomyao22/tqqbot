# -*- coding: utf-8 -*-

def onQQMessage(bot, contact, member, content):
    if '@晃晃悠悠' in content or '@ME' in content:
        from google.cloud import language
        client = language.LanguageServiceClient()
        document = language.types.Document(
            content=content,
            type='PLAIN_TEXT',
        )
        response = client.analyze_entities(
            document=document,
            encoding_type='UTF32',
        )
        reply = 'Entities: '
        types = ['UNKNOWN','PERSON','LOCATION','ORGANIZATION','EVENT','WORK_OF_ART','CONSUMER_GOOD','OTHER']              
        for entity in response.entities:
            reply += '{}'.format(entity.name)
            reply += ' type: {}'.format(types[entity.type])
        bot.SendTo(contact, reply)
