from tradingview_ta import TA_Handler, Interval, Exchange
import customtkinter
import tkinter

app = customtkinter.CTk()
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
app.title("Turtle Code")
app.geometry("960x960")

bottomframe = tkinter.Frame(app)
bottomframe.pack(expand = True)

def button_event():
    text = search.get()


    output = TA_Handler(
        symbol=text,
        screener="Crypto",
        exchange="Coinbase",
        interval=Interval.INTERVAL_5_MINUTES
        )

    label.set_text(str(output.get_analysis().summary['RECOMMENDATION']))

    print('Symbol : ' + text)


search = customtkinter.CTkEntry(master=bottomframe,
                                placeholder_text='Enter a text',
                                text_font=('Helvetica',28),
                                width=800,
                                height=100,
                                border_width=2,
                                corner_radius=10)
search.pack()

button = customtkinter.CTkButton(master=bottomframe,
                                 width=500,
                                 height=100,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Search",
                                 text_font=('Helvetica',28),
                                 fg_color="yellow",
                                 command=button_event)
button.pack()

label = customtkinter.CTkLabel(master=bottomframe,
                               text="",
                               text_color="black",
                               width=400,
                               height=100,
                               text_font=('Helvetica',14),
                               fg_color=("white"),
                               corner_radius=8)
label.pack()

app.mainloop()