from kivymd.uix.gridlayout import MDGridLayout
from kivy.config import Config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.core.window import Window

Window.size = (560, 910)
Config.set('kivy', 'keyboard_mode', 'systemanddock')

import matplotlib.pyplot as plt


def calculation_percents(months, start_deposit, percent, monthly_refill):
    sum_list = []
    muns_list = []
    add_sum = start_deposit

    for month in range(months):
        month_sum = add_sum * (1 + percent / 12)
        sum_list.append(month_sum)
        add_sum = month_sum + monthly_refill
        muns_list.append(month)
        print(add_sum)

    final_deposit = str(round(add_sum, 2))
    get_percents = str(round((float(final_deposit) - start_deposit), 2))
    all_add_sum = str(start_deposit)
    tax = str(round((float(get_percents) * 0.195), 2))
    net_profit = str(round((float(get_percents) - float(tax)), 2))

    return {"final_deposit": final_deposit,
            "get_percents": get_percents,
            "all_add_sum": all_add_sum,
            "tax": tax,
            "net_profit": net_profit,
            "muns_list": muns_list,
            "sum_list": sum_list}


def build_graph(muns_list, sum_list):
    plt.bar(muns_list, sum_list)
    plt.xlabel('Месяци инвистирования')
    plt.ylabel('Сумма депозита')
    plt.savefig('culc_graph.png')




class StartWindow(Screen):
    pass

class MainWindow(Screen):
    def calculation(self):
        try:
            months = int(self.muns_input.text)
            start_deposit = float(self.start_input.text)
            percent = float(self.year_percent_input.text) / 100
            monthly_refill = 1
        except:
            months = 1
            start_deposit = 1
            percent = 1
            monthly_refill = 1

        calc = calculation_percents(months, start_deposit, percent, monthly_refill)

        self.final_deposit.text = calc.get('final_deposit')
        self.get_percents.text = calc.get('get_percents')
        self.all_add_sum.text = calc.get('all_add_sum')
        self.tax.text = calc.get('tax')
        self.net_profit.text = calc.get('net_profit')

        build_graph(calc.get('muns_list'), calc.get('sum_list'))

        # self.graph_img.reload()

class InfoWindow(Screen):
    pass

class GraphWindow(Screen):
    pass
    # image = "culc_graph.png"
    # graph_img.source = image

class WindowManager(ScreenManager):
    pass




class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Light'
        with open("my.kv") as f:
            kv_file = Builder.load_string(f.read())
        return kv_file


app = MyApp()

if __name__ == '__main__':
    app.run()

"""
Box Layout - вертикально ореентированый (виджеты один под другим) и горизонтально ореентированый (виджеты в строку)
Grid Layout - расположение виджетов в сетку
Stack Layout - размещает виджеты в столбик/строку пока они помещаються на екран
Anchor Layout - фиксация виджета в определенном месте
Page Layout - размещение елементов конроля на разных страницах
Float Layout - указание абсолютных координат выджетов
Relative Layout
Scatter Layout - мультитач
"""
