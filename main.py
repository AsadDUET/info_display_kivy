# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:09:15 2020

@author: asado
"""
import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Line
from kivy.graphics import Rectangle
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from PIL import Image as pil_img
from PIL import ImageFont,ImageDraw
import random
# to use buttons:
from kivy.uix.button import Button as bt
from kivy.uix.screenmanager import ScreenManager, Screen
import time
from datetime import date, datetime
from kivy.clock import Clock
import matplotlib.pyplot as plt
import csv
state=False
kivy.require("1.11.1")
slide_delay=10
field=list(range(36))
field_text=list(range(36))
month_t=list(range(31))
month_rh=list(range(31))
field_month_t=list(range(31))
field_month_rh=list(range(31))
loop=0
start_time =datetime.now()
set_time=1

if os.path.isfile("data\\prev_details.csv"):
    with open("data\\prev_details.csv","r") as f:
        reader = csv.reader(f)
        field_text = list(reader)[-2]
else:
    for i in range(len(field_text)):
        field_text[i]=''

if os.path.isfile("data\\prev_month_t.csv"):
    with open("data\\prev_month_t.csv","r") as f:
        reader = csv.reader(f)
        month_t = list(reader)[-2]
else:
    for i in range(len(field_month_t)):
        month_t[i]=''

if os.path.isfile("data\\prev_month_rh.csv"):
    with open("data\\prev_month_rh.csv","r") as f:
        reader = csv.reader(f)
        month_rh = list(reader)[-2]
else:
    for i in range(len(field_month_rh)):
        month_rh[i]=''
class filechooser(FileChooserIconView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
class Button(bt):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #self.background_normal=''
        #self.background_color=[1,1,1,1]

class InputPage(GridLayout):
    # runs on initialization
    def __init__(self, **kwargs):
        global field,field_text,month_t,month_rh,field_month_t,field_month_rh,slide_delay
        super().__init__(**kwargs)

        self.cols=1

#############
        upper = GridLayout(cols=4)
########
        box1 = GridLayout(cols=1)
        form = GridLayout(cols=1) # Create a new grid layout

        box1.add_widget(Label(text='Factory Incident status ',size_hint_y=0.1))
        form.add_widget(Label(text='Insident Free Day:'))  # widget #1, top left
        field[0]= TextInput(text=field_text[0], multiline=False)  # defining self.ip...
        form.add_widget(field[0])

        form.add_widget(Label(text='Last day of Insident:'))  # widget #1, top left
        field[1] = TextInput(text=field_text[1], multiline=False)  # defining self.ip...
        form.add_widget(field[1])

        form.add_widget(Label(size_hint_y=4))

        box1.add_widget(form)
        upper.add_widget(box1)
########
########
        box2 = GridLayout(cols=1)
        form2 = GridLayout(cols=1) # Create a new grid layout

        box2.add_widget(Label(text="Daily Wether",size_hint_y=0.1))
        #form2.add_widget(Label(text="Day's Wether:"))  # widget #1, top left
        #field[2]= TextInput(text=field_text[2], multiline=False)  # defining self.ip...
        #form2.add_widget(field[2])

        form2.add_widget(Label(text='Date:'))  # widget #1, top left
        field_text[2]=str(date.today().strftime('%d-%m-%Y'))
        field[2] = TextInput(text=field_text[2], multiline=False)  # defining self.ip...

        form2.add_widget(field[2])

        form2.add_widget(Label(text='Temperature:'))  # widget #1, top left
        field[3] = TextInput(text=field_text[3], multiline=False)  # defining self.ip...
        form2.add_widget(field[3])

        form2.add_widget(Label(text='Humidity:'))  # widget #1, top left
        field[4] = TextInput(text=field_text[4], multiline=False)  # defining self.ip...
        form2.add_widget(field[4])

        form2.add_widget(Label(text='Day:'))  # widget #1, top left
        field_text[5]=date.today().strftime('%A')
        field[5] = TextInput(text=field_text[5], multiline=False)  # defining self.ip...
        form2.add_widget(field[5])

#        form2.add_widget(Label(size_hint_y=4))

        box2.add_widget(form2)
        upper.add_widget(box2)
########
########
        box3 = GridLayout(cols=1)
        form3 = GridLayout(cols=1) # Create a new grid layout

        box3.add_widget(Label(text='Month Summary',size_hint_y=0.1))

        #form3.add_widget(Label(text="Month Summary:"))  # widget #1, top left
        #field[7]= TextInput(text=field_text[7], multiline=False)  # defining self.ip...
        #form3.add_widget(field[7])

#        form3.add_widget(Label(text='Highest Temperature:'))  # widget #1, top left
        field[6] = TextInput(text=field_text[6], multiline=False)  # defining self.ip...
#        form3.add_widget(field[8])
#
#        form3.add_widget(Label(text='Lowest Temperature:'))  # widget #1, top left
        field[7] = TextInput(text=field_text[7], multiline=False)  # defining self.ip...
#        form3.add_widget(field[9])

        form3.add_widget(Label(text='No of Sunny Days:'))  # widget #1, top left
        field[8] = TextInput(text=field_text[8], multiline=False)  # defining self.ip...
        form3.add_widget(field[8])

        form3.add_widget(Label(text='No of cloudy Days:'))  # widget #1, top left
        field[9] = TextInput(text=field_text[9], multiline=False)  # defining self.ip...
        form3.add_widget(field[9])

        form3.add_widget(Label(text='No. of Rainy Days:'))  # widget #1, top left
        field[10] = TextInput(text=field_text[10], multiline=False)  # defining self.ip...
        form3.add_widget(field[10])

        form3.add_widget(Label(text='No. of Stromy Days:'))  # widget #1, top left
        field[11] = TextInput(text=field_text[11], multiline=False)  # defining self.ip...
        form3.add_widget(field[11])



        box3.add_widget(form3)
        upper.add_widget(box3)
########
########
        box4 = GridLayout(cols=1,size_hint_x=1.5)
        form4 = GridLayout(cols=5) # Create a new grid layout

        box4.add_widget(Label(text='',size_hint_y=0.1))

        form4.add_widget(Label())
        form4.add_widget(Label(text="DOE Std."))
        form4.add_widget(Label(text="Date"))
        form4.add_widget(Label(text="Result"))
        form4.add_widget(Label(text="Unit"))

        form4.add_widget(Label(text="pH:"))
        field[12]= TextInput(text=field_text[12], multiline=False)
        form4.add_widget(field[12])
        field[13]= TextInput(text=field_text[13], multiline=False)
        form4.add_widget(field[13])
        field[14]= TextInput(text=field_text[14], multiline=False)
        form4.add_widget(field[14])
        field[15]= TextInput(text=field_text[15], multiline=False)
        form4.add_widget(field[15])

        form4.add_widget(Label(text="BOD:"))
        field[16]= TextInput(text=field_text[16], multiline=False)
        form4.add_widget(field[16])
        field[17]= TextInput(text=field_text[17], multiline=False)
        form4.add_widget(field[17])
        field[18]= TextInput(text=field_text[18], multiline=False)
        form4.add_widget(field[18])
        field[19]= TextInput(text=field_text[19], multiline=False)
        form4.add_widget(field[19])

        form4.add_widget(Label(text="COD:"))
        field[20]= TextInput(text=field_text[20], multiline=False)
        form4.add_widget(field[20])
        field[21]= TextInput(text=field_text[21], multiline=False)
        form4.add_widget(field[21])
        field[22]= TextInput(text=field_text[22], multiline=False)
        form4.add_widget(field[22])
        field[23]= TextInput(text=field_text[23], multiline=False)
        form4.add_widget(field[23])

        form4.add_widget(Label(text="DO:"))
        field[24]= TextInput(text=field_text[24], multiline=False)
        form4.add_widget(field[24])
        field[25]= TextInput(text=field_text[25], multiline=False)
        form4.add_widget(field[25])
        field[26]= TextInput(text=field_text[26], multiline=False)
        form4.add_widget(field[26])
        field[27]= TextInput(text=field_text[27], multiline=False)
        form4.add_widget(field[27])

        form4.add_widget(Label(text="TSS:"))
        field[28]= TextInput(text=field_text[28], multiline=False)
        form4.add_widget(field[28])
        field[29]= TextInput(text=field_text[29], multiline=False)
        form4.add_widget(field[29])
        field[30]= TextInput(text=field_text[30], multiline=False)
        form4.add_widget(field[30])
        field[31]= TextInput(text=field_text[31], multiline=False)
        form4.add_widget(field[31])

        form4.add_widget(Label(text="TDS:"))
        field[32]= TextInput(text=field_text[32], multiline=False)
        form4.add_widget(field[32])
        field[33]= TextInput(text=field_text[33], multiline=False)
        form4.add_widget(field[33])
        field[34]= TextInput(text=field_text[34], multiline=False)
        form4.add_widget(field[34])
        field[35]= TextInput(text=field_text[35], multiline=False)
        form4.add_widget(field[35])



        box4.add_widget(form4)
        upper.add_widget(box4)
########
        self.add_widget(upper)
#############
        self.add_widget(Label(text="Daily Temp & RH ",size_hint_y=.2))

        form5 = GridLayout(cols=21,size_hint_y=.1)
        for day in range(7):
            form5.add_widget(Label(text='Date'))
            form5.add_widget(Label(text='T'))
            form5.add_widget(Label(text='RH'))
        self.add_widget(form5)

        form6 = GridLayout(cols=21,size_hint_y=0.5)
        for day in range(31):
            form6.add_widget(Label(text=str(day+1)))
            field_month_t[day] = TextInput(text=month_t[day], multiline=False)
            field_month_rh[day] = TextInput(text=month_rh[day], multiline=False)
            form6.add_widget(field_month_t[day])
            form6.add_widget(field_month_rh[day])
        self.add_widget(form6)

        slide=GridLayout(cols=2,size_hint_y=0.1)
        slide.add_widget(Label(text='Slide Show Delay (in Seconds): '))
        self.text_slide=TextInput(text=str(slide_delay),multiline=False)
        slide.add_widget(self.text_slide)
        self.add_widget(slide)
        # add our button.
        self.run = Button(text="Next",size_hint_y=0.2,padding=[10,10],halign='center')
        self.run.text_size=(self.run.width, None)
        self.run.bind(width=self.update_text_width,on_press=self.run_button)
        #self.add_widget(Label())  # just take up the spot.
        self.add_widget(self.run)

    def update_text_width(self, *_):
        self.run.text_size = (self.run.width * 0.9, None)
        
    def run_button(self, instance):
        global field,field_text,month_t,month_rh,field_month_t,field_month_rh,slide_delay
        slide_delay=int(self.text_slide.text)
        with open("data\\prev_details.csv","a") as f:
            for i in range(len(field)):
                field_text[i]=str(field[i].text)
            writer = csv.writer(f, delimiter=",")
            writer.writerow(field_text)

        with open("data\\prev_month_t.csv","a") as f:
            for i in range(len(month_t)):
                month_t[i]=str(field_month_t[i].text)
            writer = csv.writer(f, delimiter=",")
            writer.writerow(month_t)

        with open("data\\prev_month_rh.csv","a") as f:
            for i in range(len(month_rh)):
                month_rh[i]=str(field_month_rh[i].text)
            writer = csv.writer(f, delimiter=",")
            writer.writerow(month_rh)
        #chat_app.info_page.update_info(info)
        chat_app.info_page.make_page(self)
        chat_app.screen_manager.current = 'Input2'
        Clock.schedule_interval(chat_app.my_time,slide_delay)

#from kivy.uix.checkbox import CheckBox
class InputPage2(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        i=0
        if os.path.isfile("data\\Attendence_info.csv"):
            with open("data\\Attendence_info.csv","r") as f:
                reader = csv.reader(f)
                field_text2 = list(reader)[-2]
                for k, v in self.ids.items():
                    self.ids[str(k)].text=field_text2[i]
                    i+=1
        self.chk_state=False
    def checkbox_click(self, instance, value):
        self.chk_state=value
    def save_to_file(self):
        global state
        for_save=[]
        with open("data\\Attendence_info.csv","a") as f:
            for k, v in self.ids.items():
                for_save.append(str(self.ids[str(k)].text))
            writer = csv.writer(f, delimiter=",")
            writer.writerow(for_save)
        chat_app.info_page2.update_data(self)
        if self.chk_state:
            chat_app.screen_manager.current = 'In_visitor'
        else:
            chat_app.screen_manager.current = 'Info'
            state=True


class InputVisitor(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #global visitor_table
        self.visitor_table = GridLayout(cols=4)
        self.add_widget(self.visitor_table)
        self.next=Button(text='Next',size_hint_y=0.2)
        self.next.bind(on_press=self.next_p)
        self.add_widget(self.next)
        self.num_visitor=0
        self.visitor_list=[]
        self.v_name=[]
        self.btn_photo=[]
        self.v_desig=[]
        self.v_addr=[]
        self.v_image=[]
        self.dynamic_id={}

    def next_p(self, instance):
        global state, set_time
        set_time=int(self.ids['show_visitor'].text)
        data=[]
        data.append(len(self.visitor_list))
        for i in self.visitor_list:
            data.append(self.v_name[i].text)
            data.append(self.v_desig[i].text)
            data.append(self.v_addr[i].text)
            data.append(self.v_image[i])
        with open("data\\visitor_info.csv","a") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(data)
                
        if os.path.isfile("data\\visitor_info.csv"):
            with open("data\\visitor_info.csv","r") as f:
                reader = csv.reader(f)
                data = list(reader)[-2]
                templets=os.listdir('cover')
                for p_no in range(int(data[0])):
                    img_t=pil_img.open('cover\\'+templets[random.randint(0,len(templets)-1)])
                    draw = ImageDraw.Draw(img_t)
                    font = ImageFont.truetype("Renfrew.ttf", 50)
                    draw.text((80, 100),data[4*p_no+1],(0,0,0),font=font)
                    draw.text((80, 200),data[4*p_no+2],(0,0,0),font=font)
                    draw.text((80, 300),data[4*p_no+3],(0,0,0),font=font)
                    img = pil_img.open(data[4*p_no+4])
                    ratio=min((1000/img.height),(1000/img.width))
                    img=img.resize((int(img.width*ratio),int(img.height*ratio)))
                    img_t.paste(img,(1450-int(img.width/2),int(1080/2)-int(img.height/2)))
                    img_t.save('temp\\'+str(p_no)+'.png')
                    
                    data[4*p_no+4]='temp\\'+str(p_no)+'.png'
                    chat_app.visitor_page = VisitorPage(data[4*p_no+1],data[4*p_no+2],data[4*p_no+3],data[4*p_no+4])
                    screen = Screen(name='vistor'+str(p_no))
                    screen.add_widget(chat_app.visitor_page)
                    chat_app.screen_manager.add_widget(screen)
                    chat_app.screens.append(screen.name)
        else:
            pass
                

        
        chat_app.info_page2.update_data(self)
        chat_app.screen_manager.current = 'Info'
        state=True
                
    def add_list(self):
        #global v_image,num_visitor, visitor_table, v_name,btn_photo,v_desig,v_addr
        
        self.visitor_list.append(self.num_visitor)
        self.v_name.append(TextInput())
        self.visitor_table.add_widget(self.v_name[self.num_visitor])
        
        self.v_desig.append(TextInput())
        self.visitor_table.add_widget(self.v_desig[self.num_visitor])
        
        self.v_addr.append(TextInput())
        self.visitor_table.add_widget(self.v_addr[self.num_visitor])
        
        self.btn_photo.append(Button(text="Choose Photo",size_hint_y=0.2))
        self.btn_photo[self.num_visitor].bind(on_press=self.pop)
        self.v_image.append('')
        #self.add_widget(Label())  # just take up the spot.
        self.visitor_table.add_widget(self.btn_photo[self.num_visitor])
        self.dynamic_id[str(self.btn_photo[self.num_visitor])]=self.num_visitor
        self.num_visitor=self.num_visitor+1


    def pop(self, instance):
        #global num_visitor
        content = BoxLayout(orientation='vertical', spacing=5)
        self.popup = popup = Popup(title='pick',
            content=content, size_hint=(None, None), size=(600, 400))

        # first, create the scrollView
        self.scrollView = scrollView = ScrollView()

        # then, create the fileChooser and integrate it in thescrollView
        self.fileChooser = fileChooser =FileChooserListView(size_hint_y=None,path=os.getcwd())
        fileChooser.height = 500 # this is a bit ugly...
        scrollView.add_widget(fileChooser)

        # construct the content, widget are used as a spacer
        content.add_widget(Widget(size_hint_y=None, height=5))
        content.add_widget(scrollView)
        content.add_widget(Widget(size_hint_y=None, height=5))

        # 2 buttons are created for accept or cancel the current value
        btnlayout = BoxLayout(size_hint_y=None, height=50, spacing=5)
        btn = Button(text='Ok')
        self.dynamic_id[str(btn)]=self.dynamic_id[str(instance)]
        btn.bind(on_release=self._validate)
        btnlayout.add_widget(btn)
        btn = Button(text='Cancel')
        btn.bind(on_release=popup.dismiss)
        btnlayout.add_widget(btn)
        content.add_widget(btnlayout)

        # all done, open the popup !
        popup.open()
    def _validate(self, instance):
        self.popup.dismiss()
        self.popup = None
        value = self.fileChooser.selection
        try:
            self.btn_photo[self.dynamic_id[str(instance)]].background_normal=str(value[0])
        # if the value was empty, don't change anything.
            if value == []:
                return
    
            # do what you would do if the user selected a file.
            else:
                self.v_image[int(self.dynamic_id[str(instance)])]=str(value[0])
        except:
            pass

class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def make_page(self, instance):
        global field_text,month_t,month_rh
        if os.path.isfile("data\\prev_details.csv"):
            with open("data\\prev_details.csv","r") as f:
                reader = csv.reader(f)
                data=list(reader)[-2]
                i=0
                for k,v in self.ids.items():
                    self.ids[str(k)].text=str(data[i])
                    i=i+1
                    if i==len(data):
                        break
        plt.figure(figsize=(8,3))
        month_tt=[]
        month_rhh=[]
        for i in range(len(month_t)):
            try:
                month_tt.append(float(month_t[i]))
            except:

                break
        for i in range(len(month_rh)):
            try:
                month_rhh.append(float(month_rh[i]))
            except:
                break
        try:
            self.ids['id_6'].text=str(max(month_tt))
        except:
            pass
        try:
            self.ids['id_7'].text=str(min(month_tt))
        except:
            pass
        plt.style.use('dark_background')
        plt.title("Daily Temp & RH")

        plt.plot(month_tt)
        plt.plot(month_rhh)
        plt.axis([0, 30, 0, 100])
        plt.legend(['Temp','RH'])
        #plt.grid()
        plt.savefig('plot.png')
        self.ids['plot'].source='plot.png'

#    def my_time(self,*args):
#        self.message.text = str(datetime.now())
#
#    # Called with a message, to update message text in widget
#    def update_info(self, message):
#        self.message.text = message
#
#    # Called on label width update, so we can set text width properly - to 90% of label width
#    def update_text_width(self, *_):
#        self.message.text_size = (self.message.width * 0.9, None)


class InfoPage2(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def update_data(self, instance):
        if os.path.isfile("data\\Attendence_info.csv"):
            with open("data\\Attendence_info.csv","r") as f:
                reader = csv.reader(f)
                data=list(reader)[-2]
                i=0
                for k,v in self.ids.items():
                    self.ids[str(k)].text=str(data[i])
                    i=i+1
        self.ids['att_13'].text=str(self.conv(self.ids['att_1'].text)+self.conv(self.ids['att_5'].text)+self.conv(self.ids['att_9'].text))
        self.ids['att_14'].text=str(self.conv(self.ids['att_2'].text)+self.conv(self.ids['att_6'].text)+self.conv(self.ids['att_10'].text))
        self.ids['att_15'].text=str(self.conv(self.ids['att_3'].text)+self.conv(self.ids['att_7'].text)+self.conv(self.ids['att_11'].text))
        self.ids['att_16'].text=str(self.conv(self.ids['att_4'].text)+self.conv(self.ids['att_8'].text)+self.conv(self.ids['att_12'].text))

    def conv(self,val):
        try:
            return int(val)
        except:
            return 0



class VisitorPage(GridLayout):
    def __init__(self,a,b,c,d):
        super().__init__()
        self.cols=2
#        self.table=GridLayout(cols=1,size_hint_x=0.3)
#        
#        
#        self.table.add_widget(Label(text='Name: '+str(a)))
#        self.table.add_widget(Label(text='Designition: '+str(b)))
#        self.table.add_widget(Label(text='Address: '+str(c)))
#        self.table.add_widget(Label(text='',size_hint_y=5))
#        self.add_widget(self.table)
        
        self.add_widget(Image(source=d,allow_stretch=True))
        

    # Called with a message, to update message text in widget
    def update_info(self, message):
        self.message.text = message

    # Called on label width update, so we can set text width properly - to 90% of label width
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)


class DashboardApp(App):
    def build(self):
        # We are going to use screen manager, so we can add multiple screens
        # and switch between them

        self.screen_manager = ScreenManager()
        self.screens=['Info','Info2']
        

        
        self.input_page = InputPage()
        screen = Screen(name='Input')
        screen.add_widget(self.input_page)
        self.screen_manager.add_widget(screen)

        self.input_page2 = InputPage2()
        screen = Screen(name='Input2')
        screen.add_widget(self.input_page2)
        self.screen_manager.add_widget(screen)
        
        self.visitor_input_page = InputVisitor()
        screen = Screen(name='In_visitor')
        screen.add_widget(self.visitor_input_page)
        self.screen_manager.add_widget(screen)


        # Info page
        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        self.info_page2 = InfoPage2()
        screen = Screen(name='Info2')
        screen.add_widget(self.info_page2)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def my_time(self,*args):
        global state, loop,set_time
        
        if state:
            time_diff=datetime.now()-start_time
            if time_diff.seconds/3600 > set_time:
                self.screens=['Info','Info2']
            if loop<len(chat_app.screens):
                chat_app.screen_manager.current=chat_app.screens[loop]
                loop=loop+1
            else:
                loop=0
                    
 
    
if __name__ == "__main__":
    chat_app = DashboardApp()
    chat_app.run()
