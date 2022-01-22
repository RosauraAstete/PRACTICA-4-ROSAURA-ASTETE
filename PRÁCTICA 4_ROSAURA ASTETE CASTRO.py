#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Problemas Diversos

import os
print(os.getcwd())


# In[4]:


# 1

num = int(input("Ingrese un número entero entre 1 y 10: "))

file = 'Tabla-' + str(num) + '.txt'

with open (file , 'w') as f:
    
    for i in range (1 , 13):
        f.write ( str(num) + ' x ' + str(i) + ' = ' + str(num * i) + '\n')


# In[3]:


# 2

num = int(input("Ingrese un número entero entre 1 y 10: "))

try:
    
    fichero = open (f'./Tabla-{num}.txt' , 'r')
    texto = fichero.read()
    fichero.close()
    print(texto)
    
except:
    
    print("El fichero no existe.")


# In[13]:


# 3

n = int(input("Ingrese un número entero entre 1 y 10: "))
m = int(input("Ingrese otro número entero entre 1 y 10: "))

try:
    
    fichero = open (f'./Tabla-{n}.txt' , 'r')
    texto = fichero.readlines()
    linea = texto[m - 1]
    fichero.close()
    print(linea)
    
except:
    
    print("El fichero no existe.")


# In[19]:


# 4

import re

cadena_entrada = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
regex = r"@robot\d!"

print ( re.findall(regex,cadena_entrada) )


# In[21]:


# 5

cadena_entrada = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"

regex1 = r"User_mentions:\d"
regex2 = r"likes: \d"
regex3 = r"number of retweets: \d"

print ( re.findall(regex1,cadena_entrada) )
print ( re.findall(regex2,cadena_entrada) )
print ( re.findall(regex3,cadena_entrada) )


# In[36]:


# 6

tweet = "AIshadowhunters.txt aaaaand back to my literature review. At least i have a friendly cup of coffee to keep me company ouMYTAXES.txt I am worried that I won't get my $900 even though I paid tax last year"

regex = r'[AEIOUaeiou]{2,3}[a-zA-Z0-9]*.txt'

print ( re.findall (regex, tweet) )


# In[39]:


# 7

regex = r"[a-zA-Z0-9!#%&*$.]*@[a-zA-Z0-9]*[!#%&*$.]*.com"

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']

for example in emails:
    
    
    if re.match(regex, example):
        
        print(f"The email {example} is a valid email")
    else:
        print(f"The email {example} is invalid")



# In[2]:


# Problema 2 Validación de tarjetas de crédito

import re 

lista_prueba = ['4123456789123456' , '5123-4567-8912-3456', '61234-567-8912-3456', '4123356789123456' , '5133-3367-8912-3456', '5123 - 3567 - 8912 - 3456' ]

regex1 = r'[456]\d{3}(-?\d{4}){3}$'
regex2 = r'((\d)-?(?!(-?\2){3})){16}'

for numero in lista_prueba:
   
    valido1 = re.match(regex1 , numero)
    valido2 = re.match(regex2 , numero)
    
    if (valido1 and valido2):
        print ("Valid")
    else:
        print ("Invalid")


# In[ ]:





# In[ ]:




