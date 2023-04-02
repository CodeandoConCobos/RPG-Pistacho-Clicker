class Clase:
    def __init__(self, vida, vida_max, defensa, defensa_max, p_atributo, p_atributo_max, nivel, exp, exp_max, velocidad, velocidad_max, hambre, hambre_max, sed, sed_max, felicidad, felicidad_max, sueño, sueño_max, estamina, estamina_max, energia, energia_max):
        # STATS
        self.vida = vida # 
        self.vida_max = vida_max
        self.defensa = defensa # 
        self.defensa_max = defensa_max
        self.velocidad = velocidad # Esta caracteristica determina quien nataca primero en un juego de turnos
        self.velocidad_max = velocidad_max # Necesitamos un maximo ya que durante el combate la velocidad puede subir 
        self.nivel = nivel # Aumenta las estadsiticas base en función de tu clase hijo como Mono() y te da puntos de atributos para poder elegir cual subir
        self.exp = exp # Experiencia normalmente 0
        self.exp_max = exp_max # cuando igualaas o superas la exp_max subes de nivel y exp pasa a 0 y exp_max aumenta un porcentaje variable en funcion de tus atributos
        self.p_atributo = p_atributo # Consumibles para mejorar solo los atributos
        self.p_atributo_max = p_atributo_max # Numero máximo de atributos para poder utilizar
        self.hambre = hambre # Afecta directamente a la felicidad y al sueño si llega a 0 durante 3 dias mueres
        self.hambre_max = hambre_max
        self.sed = sed # Afecta directamente a la felicidad y al sueño si llega a 0 durante 7 dias mueres
        self.sed_max = sed_max
        self.felicidad = felicidad # Afecta al personaje, en caso de tener depresion se puede suicidar y tienes que crearte nuevo personaje
        self.felicidad_max = felicidad_max
        self.sueño = sueño # Afecta a tus estadisticas y limita al personaje a descansar() porque sino reduce a la mitad todas las estadisticas
        self.sueño_max = sueño_max
        self.estamina = estamina # La estamina se consume para hacer acciones como abrir pistachos
        self.estamina_max = estamina_max
        self.energia = energia # La energía se consume en combate
        self.energia_max = energia_max

        # ATRIBUTOS (afectan a las características principales)
        self.vitalidad = vitalidad # Aumenta los puntos maximos de vida
        self.robustez = robustez # Aumenta los puntos de defensa base y maxima
        self.agilidad = agilidad # Aumenta los puntos de velocidad base y maxima
        self.apetito = apetito # Aumenta los puntos de hambre/sed base y maxima
        
        # HABILIDADES
        self.superviviente = superviviente # Reduce el consumo de hambre y sed
        self.eficiente = eficiente # Crea una probabilidad de obtener 1.5 u 2 de puntos para atributos
        self.autodidacta = autodidacta # Reduce la exp_max necesaria para poder subir de nivel mas rapido

class Mono(Clase):
    def __init__(self, vida, vida_max, defensa, defensa_max, daño_base):
        daño_base = 3
        self.vida = 100
        self.vida_max = 100
        self.defensa = 5
        self.defensa_max = 50
        super().__init__(vida, vida_max, defensa, defensa_max, daño_base)
        self.daño_base = daño_base
        self.vida = vida
        self.vida_max = vida_max
        self.defensa = defensa
        self.defensa_max = defensa_max