from tkinter import *
from tkinter import ttk
from tkinter import font
import db

class Nummerplaatzoeker:
    
    def __init__(self, root):
        
        root.title("Nummerplaatzoeker")
        root.resizable(FALSE,FALSE)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        point_x = (screen_width // 2) - 200
        point_y = (screen_height // 2) - 100
        root.geometry(f"+{point_x}+{point_y}")
        root.attributes("-topmost", 1)
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
    
        
        logo_police = PhotoImage(file='logo_police_small.gif')
        logo_label = ttk.Label(mainframe, image=logo_police)
        logo_label.image = logo_police
        logo_label.grid(row=0, column=0)

        self.nummerplaat = StringVar()
        nummerplaat_entry = ttk.Entry(mainframe, width=9, 
                                      textvariable=self.nummerplaat)
        nummerplaat_entry.grid(column=1, row=2, sticky=(W, E))

        # title label
        title_style = ttk.Style()
        title_style.configure("Title.TLabel", foreground="blue", 
                        font=("Helvetica", 18, "bold"))
        title = "Nummerplaatzoeker"
        title_label = ttk.Label(mainframe, text=title, style="Title.TLabel")
        title_label.grid(row=0, column=1)

        # label with question for plate
        nummerplaat_question = "Geef hier een nummerplaat in: "
        ttk.Label(mainframe, text=nummerplaat_question).grid(column=1, row=1,
                                                     sticky=(W))

        # knop om de zoekactie te starten
        ttk.Button(mainframe, text="Zoek", command=self.zoek).grid(column=2, 
                                    row=2, sticky=W)

        # Result
        self.info = StringVar()
        info_text = ttk.Label(mainframe, textvariable=self.info).grid(
                row=3, column=1, columnspan=2, sticky=(W, E, N))
        
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        nummerplaat_entry.focus()
        root.bind("<Return>", self.zoek)

    def zoek(self, *args):
        zoekwaarde = str(self.nummerplaat.get())
        self.info.set(db.get_info_for_nummerplaat(zoekwaarde))



def main():
    root = Tk()
    Nummerplaatzoeker(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()

