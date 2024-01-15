import pyautogui
import time 

#pyautogui.PAUSE = 1

# Variáveis 
linkMovidesk = "https://enterprise.movidesk.com/Account/Login"
ticketsFrancis = "Tickets Francis"
ticketsDaniel = "Tickets Daniel"
ticketsPaulo = "Tickets Paulo"
ticketsLucas = "Tickets Lucas"
ticketsMarcos = "Tickets Marcos"

mailLorraine = "lorraine.ferreira@projuris.com.br"
mailMorgana = "morgana.lima@softplan.com.br"
mailTati = "tatiane.martins@softplan.com.br"

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 1 - Abrir navegador:
pyautogui.press("win")
time.sleep(1)
pyautogui.write("chorme")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2.5)

# 2 - Logar no Movidesk
pyautogui.write(linkMovidesk)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=1141, y=662)
time.sleep(2)
pyautogui.click(x=253, y=521)
time.sleep(2.3)

# 3 - Gerar Relatório 1 Francis ////////// Só nessa vai precisar descer a pagina toda
pyautogui.click(x=18, y=225)
time.sleep(2)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
pyautogui.click(x=367, y=698)
time.sleep(0.5)

# Nome Francis
pyautogui.click(x=215, y=414)
time.sleep(1)

# **** Sequência de click do relatório ****
pyautogui.click(x=921, y=204)
time.sleep(0.5)
pyautogui.click(x=926, y=308)
time.sleep(0.5)
pyautogui.click(x=837, y=380)
time.sleep(3.5)

# **** Renomear relatório 1

pyautogui.click(x=388, y=734)
time.sleep(1.3)
pyautogui.click(x=111, y=270)
time.sleep(1.5)
pyautogui.click(x=306, y=202)
time.sleep(1.2)
pyautogui.click(x=280, y=101)
time.sleep(1)
pyautogui.write(ticketsFrancis)
pyautogui.press("enter")

# 3 - Gerar Relatório 2 Daniel

# **** Voltar pro google
pyautogui.click(x=204, y=738)
time.sleep(0.9)

# Separação de cada relatório (Não copiar)
pyautogui.click(x=188, y=449)
time.sleep(0.9)

# ****
pyautogui.click(x=921, y=204)
time.sleep(0.8)
pyautogui.click(x=926, y=308)
time.sleep(0.8)
pyautogui.click(x=837, y=380)
time.sleep(4)

# * Renomear relatório 2

pyautogui.click(x=388, y=734)
time.sleep(1.3)
pyautogui.click(x=111, y=270)
time.sleep(1.5)
pyautogui.click(x=306, y=202)
time.sleep(1.2)
pyautogui.click(x=280, y=101)
time.sleep(1)
pyautogui.write(ticketsDaniel)
pyautogui.press("enter")


# GERAR RELATÓRIO 3 PAULO

# **** Voltar pro google
pyautogui.click(x=204, y=738)
time.sleep(0.8)

pyautogui.click(x=171, y=534)

# **** Sequência de click do relatório ****
pyautogui.click(x=921, y=204)
time.sleep(0.5)
pyautogui.click(x=926, y=308)
time.sleep(0.5)
pyautogui.click(x=837, y=380)
time.sleep(3.5)

# **** Renomear relatório (PADRÃO, MUDAR SÓ O NOME DO RELATÓRIO)

pyautogui.click(x=388, y=734)
time.sleep(1.3)
pyautogui.click(x=111, y=270)
time.sleep(1.5)
pyautogui.click(x=306, y=202)
time.sleep(1.2)
pyautogui.click(x=280, y=101)
time.sleep(1)
pyautogui.write(ticketsPaulo)
pyautogui.press("enter")


# Gerar relatório 4 Lucas

# **** Voltar pro google
pyautogui.click(x=204, y=738)
time.sleep(0.8)

# Relatório Lucas
pyautogui.click(x=210, y=585)
time.sleep(0.9)

# **** Sequência de click do relatório ****
pyautogui.click(x=921, y=204)
time.sleep(0.5)
pyautogui.click(x=926, y=308)
time.sleep(0.5)
pyautogui.click(x=837, y=380)
time.sleep(3.5)

# **** Renomear relatório (PADRÃO, MUDAR SÓ O NOME DO RELATÓRIO)

