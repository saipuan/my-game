import tkinter as tk
import random
import math

#--Constant--
TILE_COUNT = 204
TIMER_DURATION = 15 * 60
COLORS = [f"#{random.randint(0, 0xFFFFFF) :06x}" for _ in range(TILE_COUNT // 2)] * 2
random.shuffle(COLORS)

#--Game State--
selected = []
matched = set()
time_left = TIMER_DURATION
player_name = ""


#--MainWindow--
MainWindow = tk.Tk()
MainWindow.withdraw()

#--Center Window--
def center_window(win, width, height):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
#--Grid Size--
def get_grid_dimension(tile_count):
    row = 12
    cols = math.ceil(tile_count / rows)
    return rows, cols

#--Name Entry/Input--
def launch_name_window():
    name_win = tk.Toplevel()
    name_win.title("My Game - Welcome!")
    center_window(name_win, 420, 240)
    name_win.configure(bg = "#121212")
    name_win.resizable(False, False)
    
    tk.Label(name_win, text = "Remember Me", font = ("Segoe UI Black", 18), fg = "#00bfff", bg = "#121212").pack(pady = (20, 5))
    tk.Label(name_win, text = "Enter Your Name to Begin", font = ("Segoe UI Black", 12), fg = "#DDDDDD", bg = "#121212").pack(pady = (5, 10))
    
    name_entry = tk.Entry(name_win,font = ("Segeo UI", 14), justify = "center", fg = "#222", relief = "flat")
    name_entry.pack(pady = 5, ipadx = 10, ipady = 5)
    
    def start_game():
        global player_name
        player_name = name.entry.get().strip() or "Player"
        name_win.destroy()
        launch_game_window()
        
    start_btn = tk.Button(
        name_win, text = "Start Game", font = ("Segoe UI Semibold", 13),
        bg = "#00bfff", fg = "white", activebackground = "#008cba",
        activeforeground = "white", relief = "flat", padx = 15, pady = 6,
        cursor = "hand2", command = start_game
        
        )
    
    start_btn.pack(pady = 15)
    
    #hover effect
    def on_enter(e): start_btn.config(bg="#1E90FF")
    def on_leave(e): start_btn.config(bg="#00BFF")
    start_btn.bind("Enter", on_enter)
    start_btn.bind("Enter", on_leave)
    
#--Main Game Window--
def launch_game_window():
    game_win = tk.Toplevel()
    game_win.title("Remember Me")
    center_window(game_win, 1200, 740)
    game_win.configure(bg = "#1E1E1E")
    
    #--Header--
    header = tk.Frame(game_win, bg = "#2A2A2A")
    header.pack(fill = "x", pady = (0, 25))
    header.pack_propagate(False)
    
    #--Timer--
    timer_label = tk.Label(header, text = "15:00", font = ("Segoe UI Semibold", 14), fg = "#00BFF", bg = "#2A2A2A")
    timer.label.pack(side = "left", padx = 20)
    
    #--Score--
    score_label = tk.Label(header, text = f"{player_name}'s Score: 0", font = ("Segoe UI Semibold", 14), fg = "#00BFF", bg = "#2A2A2A")
    score.label.pack(side = "right", padx = 20)
    
    #--Title--
    title_label = tk.Label(header, text = "Memory Match", font = ("Segoe UI Semibold", 18), fg = "#FFFFFF", bg = "#2A2A2A")
    title.label.pack(relx = 0.5, rely = 0.5, anchor = "center")
    
    #--Grid--
    grid_container = tk.Frame(game_win, bg = "#1E1E1E")
    grid_container.pack(expand = True, fill = "both", pady =(10, 10))
    
    tiles_frame = tk.Frame(gride_container, bg = "#1E1E1E")
    tiles_frame.pack(pady =(10, 10))
    
    rows, cols = get_gride_dimensions(TILE_COUNT)
    tiles = []
    
#--Launch/show window--
launch_name_window()
MainWindow.mainloop()


        

MainWindow.mainloop()