import tkinter as tk
from tkinter import ttk

class RPGInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('RPG Pistachio Clicker')
        self.create_widgets()
        
        self.vida_text = tk.StringVar()
        self.daño_text = tk.StringVar()
        self.name_text = tk.StringVar()
        self.defensa_text = tk.StringVar()
        self.mana_text = tk.StringVar()
        self.velocidad_text = tk.StringVar()
        self.exp_text = tk.StringVar()
        self.p_atributo_text = tk.StringVar()
        self.p_habilidad_text = tk.StringVar()
        self.hambre_text = tk.StringVar()
        self.sed_text = tk.StringVar()

        self.update_stat_values()  # actualizar los valores iniciales de las variables
        
        # Create labels and progress bars for each statistic
        # Name and base damage
        name_label = tk.Label(self.window, text="Name:")
        name_label.grid(row=0, column=0, sticky="E")
        self.name_text.set(f"{data['name']}")
        name_value_label = tk.Label(self.window, textvariable=self.name_text)
        name_value_label.grid(row=0, column=1, sticky="W")
        
        daño_label = tk.Label(self.window, text="Daño:")
        daño_label.grid(row=1, column=0, sticky="E")
        self.daño_text.set(f"{data['daño_base']}")
        daño_value_label = tk.Label(self.window, textvariable=self.daño_text)
        daño_value_label.grid(row=1, column=1, sticky="W")

        # Health
        vida_label = tk.Label(self.window, text="Vida:")
        vida_label.grid(row=1, column=3, sticky="E")

        self.vida_text.set(f"{data['vida']}/{data['vida_max']}")
        vida_value_label = tk.Label(self.window, textvariable=self.vida_text)
        vida_value_label.grid(row=0, column=4)

        self.vida_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.vida_progress.grid(row=1, column=4)
        self.vida_progress['maximum'] = data['vida_max']
        self.vida_progress['value'] = data['vida']

        # Defense
        defensa_label = tk.Label(self.window, text="Defensa:")
        defensa_label.grid(row=4, column=0)
        self.defensa_text.set(f"{data['defensa']}/{data['defensa_max']}")
        defensa_value_label = tk.Label(self.window, textvariable=self.defensa_text)
        defensa_value_label.grid(row=4, column=1)

        # Mana
        mana_label = tk.Label(self.window, text="Mana:")
        mana_label.grid(row=5, column=0, sticky="E")
        self.mana_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.mana_progress.grid(row=5, column=1)
        self.mana_progress['maximum'] = data['mana_max']
        self.mana_progress['value'] = data['mana']

        # Speed
        velocidad_label = tk.Label(self.window, text="Velocidad:")
        velocidad_label.grid(row=5, column=0)
        self.velocidad_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL,
                                                length=100, mode='determinate')
        self.velocidad_progress.grid(row=5, column=1)
        self.velocidad_progress['maximum'] = data['velocidad_max']
        self.velocidad_progress['value'] = data['velocidad']

        # Experience
        exp_label = tk.Label(self.window, text="Experience:")
        exp_label.grid(row=6, column=0)
        self.exp_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL,
                                            length=100, mode='determinate')
        self.exp_progress.grid(row=6, column=1)
        self.exp_progress['maximum'] = data['exp_max']
        self.exp_progress['value'] = data['exp']

        # Attribute points
        p_atributo_label = tk.Label(self.window, text="Attribute Points:")
        p_atributo_label.grid(row=7, column=0)
        self.p_atributo_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL,
                                        length=100, mode='determinate')
        self.p_atributo_progress.grid(row=7, column=1)
        self.p_atributo_progress['maximum'] = data['p_atributo_max']
        self.p_atributo_progress['value'] = data['p_atributo']

        # Skill points
        p_habilidad_label = tk.Label(self.window, text="Skill Points:")
        p_habilidad_label.grid(row=8, column=0)
        self.p_habilidad_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL,
                                                    length=100, mode='determinate')
        self.p_habilidad_progress.grid(row=8, column=1)
        self.p_habilidad_progress['maximum'] = data['p_habilidad_max']
        self.p_habilidad_progress['value'] = data['p_habilidad']

        # Hunger
        hambre_label = tk.Label(self.window, text="Hunger:")
        hambre_label.grid(row=9, column=0)
        self.hambre_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL,
                                            length=100, mode='determinate')
        self.hambre_progress.grid(row=9, column=1)
        self.hambre_progress['maximum'] = data['hambre_max']
        self.hambre_progress['value'] = data['hambre']

        # Thirst
        sed_label = tk.Label(self.window, text="Thirst:")
        sed_label.grid(row=10, column=0)
        self.sed_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL,
                                            length=100, mode='determinate')
        self.sed_progress.grid(row=10, column=1)
        self.sed_progress['maximum'] = data['sed_max']
        self.sed_progress['value'] = data['sed']

        # Happiness
        felicidad_label = tk.Label(self.window, text="Happiness:")
        felicidad_label.grid(row=11, column=0)
        self.felicidad_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL,
                                                length=100, mode='determinate')
        self.felicidad_progress.grid(row=11, column=1)
        self.felicidad_progress['maximum'] = data['felicidad_max']
        self.felicidad_progress['value'] = data['felicidad']

        # Sleep
        sueño_label = tk.Label(self.window, text="Sleep:")
        sueño_label.grid(row=12, column=0)
        self.sueño_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL,
                                            length=100, mode='determinate')
        self.sueño_progress.grid(row=12, column=1)
        self.sueño_progress['maximum'] = data['sueño_max']
        self.sueño_progress['value'] = data['sueño']

        # Stamina
        estamina_label = tk.Label(self.window, text="Stamina:")
        estamina_label.grid(row=13, column=0)
        self.estamina_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL,
                                                length=100, mode='determinate')
        self.estamina_progress.grid(row=13, column=1)
        self.estamina_progress['maximum'] = data['estamina_max']
        self.estamina_progress['value'] = data['estamina']

        # Energy
        energia_label = tk.Label(self.window, text="Energy:")
        energia_label.grid(row=0, column=10)
        self.energia_progress = ttk.Progressbar(self.window, orient=tk.HORIZONTAL,
                                                length=100, mode='determinate')
        self.energia_progress.grid(row=0, column=11)
        self.energia_progress['maximum'] = data['energia_max']
        self.energia_progress['value'] = data['energia']

        # Set up update loop to refresh values every second
        self.window.after(1000, self.update_data)
        pass

    def create_widgets(self):
        # Create all the widgets and set up the layout
        pass
    
    def update_stat_values(self):
        self.vida_text.set(f"{data['vida']}/{data['vida_max']}")
        self.daño_text.set(f"{data['daño_base']}")
        self.defensa_text.set(f"{data['defensa']}/{data['defensa_max']}")
        self.mana_text.set(f"{data['mana']}/{data['mana_max']}")
        self.velocidad_text.set(f"{data['velocidad']}/{data['velocidad_max']}")
        self.exp_text.set(f"{data['exp']}/{data['exp_max']}")
        self.p_atributo_text.set(f"{data['p_atributo']}/{data['p_atributo_max']}")
        self.p_habilidad_text.set(f"{data['p_habilidad']}/{data['p_habilidad_max']}")
        self.hambre_text.set(f"{data['hambre']}/{data['hambre_max']}")
        self.sed_text.set(f"{data['sed']}/{data['sed_max']}")

    def update_data(self, data):
        # Update all the progress bars with new values from the data dictionary
        self.vida_progress['value'] = self.data['vida']
        self.mana_progress['value'] = self.data['mana']
        self.velocidad_progress['value'] = self.data['velocidad']
        self.nivel_label.config(text=f"Level: {self.data['nivel']}")
        self.exp_progress['value'] = self.data['exp']
        self.p_atributo_progress['value'] = self.data['p_atributo']
        self.p_habilidad_progress['value'] = self.data['p_habilidad']
        self.hambre_progress['value'] = self.data['hambre']
        self.sed_progress['value'] = self.data['sed']
        self.felicidad_progress['value'] = self.data['felicidad']
        self.sueño_progress['value'] = self.data['sueño']
        self.estamina_progress['value'] = self.data['estamina']
        self.energia_progress['value'] = self.data['energia']

        # Schedule the update function to run again in 1 second
        self.window.after(1000, self.update_data)
        pass

    def run(self):
        self.window.mainloop()
        
    def set_data(self, data):
        self.vida_progress['maximum'] = data['vida_max']
        self.vida_progress['value'] = data['vida']
        self.mana_progress['maximum'] = data['mana_max']
        self.mana_progress['value'] = data['mana']
        self.velocidad_progress['maximum'] = data['velocidad_max']
        self.velocidad_progress['value'] = data['velocidad']
        self.exp_progress['maximum'] = data['exp_max']
        self.exp_progress['value'] = data['exp']
        self.p_atributo_progress['maximum'] = data['p_atributo_max']
        self.p_atributo_progress['value'] = data['p_atributo']
        self.p_habilidad_progress['maximum'] = data['p_habilidad_max']
        self.p_habilidad_progress['value'] = data['p_habilidad']
        self.hambre_progress['maximum'] = data['hambre_max']
        self.hambre_progress['value'] = data['hambre']
        self.sed_progress['maximum'] = data['sed_max']
        self.sed_progress['value'] = data['sed']

if __name__ == '__main__':
    # Create a dictionary with test data
    data = {
        'name': 'Warrior',
        'daño_base': 50,
        'vida': 80,
        'vida_max': 100,
        'defensa': 70,
        'defensa_max': 100,
        'mana': 30,
        'mana_max': 50,
        'velocidad': 20,
        'velocidad_max': 30,
        'nivel': 5,
        'exp': 120,
        'exp_max': 200,
        'p_atributo': 5,
        'p_atributo_max': 10,
        'p_habilidad': 10,
        'p_habilidad_max': 20,
        'hambre': 80,
        'hambre_max': 100,
        'sed': 70,
        'sed_max': 100,
        'felicidad': 90,
        'felicidad_max': 100,
        'sueño': 20,
        'sueño_max': 100,
        'estamina': 50,
        'estamina_max': 100,
        'energia': 20,
        'energia_max': 30,
    }

    # Create an instance of the RPGInterface class
    gui = RPGInterface()

    # Set the data for the interface
    gui.set_data(data)

    # Run the GUI
    gui.run()
