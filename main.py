import customtkinter
from functions import *

def main():
    global app, textbox

    def highlight():
        # call searchv2 and store the returned values in variables
        first, second = searchv2()

        # update the textbox with the returned values
        textbox.configure(state="normal")  # enable editing
        textbox.delete("1.0", tk.END)  # clear previous contents
        textbox.insert(tk.END, f"{first}\n")
        textbox.insert(tk.END, f"{second}\n")
        textbox.configure(state="disabled")  # disable editing

    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    #create a GUI window
    app = customtkinter.CTk()
    app.geometry("750x250")
    app.title("George's Gamer")
    app.attributes('-topmost', True)

    button_frame = customtkinter.CTkFrame(app)
    button_frame.pack(side="top", fill="x")

    # Cature Test Button
    capture_button = customtkinter.CTkButton(master=button_frame, text="Open Selected", command=open_screen)
    capture_button.pack(side=customtkinter.LEFT)

    # Quick Screen Select Button
    quick_screen_select_button = customtkinter.CTkButton(master=button_frame, text="Quick Screen Select", command=quick_select)
    quick_screen_select_button.pack(side=customtkinter.LEFT)

    #Search Valorant
    search_screen_button = customtkinter.CTkButton(master=button_frame, text="Search Valorant", command=search_val)
    search_screen_button.pack(side=customtkinter.LEFT)

    #Search Lore
    search_lore_button = customtkinter.CTkButton(master=button_frame, text="Search Lore", command=search_vallore)
    search_lore_button.pack(side=customtkinter.LEFT)

    # Search v2
    searchv2_button = customtkinter.CTkButton(master=button_frame, text="Highlight Search", command=highlight)
    searchv2_button.pack(side=customtkinter.LEFT)

    # create the textbox
    textbox = customtkinter.CTkTextbox(master=app, width=1200)
    textbox.pack(side=customtkinter.TOP)

    app.mainloop()

if __name__ == '__main__':
    main()
    app.quit()

#brimstone va

#sova va

#who was the sixth Agent to join the VALORANT

#how many credits are needed to buy marshal?