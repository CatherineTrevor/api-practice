#Currency Converter - www.101computing.net/currency-converter/
import json, urllib.request

#Request an API Key from https://free.currencyconverterapi.com/free-api-key
API_Key = "api_key"
#When requesting an API key, you will also be asked to verify your email. Please do so by following the instructions on the email you will receive.

if API_Key[0:6]=="Insert":
  print("You will not be able to run this code without a valid API Key. Please request an API key first and insert it on line 5 of this code.")
else:
  #See full lists of valid currencies on https://free.currencyconverterapi.com/api/v7/currencies
  validCurrencies = ["EUR","GBP","USD","JPY"]
  
  #Display banner
  print("$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€")
  print("$£¥€                            $£¥€")
  print("$£¥€     Currency Converter     $£¥€")
  print("$£¥€                            $£¥€")
  print("$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€")
  print("")
  print("List of currencies: ")
  print("  GBP - British Pound £")
  print("  JPY - Japanese Yen ¥")
  print("  EUR - Euro €")
  print("  USD - US Dollar $")
  print("")
  
  #Initialise key variables
  currencyFrom = ""
  currencyTo = ""
  amount = 0
  
  #Retrieve user inputs
  while not currencyFrom in validCurrencies:
    currencyFrom = input("Enter Currency to convert From: (e.g. GBP)").upper()
    
  while not currencyTo in validCurrencies:
    currencyTo = input("Enter Currency to convert To: (e.g. EUR)").upper()
  
  amount = float(input("Enter amount to convert: (e.g. 10.00)"))
  
  #A JSON request to retrieve the required exchange rate
  url = "https://free.currconv.com/api/v7/convert?apiKey=" + API_Key + "&q="+currencyFrom + "_" + currencyTo +"&compact=y"
  
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
     
  #Let's extract the required information
  exchangeRate=result[currencyFrom + "_" + currencyTo]
  rate = exchangeRate["val"]
  
  #Output exchange rate and converted amount
  print("")
  print("Exchange rate: 1 " + currencyFrom + " = " + str(rate) + " " + currencyTo)
  print(str(amount) + " " + currencyFrom + " = " + ("{0:.2f}".format(amount*rate)) + " " + currencyTo)