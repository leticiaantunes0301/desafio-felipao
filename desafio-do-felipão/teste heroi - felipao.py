heroi ="link"
xp =  3050
heroi_do_nivel = ""
if xp <= 1000 : 
    heroi_do_nivel = "ferro"
elif xp <= 2000 :
    heroi_do_nivel = "bronze"
elif xp <= 5000 :
    heroi_do_nivel = "prata"
elif xp <= 7000 :
    heroi_do_nivel = "ouro"
elif xp <= 8000 :
    heroi_do_nivel = "platina" 
elif xp <= 9000 :
    heroi_do_nivel = "ascendente"
elif xp <= 10000 :
    heroi_do_nivel = "imortal"
else :
    heroi_do_nivel = "radiante"

print(f"O Herói de nome {heroi} está no nível {heroi_do_nivel}")

    