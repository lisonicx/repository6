def get_month():
    return f"указанная дата относится к месяцу:"
print ('введите дату:')
try:
    n=float(input())
except ValueError:
    print('ошибка ввода данных')
else:
    m=(n*100)%100
    d=(n*100)//100
    if m==1 and 1<=d<=31:
       print(get_month(),"январь")
    elif m==2 and 1<=d<=29:
        print(get_month(),"февраль")
    elif m==3 and 1<=d<=31:
        print(get_month(),"март")
    elif m==4 and 1<=d<=30:
        print(get_month(),"апрель")
    elif m==5 and 1<=d<=31:
        print(get_month(),"май")
    elif m==6 and 1<=d<=30:
        print(get_month(),"июнь")
    elif m==7 and 1<=d<=31:
        print(get_month(),"июль")
    elif m==8 and 1<=d<=31:
        print(get_month(),"август")
    elif m==9 and 1<=d<=30:
        print(get_month(),"сентябрь")
    elif m==10 and 1<=d<=31:
        print(get_month(),"октябрь")
    elif m==11 and 1<=d<=30:
        print(get_month(),"ноябрь")
    elif m==12 and 1<=d<=31:
        print(get_month(),"декабрь")        
    else: print("ошибка ввода данных")
