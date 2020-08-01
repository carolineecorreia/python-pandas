# -*- coding: utf-8 -*-
"""Tarefa30-06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JsfD515JrR50dpwFG6K_QwL0JUuYZsm8
"""

import pandas as pd
import datetime
import numpy as np

superativos = pd.read_csv("Profs_Superativos.csv")

prev_junho = pd.read_csv("PREVISUL_JUNHO.csv")
prev_abr_A_1 = pd.read_csv("Previsul_A_abr_1.csv")
prev_abr_A_2 = pd.read_csv("Previsul_A_abr_2.csv")
prev_abr_A_3 = pd.read_csv("Previsul_A_abr_3.csv")
prev_maio = pd.read_csv("Previsul_MAIO.csv")

profs_GA = pd.read_csv("Profs_G_A.csv")
profs_GB = pd.read_csv("Profs_G_B.csv")

total_SP = pd.read_csv("TOTAL_SUPERDIGITAL_ABR_MAI.csv")
superdigital_junho = pd.read_csv("Superdigital_JUNHO.csv")

cpfs_df = pd.read_csv("profs_cpfs.csv")

interessados = pd.read_csv("interessados_conta_digital.csv")

cpfs_df

#Excluindo todos os e-mails que são da Previsul:

todo_mundo_previsul = pd.concat([superdigital_junho,interessados,total_SP,prev_abr_A_1,prev_abr_A_2,prev_abr_A_3,prev_maio,prev_junho]).drop_duplicates(keep='first')

print(len(todo_mundo_previsul))

final = pd.concat([superativos, todo_mundo_previsul,todo_mundo_previsul]).drop_duplicates(keep=False)

print(len(final))

GA_random = profs_GA.sample(frac=1)

amostra_GA = GA_random.iloc[0:4000]

print(len(amostra_GA))

superdigital_final = pd.concat([final,amostra_GA]).drop_duplicates(keep='first')

#superdigital_final.to_csv(r'superdigital_final.csv', index = False)

len(superdigital_final)

cpfs_df.rename(columns={"email":"Email"},inplace = True)

emails_e_cpfs = pd.merge(superdigital_final,cpfs_df, on = 'Email', how = 'left')

emails_e_cpfs.drop_duplicates(keep = 'first')

emails_e_cpfs.rename(columns={"fiscal_id":"CPF"},inplace = True)

emails_e_cpfs.dropna()

emails_e_cpfs['CPF'].to_csv(r'superdigital_cpfs.csv', index = False)
emails_e_cpfs['Email'].to_csv(r'superdigital_emails.csv', index = False)

emails_e_cpfs

cpfs_com_email = cpfs_julho['cpfs_final'].tolist()

print(len(cpfs_com_email))

emails_com_cpf = cpfs_df.loc[cpfs_df['fiscal_id'].isin(cpfs_com_email)]['email'].drop_duplicates(keep='first')


print(len(emails_com_cpf))

#Com o que sobrou dos Profs Superativos (usando se necessário o Grupo A e Grupo B... excluir todo mundo que é mês anterior 
#Previsul e que é Superdigital).  Criar csv da Previsul Julho. (8.5k emails).

pt_1 = pd.concat([superativos,final, final]).drop_duplicates(keep=False)

print(len(pt_1))

previsul_julho = pt_1.drop_duplicates(keep='first')

previsul_julho_rand = previsul_julho.sample(n=8500)

print(len(previsul_julho_rand))

previsul_julho_rand.to_csv(r'Previsul Julho.csv', index = False)

len(previsul_julho_rand)