pyautogui.click(x=388, y=734)
time.sleep(1.3)
pyautogui.click(x=111, y=270)
time.sleep(1.5)
pyautogui.click(x=306, y=202)
time.sleep(1.2)
pyautogui.click(x=280, y=101)
time.sleep(1)
pyautogui.write(ticketsLucas)
pyautogui.press("enter")


# Gerar relatório 5 Marcos

# **** Voltar pro google
pyautogui.click(x=204, y=738)
time.sleep(0.8)

# Relatório Marcos
pyautogui.click(x=113, y=625)
time.sleep(0.9)

# **** Sequência de click do relatório ****
pyautogui.click(x=921, y=204)
time.sleep(0.5)
pyautogui.click(x=926, y=308)
time.sleep(0.5)
pyautogui.click(x=837, y=380)
time.sleep(3.5)

# **** Renomear relatório (PADRÃO, MUDAR SÓ O NOME DO RELATÓRIO)

pyautogui.click(x=388, y=734)
time.sleep(1.3)
pyautogui.click(x=111, y=270)
time.sleep(1.5)
pyautogui.click(x=306, y=202)
time.sleep(1.2)
pyautogui.click(x=280, y=101)
time.sleep(1)
pyautogui.write(ticketsMarcos)
pyautogui.press("enter")

#////////////////////////////////// COMEÇO DO ENVIO AUTOMÁTICO DOS RELATÓRIOS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# Abertura do E-mail
pyautogui.press("win")
time.sleep(0.8)
pyautogui.write("email")
time.sleep(0.8)
pyautogui.press("enter")
time.sleep(2.5)

# Criando um novo e-mail


pyautogui.click(x=78, y=99)
time.sleep(0.8)
pyautogui.click(x=688, y=192)
# Colocando o e-mail de quem vai receber
pyautogui.write(mailLorraine)
time.sleep(0.8)
pyautogui.press("space")
time.sleep(0.8)
pyautogui.press("enter")
time.sleep(0.8)
pyautogui.write(mailMorgana)
time.sleep(0.8)
pyautogui.press("space")
time.sleep(0.8)
pyautogui.press("enter")
pyautogui.write(mailTati)
pyautogui.press("space")
time.sleep(0.8)
pyautogui.press("enter")
time.sleep(0.8)
pyautogui.click(x=784, y=214)
time.sleep(0.8)
# Adicionando os arquivos

## Abrindo a pasta de downloads (repete até acabar todos)
pyautogui.click(x=753, y=53)
time.sleep(1)
pyautogui.click(x=684, y=98)
time.sleep(1)
pyautogui.click(x=185, y=370)
time.sleep(1)
#///////////////////////////////

# Escolhendo o primeiro arquivo
pyautogui.click(x=405, y=313)
time.sleep(0.8)
pyautogui.click(x=793, y=658)

## Abrindo a pasta de downloads (repete até acabar todos)
time.sleep(1)
pyautogui.click(x=684, y=98)
time.sleep(1)
pyautogui.click(x=185, y=370)
time.sleep(1)
#///////////////////////////////

# Escolhendo o segundo arquivo
pyautogui.click(x=369, y=332)
time.sleep(0.8)
pyautogui.click(x=793, y=658)

## Abrindo a pasta de downloads (repete até acabar todos)
time.sleep(1)
pyautogui.click(x=684, y=98)
time.sleep(1)
pyautogui.click(x=185, y=370)
time.sleep(1)
#///////////////////////////////

# Escolhendo o terceiro arquivo
pyautogui.click(x=373, y=354)
time.sleep(0.8)
pyautogui.click(x=793, y=658)

## Abrindo a pasta de downloads (repete até acabar todos)
time.sleep(1)
pyautogui.click(x=684, y=98)
time.sleep(1)
pyautogui.click(x=185, y=370)
time.sleep(1)
#///////////////////////////////

# Escolhendo o quarto arquivo
pyautogui.click(x=381, y=374)
time.sleep(0.8)
pyautogui.click(x=793, y=658)

## Abrindo a pasta de downloads (repete até acabar todos)
time.sleep(1)
pyautogui.click(x=684, y=98)
time.sleep(1)
pyautogui.click(x=185, y=370)
time.sleep(1)
#///////////////////////////////

# Escolhendo o quinto arquivo
pyautogui.click(x=375, y=396)
time.sleep(0.8)
pyautogui.click(x=793, y=658)


#////////////////////////////////  ENVIO DO E-MAIL  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

pyautogui.click(x=1277, y=49)
