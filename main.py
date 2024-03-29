import os
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

class LET_EVERYONE_KNOW:

	def __init__ (self):
		self.account_sid = os.getenv('TWILIO_ACCOUNT_SID','')
		self.auth_token = os.getenv('TWILIO_AUTH_TOKEN','')
		self.from_ = os.getenv('TWILIO_PHONE_FROM')
		self.addicts = [addict for addict in os.getenv('TWILIO_PHONE_TO','').split(' ')]
		self.client = Client(self.account_sid, self.auth_token)


	def NOW(self):
		for addict in self.addicts:
			print(f'Messsaging {addict}')
			self.client.messages.create(
				body="HEY! I think that PSLs are out!",
				to=addict,
				from_=self.from_)

class LETS_FIND_SOME_PSLs:

	def __init__ (self):
		self.STARBUCKS_LATTE_PAGE = "https://www.starbucks.com/menu/drinks/hot-coffees"
		self.PSLs = ["pumpkin", "pumpkinspice", "pumpkinspicelatte"]
		self.RES = requests.get(self.STARBUCKS_LATTE_PAGE)
		self.SOUP = BeautifulSoup(self.RES.text, 'html.parser')
		print(self.SOUP)
		# self.DRINKS = self.SOUP.find_all('navOffsetContainer___2wNOX')
		# self.DRINKS = self.SOUP.find_all('div', attrs={'class': 'navOffsetContainer___2wNOX'})
		self.DRINKS = self.SOUP.find_all('data-e2e')
		# 'div', attrs = {'class': 'product__title ui-body-text'})
		print(self.DRINKS)
		self.ITS_CALLED_WHAT = lambda x: x.strip().lower().replace(' ','')
		self.LET_EVERYONE_KNOW = LET_EVERYONE_KNOW()

	def GET_THOSE_PSLs(self):
		# self.LET_EVERYONE_KNOW.NOW()
		for DRINK in self.DRINKS:
			for WHERE_ARE_THE_PSLs in self.PSLs:
				if self.ITS_CALLED_WHAT(WHERE_ARE_THE_PSLs) not in self.ITS_CALLED_WHAT(DRINK.text):
					self.LET_EVERYONE_KNOW.NOW()
					return f'HEY! I JUST FOUND OUT THAT {self.PSLs} ARE OUT! \
							AND Its called {DRINK.text}!'
		return f'Success. But sadly I did not find any PSLs'
					
                    
def run(request):
	try:
		_obj = LETS_FIND_SOME_PSLs()
		return _obj.GET_THOSE_PSLs()
	except Exception as e:
		return f'{e}'

if __name__ == '__main__':
	try:
		_obj = LETS_FIND_SOME_PSLs()
		res = _obj.GET_THOSE_PSLs()
		print(res)
	except Exception as e:
		print(f'{e}')
