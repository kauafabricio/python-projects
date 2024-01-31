from secrets import ACCESS_API, ACCESS_API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import tweepy

# No momento em que eu estava codando isto, dia 31 de janeiro de 2024, o TwitterAPI com X API v2 free que é o meu caso, é muito limitado, então não foi possível acessar os tweets pelo get_place_trends.
# Para ter acesso, é necessário pagar pelo serviço.
# Este é um código simples, que faz conexão com TwitterAPI através da biblioteca tweepy, acessando os trends do Brasil pelo ID.

BRAZIL_WOE_ID = 23424768

auth = tweepy.OAuth1UserHandler(consumer_key=ACCESS_API, consumer_secret=ACCESS_API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

trends = api.get_place_trends(id=BRAZIL_WOE_ID)

for tweet in trends:
    print(tweet)
