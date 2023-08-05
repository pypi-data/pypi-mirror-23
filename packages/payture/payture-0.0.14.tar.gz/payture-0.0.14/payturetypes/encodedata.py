class EncodeString(object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getPropertiesString(self):
        listattrs = dir(self)
        result = ""
        for elem in listattrs:
            if(elem.startswith('_') or elem.endswith('_') or elem.startswith('get')):
                continue
            result += elem + '=' +getattr(self, elem) + ';'
        return result


class PayInfo(EncodeString):

    def __init__(self, pan, emonth, eyear, cardHolder, secureCode, orderId, amount):
        self.PAN = pan
        self.EMonth = emonth
        self.EYear = eyear
        self.CardHolder = cardHolder
        self.SecureCode = secureCode
        self.OrderId = orderId
        self.Amount = amount



class Card(EncodeString):
    def __init__(self, cardNum, eMonth, eYear, cardHolder, secureCode, cardId = None ):
        self.CardNumber = cardNum
        self.EMonth = eMonth
        self.EYear = eYear
        self.CardHolder = cardHolder
        self.SecureCode = secureCode
        self.CardId = cardId
        super().__init__(self)


class Customer(EncodeString):
    def __init__(self, login, password, phone=None, email=None):
        self.VWUserLgn = login
        self.VWUserPsw = password
        self.PhoneNumber = phone
        self.Email = email

class Data(EncodeString):
    def __init__(self, sessionType, ip,  **kwargs):
        self.SessionType = sessionType
        self.IP = ip
        for key, value in kwargs.items():
            if(key == 'OrderId'):
                self.OrderId = value
            elif(key == 'Amount'):
                self.Amount = value
            elif(key == 'Language'):
                self.Language = value
            elif(key == 'TemplateTag'):
                self.TemplateTag = value
            elif(key == 'Url'):
                self.Url = value
            elif(key == 'Product'):
                self.Product = value
            elif(key == 'Total'):
                self.Total = value
            elif(key == 'ConfirmCode'):
                self.ConfirmCode = value
            elif(key == 'CustomFields'):
                self.CustomFields = value


