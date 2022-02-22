import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import xgboost
# from Codigo.Modelos.Eto_models import xgb
from Modelos.Eto_experiments import get_x2, get_x30,resource_ranking,column_Filter,list_Format,tab_to_tab_lags
from Tratamento.variaveis import latitude_2,  altitude_2, sigma, G, Gsc
from Tratamento.Eto_generator import gera_serie
from Modelos.Eto_models import arvores,florestasAleatorias,xgbs,RandomizedSearchsF,gridSearchFs,gridSearchXgbs,gridSearchAs
import os.path
import seaborn as sns 
import matplotlib as plt
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore") 
# from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
path= 'C:/Users/Ray/Documents/'

# data_Ray = pd.read_csv(path+'IC/2020_Ic/Dados/Dados_PP_Eto.csv') 
# eto_Ray = gera_serie(data_Ray, latitude_2, altitude_2, Gsc, sigma, G)
# data_Ray["Eto"] = eto_Ray
# atributeR = ["Eto", "temp_media", "temp_max","radiacao"]
# resultado = get_x30(data_Ray, atributeR, ['Eto'])
# if(os.path.exists(path+'IC/2020_Ic/Dados/Tabela30R_Lags.csv')):
#   print("CSV Ray já existente !")
# else:
#   print("Exportando dados Ray ...")
#   resultado[0].to_csv(path+'IC/2020_Ic/Dados/Tabela30R_Lags.csv')
#   print("Concluido !")


data_Patricia_Eto = pd.read_csv(path+'IC/2020_Ic/Dados/ETo_setelagoas.csv') 
data_Patricia= pd.read_csv(path+'IC/2020_Ic/Dados/variaveis_setelagoas.csv')
data_Patricia["Eto"] = data_Patricia_Eto["Eto"]
if(os.path.exists(path+'IC/2020_Ic/Dados/data_PEto.csv')):
  print("JÁ EXISTE")
else:
  data_Patricia.to_csv(path+'IC/2020_Ic/Dados/data_PEto.csv')

atributeP= [ "Tmax","Tmean","I","UR","V","Tmin","J"]
resultadoP=get_x30(data_Patricia,atributeP,['Eto'])
if(os.path.exists(path+'IC/2020_Ic/Dados/Tabela30P_Lags.csv')):
  print("CSV patricia já existente !")
else:
  print("Exportando dados Patricia ...")
  resultadoP[0].to_csv(path+'IC/2020_Ic/Dados/Tabela30P_Lags.csv')
  print("Concluido !")

print("\n Para o dataframe Brasilia")



url=('https://raw.githubusercontent.com/RayBasilio123/database/main/INMET/CSV/J_Database/MANAUS_J_2014_2020.csv')
data_Pampulha = pd.read_csv(url, sep=",", encoding = "ISO-8859-1")
data_Pampulha=data_Pampulha.drop(columns=['Unnamed: 0'])

atributeReg = [ 'vento'	,'radiacao',	'temp_max',	'temp_min',	'umi_max',	'umi_min',	'umi_rel',	'press_atm',	'temp_media','J']
resultadoPampulha = get_x30(data_Pampulha, atributeReg, ['Eto'])
#Manaus
# -----------Para----1----dias --------
lista_Formatada_1=  [['umi_rel', 'umi_min', 'temp_media', 'temp_max', 'radiacao', 'umi_max', 'temp_min'], [[1, 2], [1], [1], [1], [1], [1], [1]], ['Eto'], [1, 2]]
lista_Formatada_2=  [['umi_min', 'umi_rel', 'temp_max', 'temp_media', 'radiacao', 'vento', 'umi_max'], [[1], [1, 16], [1], [2, 1], [1], [1], [1]], ['Eto'], [1]]
#  -----------Para----3----dias --------
# lista_Formatada_1=  [['umi_rel'], [[3, 13, 9, 8, 4, 12, 14, 7, 10]], ['Eto'], [3]]
# lista_Formatada_2=  [['J', 'umi_min'], [[4, 5, 19, 15, 6, 13, 7, 21], [4]], ['Eto'], [13]]
#  -----------Para----7----dias --------
# lista_Formatada_1=  [['umi_rel'], [[13, 9, 8, 12, 14, 7, 10, 11]], ['Eto'], [13, 8]]
# lista_Formatada_2=  [['temp_max', 'J', 'umi_rel', 'umi_min'], [[8], [13, 14, 16, 9, 27, 10], [9, 13], [16]], [], []]
#  -----------Para----10----dias --------
# lista_Formatada_1=  [['umi_rel'], [[13, 12, 14, 10, 11, 15, 16, 17]], ['Eto'], [13, 14]]
# lista_Formatada_2=  [['J', 'umi_min'], [[21, 14, 30, 12, 11, 23, 24, 16, 15], [13]], [], []]

 
# arvores(data_Pampulha,[lista_Formatada_1,lista_Formatada_2],"Eto")

xgbs(data_Pampulha,[lista_Formatada_1,lista_Formatada_2],"Eto")

# florestasAleatorias(data_Pampulha,[lista_Formatada_1,lista_Formatada_2],"Eto")