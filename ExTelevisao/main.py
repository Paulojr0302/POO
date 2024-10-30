from televisao import Televisao

tv = Televisao(1, 99)

for x in range(0, 120):
    tv.muda_canal_para_cima()
print(tv.canal)  

for x in range(0, 129):
    tv.muda_canal_para_baixo()
print(tv.canal)  
