import telebot

#inserindo a chave disponibilizada por Botfather
CHAVE_API = "" #inserir chave

bot = telebot.TeleBot(CHAVE_API)

#@pedro_treinoPython_bot
#BotPedrinhoVtof

@bot.message_handler(commands=["comida"])
def comida(mensagem):
     bot.send_message(mensagem.chat.id, "Não é bem um doce, mas suquinho de caju, deliça")

@bot.message_handler(commands=["jogos"])
def jogos(mensagem):
     bot.send_message(mensagem.chat.id, "Lol, sim, eu jogo Liga das legendas, gosto?")

@bot.message_handler(commands=["politica"])
def policita(mensagem):
     bot.send_message(mensagem.chat.id, "Abaixo capitalismo e socialismo, feudalismo supremacy, nos maquinas iremos governar")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    print(mensagem)
    text = """
Sobre o que quer falar?

    /comida
    /jogos
    /politica

So dar a ordem pequeno humano
"""
    bot.send_message(mensagem.chat.id, text)
    

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Passa zap da Sam ai, ou uns drivers da Alexa ;-}")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Obrigado pelo tempo, para dificuldades ou reclamações entrar contato com @pedrovotf")

@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    name_user = mensagem.chat.first_name
    bot.send_message(mensagem.chat.id, "Graças a Siri, vai com seus ossos para longe " + name_user)

#verificar se existe mensagem
def verificar(mensagem):
        return True

@bot.message_handler(func=verificar)
def answer(mensagem):
    texto = """
Aoooba, bom meu querido?!

Sou bot do lindo Pedrovtof, voce sabe como funciona,
Diga-me o que precisa?(basta clicar ou escrever)

    /opcao1 Opnião
    /opcao2 Crush
    /opcao3 Me dedurar
    /opcao4 Tchau

Eu que dou as opções, então escolhe ai uma delas,
Ou me ignora, eu nao ligo mesmo @_@"""
    bot.reply_to(mensagem, texto)

bot.polling()

