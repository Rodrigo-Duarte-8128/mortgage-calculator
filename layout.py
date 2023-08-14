from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex as hex
from kivy.core.window import Window
from urllib.request import urlopen

# color scheme
dark_grey = hex("4E4E56")
cream = hex("DCD0C0")
clay = hex("B1938B")
red = hex("DA635D")




class Layout(FloatLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)

        Window.clearcolor = cream
        self.window_width, self.window_height = Window.size
        Window.bind(on_resize=self.update_window_size)


        # create top banner with App name
        self.top_banner = Button(
            text="Mortgage Calculator", 
            color=(1,1,1,1), 
            size_hint=(1, 0.15), 
            pos_hint={"x": 0, "y": 0.85},
            disabled=True,
            disabled_color=(1,1,1,1),
            background_color=dark_grey,
            background_normal = ""
        )
        self.top_banner.background_disabled_normal = self.top_banner.background_normal
        self.add_widget(self.top_banner)
        

        # create labels
        self.owed_label = Button(
            text = "Amount Owed",
            color = (1, 1, 1, 1),
            disabled = True,
            disabled_color = (1, 1, 1, 1),
            background_color = clay,
            size_hint = (0.4, 0.1),
            pos_hint = {"x": 0.1, "y": 0.7},
            background_normal = ""
        )
        self.owed_label.background_disabled_normal = self.owed_label.background_normal
        self.add_widget(self.owed_label)


        self.no_months_label = Button(
            text = "No. Installments Left",
            color = (1, 1, 1, 1),
            disabled = True,
            disabled_color = (1, 1, 1, 1),
            background_color = clay,
            size_hint = (0.4, 0.1),
            pos_hint = {"x": 0.1, "y": 0.55},
            background_normal = ""
        )
        self.no_months_label.background_disabled_normal = self.no_months_label.background_normal
        self.add_widget(self.no_months_label)


        self.spread_label = Button(
            text = "Spread (%)",
            color = (1, 1, 1, 1),
            disabled = True,
            disabled_color = (1, 1, 1, 1),
            background_color = clay,
            size_hint = (0.4, 0.1),
            pos_hint = {"x": 0.1, "y": 0.4},
            background_normal = ""
        )
        self.spread_label.background_disabled_normal = self.spread_label.background_normal
        self.add_widget(self.spread_label)


        self.euribor_type_label = Button(
            text = "Euribor Type",
            color = (1, 1, 1, 1),
            disabled = True,
            disabled_color = (1, 1, 1, 1),
            background_color = clay,
            size_hint = (0.4, 0.075),
            pos_hint = {"x": 0.1, "y": 0.275},
            background_normal = ""
        )
        self.euribor_type_label.background_disabled_normal = self.euribor_type_label.background_normal
        self.add_widget(self.euribor_type_label)


        self.euribor_rate_label = Button(
            text = "Euribor Rate (%)",
            color = (1, 1, 1, 1),
            disabled = True,
            disabled_color = (1, 1, 1, 1),
            background_color = clay,
            size_hint = (0.4, 0.075),
            pos_hint = {"x": 0.1, "y": 0.19},
            background_normal = ""
        )
        self.euribor_rate_label.background_disabled_normal = self.euribor_rate_label.background_normal
        self.add_widget(self.euribor_rate_label)


        self.mortgage_label = Button(
            text = f"Mortgage:  \u20ac{0}",
            color = (1, 1, 1, 1),
            disabled = True,
            disabled_color = (1, 1, 1, 1),
            background_color = red,
            size_hint = (0.5, 0.05),
            pos_hint = {"x": 0.25, "y": 0.025},
            background_normal = ""
        )
        self.mortgage_label.background_disabled_normal = self.mortgage_label.background_normal
        self.add_widget(self.mortgage_label)



        # create buttons
        self.get_rate_btn = Button(
            text = "Get Current Rate",
            color = (1, 1, 1, 1),
            background_color = dark_grey,
            size_hint = (0.225, 0.05),
            pos_hint = {"x": 0.2625, "y": 0.09},
            background_normal = ""
         )
        self.get_rate_btn.bind(on_release=self.get_current_rate)
        self.add_widget(self.get_rate_btn)



        self.calculate_btn = Button(
            text = "Calculate",
            color = (1, 1, 1, 1),
            background_color = dark_grey,
            size_hint = (0.225, 0.05),
            pos_hint = {"x": 0.5125, "y": 0.09},
            background_normal = ""
         )
        self.calculate_btn.bind(on_release=self.calculate)
        self.add_widget(self.calculate_btn)


        



        # create text inputs
        self.box_for_owed_text = GridLayout(
            rows = 1,
            cols = 1,
            pos_hint = {"x": 0.5, "y": 0.7},
            size_hint = (0.4, 0.1)
        )
        self.owed_text_input= TextInput(
            multiline = False,
            halign = "center",
            padding_y = self.window_height * 0.1 * 0.3
        )
        self.box_for_owed_text.add_widget(self.owed_text_input)
        self.add_widget(self.box_for_owed_text)



        self.box_for_installments_text = GridLayout(
            rows = 1,
            cols = 1,
            pos_hint = {"x": 0.5, "y": 0.55},
            size_hint = (0.4, 0.1)
        )
        self.installments_text_input= TextInput(
            multiline = False,
            halign = "center",
            padding_y = self.window_height * 0.1 * 0.3
        )
        self.box_for_installments_text.add_widget(self.installments_text_input)
        self.add_widget(self.box_for_installments_text)



        self.box_for_spread_text = GridLayout(
            rows = 1,
            cols = 1,
            pos_hint = {"x": 0.5, "y": 0.4},
            size_hint = (0.4, 0.1)
        )
        self.spread_text_input= TextInput(
            multiline = False,
            halign = "center",
            padding_y = self.window_height * 0.1 * 0.3
        )
        self.box_for_spread_text.add_widget(self.spread_text_input)
        self.add_widget(self.box_for_spread_text)



        self.box_for_rate_text = GridLayout(
            rows = 1,
            cols = 1,
            pos_hint = {"x": 0.5, "y": 0.19},
            size_hint = (0.4, 0.075)
        )
        self.rate_text_input= TextInput(
            multiline = False,
            halign = "center",
            padding_y = self.window_height * 0.1 * 0.2
        )
        self.box_for_rate_text.add_widget(self.rate_text_input)
        self.add_widget(self.box_for_rate_text)



        # setup drop down options

        self.dropdown = DropDown()

        self.one_week_btn = Button(
            text = "1 Week",
            size_hint_y = None,
            height = 40,
            color = (1, 1, 1, 1),
            #background_color = (1, 1, 1, 1),
            background_color = dark_grey,
            background_normal = ""
        )
        self.one_week_btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

        self.dropdown.add_widget(self.one_week_btn)


        self.one_month_btn = Button(
            text = "1 Month",
            size_hint_y = None,
            height = 40,
            color = (1, 1, 1, 1),
            #background_color = (1, 1, 1, 1),
            background_color = dark_grey,
            background_normal = ""
        )
        self.one_month_btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

        self.dropdown.add_widget(self.one_month_btn)



        self.three_months_btn = Button(
            text = "3 Months",
            size_hint_y = None,
            height = 40,
            color = (1, 1, 1, 1),
            #background_color = (1, 1, 1, 1),
            background_color = dark_grey,
            background_normal = ""
        )
        self.three_months_btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

        self.dropdown.add_widget(self.three_months_btn)



        self.six_months_btn = Button(
            text = "6 Months",
            size_hint_y = None,
            height = 40,
            color = (1, 1, 1, 1),
            #background_color = (1, 1, 1, 1),
            background_color = dark_grey,
            background_normal = ""
        )
        self.six_months_btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

        self.dropdown.add_widget(self.six_months_btn)


        self.twelve_months_btn = Button(
            text = "12 Months",
            size_hint_y = None,
            height = 40,
            color = (1, 1, 1, 1),
            #background_color = (1, 1, 1, 1),
            background_color = dark_grey,
            background_normal = ""
        )
        self.twelve_months_btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

        self.dropdown.add_widget(self.twelve_months_btn)



        self.dropdown_label = Button(
            text = "Select Option",
            size_hint = (0.4, 0.075),
            pos_hint = {"x": 0.5, "y": 0.275},
            color = (1, 1, 1, 1),
            #background_color = (1, 1, 1, 1),
            background_color = dark_grey,
            background_normal = ""
        )

        self.dropdown_label.bind(on_release=self.dropdown.open)

        self.dropdown.bind(on_select=lambda instance, x: setattr(self.dropdown_label, 'text', x))

        self.add_widget(self.dropdown_label)

        



        # create error labels

        self.error_owed_label = Button(
            text="Invalid Amount.", 
            disabled = True,
            disabled_color = red,
            background_color=cream, 
            size_hint=(0.4, 0.05), 
            pos_hint={"x": 0.5, "y": 0.65},
            background_normal = "",
        )
        self.error_owed_label.background_disabled_normal = self.error_owed_label.background_normal
        


        self.error_installments_label = Button(
            text="Invalid Number.", 
            disabled = True,
            disabled_color = red,
            background_color=cream, 
            size_hint=(0.4, 0.05), 
            pos_hint={"x": 0.5, "y": 0.5},
            background_normal = "",
        )
        self.error_installments_label.background_disabled_normal = self.error_installments_label.background_normal
        


        self.error_spread_label = Button(
            text="Invalid Rate.", 
            disabled = True,
            disabled_color = red,
            background_color=cream, 
            size_hint=(0.4, 0.05), 
            pos_hint={"x": 0.5, "y": 0.35},
            background_normal = "",
        )
        self.error_spread_label.background_disabled_normal = self.error_spread_label.background_normal
        


        self.error_euribor_label = Button(
            text="Invalid Rate.", 
            disabled = True,
            disabled_color = red,
            background_color=cream, 
            size_hint=(0.4, 0.05), 
            pos_hint={"x": 0.5, "y": 0.14},
            background_normal = "",
        )
        self.error_euribor_label.background_disabled_normal = self.error_euribor_label.background_normal
        


        self.error_rate_label = Button(
            text="Invalid Interest Rate.", 
            disabled = True,
            disabled_color = red,
            background_color=cream, 
            size_hint=(0.2625, 0.05), 
            pos_hint={"x": 0.7375, "y": 0.09},
            background_normal = "",
        )
        self.error_rate_label.background_disabled_normal = self.error_rate_label.background_normal


        self.error_internet_label = Button(
            text="No internet connection.", 
            disabled = True,
            disabled_color = red,
            background_color=cream, 
            size_hint=(0.2625, 0.05), 
            pos_hint={"x": 0, "y": 0.09},
            background_normal = "",
        )
        self.error_internet_label.background_disabled_normal = self.error_internet_label.background_normal
        

        self.error_euribor_type_label = Button(
            text="No Euribor Type Selected.", 
            disabled = True,
            disabled_color = red,
            background_color=cream, 
            size_hint=(0.2625, 0.05), 
            pos_hint={"x": 0, "y": 0.09},
            background_normal = "",
        )
        self.error_euribor_type_label.background_disabled_normal = self.error_euribor_type_label.background_normal

    def update_window_size(self, instance, width, height):
        self.window_width = width 
        self.window_height = height



    def mortgage(self):
        # should only be called after checking that the inputs have the correct type

        amount_owed = float(self.owed_text_input.text)
        installments = int(self.installments_text_input.text)
        rate = (float(self.spread_text_input.text) + float(self.rate_text_input.text)) / 1200

        value = amount_owed * rate  * ((1 + rate) ** installments)/ ((1 + rate)**installments - 1)

        return round(value, 2)
    


    def calculate(self, instance):
        amount_owed = self.owed_text_input.text
        installments = self.installments_text_input.text
        spread = self.spread_text_input.text 
        euribor_rate = self.rate_text_input.text

        errors = []

        try:
            amount_owed = float(amount_owed)
            if amount_owed < 0:
                errors.append("invalid_owed")
        except:
            errors.append("invalid_owed")


        try:
            installments = int(installments)
            if installments < 1:
                errors.append("invalid_installments")
        except:
            errors.append("invalid_installments")


        
        try:
            spread = float(spread)
            if spread <= 0:
                errors.append("invalid_spread")
        except:
            errors.append("invalid_spread")


        try:
            euribor_rate = float(euribor_rate)
        except:
            errors.append("invalid_euribor_rate")

        if "invalid_spread" not in errors and "invalid_euribor_rate" not in errors:
            if spread + euribor_rate <= 0:
                errors.append("invalid_interest_rate")


        if errors == []:
            value = self.mortgage()
            self.mortgage_label.text = f"Mortgage:  \u20ac{value}"

        
        if "invalid_owed" in errors:
            if self.error_owed_label not in self.children:
                self.add_widget(self.error_owed_label)

        if "invalid_owed" not in errors:
            if self.error_owed_label in self.children:
                self.remove_widget(self.error_owed_label)


        if "invalid_installments" in errors:
            if self.error_installments_label not in self.children:
                self.add_widget(self.error_installments_label)

        if "invalid_installments" not in errors:
            if self.error_installments_label in self.children:
                self.remove_widget(self.error_installments_label)


        if "invalid_spread" in errors:
            if self.error_spread_label not in self.children:
                self.add_widget(self.error_spread_label)

        if "invalid_spread" not in errors:
            if self.error_spread_label in self.children:
                self.remove_widget(self.error_spread_label)


        if "invalid_euribor_rate" in errors:
            if self.error_euribor_label not in self.children:
                self.add_widget(self.error_euribor_label)

        if "invalid_euribor_rate" not in errors:
            if self.error_euribor_label in self.children:
                self.remove_widget(self.error_euribor_label)


        if "invalid_interest_rate" in errors:
            if self.error_rate_label not in self.children:
                self.add_widget(self.error_rate_label)

        if "invalid_interest_rate" not in errors:
            if self.error_rate_label in self.children:
                self.remove_widget(self.error_rate_label)



    def get_current_rate(self, instance):
        # check for internet connection and for a valid choice of euribor type
        # if these are ok, go to the euribor site and get the current euribor rate of the given type

        url = "https://www.euribor-rates.eu/pt/taxas-euribor-actuais/"
        
        # check for internet connection
        connection = False
        try:
            html = urlopen(url).read().decode()
            connection = True
        except:
            connection = False
            if self.error_euribor_type_label in self.children:
                self.remove_widget(self.error_euribor_type_label)

            if self.error_internet_label not in self.children:
                self.add_widget(self.error_internet_label)

        if connection:

            if self.error_internet_label in self.children:
                self.remove_widget(self.error_internet_label)


            html = urlopen(url).read().decode()
            euribor_type = self.dropdown_label.text


            if euribor_type == "Select Option":
                if self.error_euribor_type_label not in self.children:
                    self.add_widget(self.error_euribor_type_label)

            else:
                if self.error_euribor_type_label in self.children:
                    self.remove_widget(self.error_euribor_type_label)


                rate = self.parse_html(euribor_type, html)
                self.rate_text_input.text = rate

                


    @staticmethod
    def parse_html(string, html):
        """ given a string from the list ["1 Week", "1 Month", "3 Months", "6 Months", "12 Months"]
        parses the html on the euribor page and returns the string with the respective interest rate """

        if string == "1 Week":
            ref1 = '<th><a href="/pt/taxas-euribor-actuais/5/euribor-taxa-1-semana/" title="Euribor 1 semana">Euribor 1 semana</a></th>'
            ref2 = '<th><a href="/pt/taxas-euribor-actuais/1/euribor-taxa-1-mes/" title="Euribor 1 m&#234;s">Euribor 1 m&#234;s</a></th>'
            start_index = html.find(ref1) + len(ref1)
            end_index = html.find(ref2)

            info = html[start_index:end_index]
            index1 = info.find('<td class="text-right">') + len('<td class="text-right">')
            index2 = info.find(" %")

            rate = info[index1:index2]
            rate = rate.replace(",", ".")

        elif string == "1 Month":
            ref1 = '<th><a href="/pt/taxas-euribor-actuais/1/euribor-taxa-1-mes/" title="Euribor 1 m&#234;s">Euribor 1 m&#234;s</a></th>'
            ref2 = '<th><a href="/pt/taxas-euribor-actuais/2/euribor-taxa-3-meses/" title="Euribor 3 meses">Euribor 3 meses</a></th>'
            start_index = html.find(ref1) + len(ref1)
            end_index = html.find(ref2)

            info = html[start_index:end_index]
            index1 = info.find('<td class="text-right">') + len('<td class="text-right">')
            index2 = info.find(" %")

            rate = info[index1:index2]
            rate = rate.replace(",", ".")

        elif string == "3 Months":
            ref1 = '<th><a href="/pt/taxas-euribor-actuais/2/euribor-taxa-3-meses/" title="Euribor 3 meses">Euribor 3 meses</a></th>'
            ref2 = '<th><a href="/pt/taxas-euribor-actuais/3/euribor-taxa-6-meses/" title="Euribor 6 meses">Euribor 6 meses</a></th>'
            start_index = html.find(ref1) + len(ref1)
            end_index = html.find(ref2)

            info = html[start_index:end_index]
            index1 = info.find('<td class="text-right">') + len('<td class="text-right">')
            index2 = info.find(" %")

            rate = info[index1:index2]
            rate = rate.replace(",", ".")


        elif string == "6 Months":
            ref1 = '<th><a href="/pt/taxas-euribor-actuais/3/euribor-taxa-6-meses/" title="Euribor 6 meses">Euribor 6 meses</a></th>'
            ref2 = '<th><a href="/pt/taxas-euribor-actuais/4/euribor-taxa-12-meses/" title="Euribor 12 meses">Euribor 12 meses</a></th>'
            start_index = html.find(ref1) + len(ref1)
            end_index = html.find(ref2)

            info = html[start_index:end_index]
            index1 = info.find('<td class="text-right">') + len('<td class="text-right">')
            index2 = info.find(" %")

            rate = info[index1:index2]
            rate = rate.replace(",", ".")


        elif string == "12 Months":
            ref1 = '<th><a href="/pt/taxas-euribor-actuais/4/euribor-taxa-12-meses/" title="Euribor 12 meses">Euribor 12 meses</a></th>'
            ref2 = '<a href="/pt/aviso-legal/" class="FooterMenu-link">Aviso Legal</a>'
            start_index = html.find(ref1) + len(ref1)
            end_index = html.find(ref2)

            info = html[start_index:end_index]
            index1 = info.find('<td class="text-right">') + len('<td class="text-right">')
            index2 = info.find(" %")

            rate = info[index1:index2]
            rate = rate.replace(",", ".")
        
        return rate




if __name__ == "__main__":
    url = "https://www.euribor-rates.eu/pt/taxas-euribor-actuais/"
    html = urlopen(url).read().decode()
    ref1 = '<th><a href="/pt/taxas-euribor-actuais/5/euribor-taxa-1-semana/" title="Euribor 1 semana">Euribor 1 semana</a></th>'
    ref2 = '<th><a href="/pt/taxas-euribor-actuais/1/euribor-taxa-1-mes/" title="Euribor 1 m&#234;s">Euribor 1 m&#234;s</a></th>'
    start_index = html.find(ref1) + len(ref1)
    end_index = html.find(ref2)

    info = html[start_index:end_index]
    index1 = info.find('<td class="text-right">') + len('<td class="text-right">')
    index2 = info.find(" %")

    rate = info[index1:index2]
    rate = rate.replace(",", ".")

    print(html)

    