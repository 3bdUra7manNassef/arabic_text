
#!dont touch module!#
from tkinter import *
import arabic_reshaper
import bidi.algorithm

#?window : نافذة?#
app = Tk()
app.geometry('600x600+350+60')
app.resizable(False,False)
app.config(bg='#F4DFC8')
app.title('arabic keyboard')

#?text for input or output txt?#
text_lb_input = arabic_reshaper.reshape('ادخل النص')
text_lb_input_bidi = bidi.algorithm.get_display(text_lb_input)

text_btn_output = arabic_reshaper.reshape('تحويل النص')
text_btn_output_bidi = bidi.algorithm.get_display(text_btn_output)

text_lb_output = arabic_reshaper.reshape('النتيجة')
text_lb_output_bidi = bidi.algorithm.get_display(text_lb_output)

text_btn_copy = arabic_reshaper.reshape('نسخ')
text_btn_copy_bidi = bidi.algorithm.get_display(text_btn_copy)

#?command for btn?#

def copy_to_memory():
    output = txt_input.get('1.0','end')
    reversed_output = arabic_reshaper.reshape(output)[::-1]  # Reverse the output text
    app.clipboard_append(reversed_output)


def revers():
    txt_output.delete("1.0", "end")
    output = txt_input.get('1.0','end')
    txt_output.insert('1.0',arabic_reshaper.reshape(output))

#?label?#
lb_input = Label(app,text=text_lb_input_bidi,fg='#000f30',bg ='#F4EAE0',font=('100'),width=14,pady=10)
lb_input.place(y=10,x=225)

lb_output = Label(app,text=text_lb_output_bidi,fg='#000f30',bg ='#F4EAE0',font=('100'),width=14,pady=10)
lb_output.place(y=320,x=240)

#?text?#
txt_input = Text(app,fg='#000f30',bg ='#F4EAE0',font=('100'),height=10,width=40,)
txt_input.place(y=50,x=120)

txt_output = Text(app,fg='#000f30',bg ='#F4EAE0',font=('100'),height=10,width=40)
txt_output.place(y=360,x=120)

#?btn?#
btn_output = Button(app,text=text_btn_output_bidi,command=revers,bg='#000000',fg='white',activebackground='#000f30')
btn_output.place(x=275,y=270)

btn_add_to_memory = Button(app,text = text_btn_copy_bidi,activebackground='#1c1c11',bg='#c0c0c0',command=copy_to_memory)
btn_add_to_memory.place(x=500,y=500)


mainloop()