class Clase:
    def __init__(self, vitalidad, meditacion, robustez, mana, mana_max, sabio, vida, medico, agilidad, apetito, deportista, mentalidad_fuerte, superviviente, insomnio, crecimento_emocional, autodidacta, eficiente, vida_max, defensa, defensa_max, p_habilidad, p_atributo, p_habilidad_max, p_atributo_max, nivel, exp, exp_max, velocidad, velocidad_max, hambre, hambre_max, sed, sed_max, felicidad, felicidad_max, sueño, sueño_max, estamina, estamina_max, energia, energia_max):
        # STATS
        self.vida = vida # Vida actual del jugador
        self.vida_max = vida_max # Vida maxima del jugador
        self.defensa = defensa # 
        self.defensa_max = defensa_max # 
        self.mana = mana # 
        self.mana_max = mana_max # 
        self.velocidad = velocidad # Esta caracteristica determina quien ataca primero en un juego de turnos
        self.velocidad_max = velocidad_max # Necesitamos un maximo ya que durante el combate la velocidad puede subir 
        self.nivel = nivel # Aumenta las estadsiticas base en función de tu clase hijo como Mono() y te da puntos de atributos para poder elegir cual subir
        self.exp = exp # Experiencia normalmente 0
        self.exp_max = exp_max # cuando igualaas o superas la exp_max subes de nivel y exp pasa a 0 y exp_max aumenta un porcentaje variable en funcion de tus atributos
        self.p_atributo = p_atributo # Consumibles para mejorar solo los atributos
        self.p_atributo_max = p_atributo_max # Numero máximo de atributos para poder utilizar
        self.p_habilidad = p_habilidad # Consumibles para mejorar solo las habilidades
        self.p_habilidad_max = p_habilidad_max # Numero máximo de habilidades para poder utilizar
        self.hambre = hambre # Afecta directamente a la felicidad y al sueño si llega a 0 durante 3 dias mueres
        self.hambre_max = hambre_max
        self.sed = sed # Afecta directamente a la felicidad y al sueño si llega a 0 durante 7 dias mueres
        self.sed_max = sed_max
        self.felicidad = felicidad # Afecta al personaje, en caso de tener depresion se puede suicidar y tienes que crearte nuevo personaje
        self.felicidad_max = felicidad_max
        self.sueño = sueño # Afecta a tus estadisticas y limita al personaje a descansar() porque sino reduce a la mitad todas las estadisticas
        self.sueño_max = sueño_max
        self.estamina = estamina # La energía se consume en combate
        self.estamina_max = estamina_max
        self.energia = energia # La estamina se consume para hacer acciones como abrir pistachos
        self.energia_max = energia_max

        # ATRIBUTOS (afectan a las características principales) +3 por nivel
        self.vitalidad = vitalidad # Aumenta los puntos maximos de vida
        self.robustez = robustez # Aumenta los puntos de defensa base y maxima
        self.agilidad = agilidad # Aumenta los puntos de velocidad base y maxima
        self.meditacion = meditacion # Aumenta los puntos de mana base y maxima
        self.apetito = apetito # Aumenta los puntos de hambre/sed base y maxima
        self.mentalidad_fuerte = mentalidad_fuerte # Aumenta los puntos de felicidad base y maxima
        
        # HABILIDADES (afectan a las características principales) +1 por nivel
        self.superviviente = superviviente # Reduce el consumo de hambre y sed
        self.eficiente = eficiente # Crea una probabilidad de obtener 1 u 2 de puntos para atributos extra
        self.autodidacta = autodidacta # Reduce la exp_max necesaria para poder subir de nivel mas rapido
        self.crecimento_emocional = crecimento_emocional # Reduce el consumo de felicidad
        self.insomnio = insomnio # Reduce el consumo de sueño
        self.deportista = deportista # Reduce el consumo de estamina en combate
        self.medico = medico # Aumenta un porcentaje extra de curación de las pociones
        self.sabio = sabio # Reduce un porcentaje del consumo del mana

class Mono(Clase):
    def __init__(self, vitalidad, meditacion, robustez, mana, mana_max, sabio, vida, medico, agilidad, apetito, deportista, mentalidad_fuerte, superviviente, insomnio, crecimento_emocional, autodidacta, eficiente, vida_max, defensa, defensa_max, p_habilidad, p_atributo, p_habilidad_max, p_atributo_max, nivel, exp, exp_max, velocidad, velocidad_max, hambre, hambre_max, sed, sed_max, felicidad, felicidad_max, sueño, sueño_max, estamina, estamina_max, energia, energia_max, daño_base):
        daño_base = 3
        vida = 
        vida_max = 
        defensa = 
        defensa_max = 
        mana = 
        mana_max = 
        velocidad = 
        velocidad_max = 
        nivel = 
        exp = 
        exp_max = 
        p_atributo = 
        p_atributo_max = 
        p_habilidad = 
        p_habilidad_max = 
        hambre = 
        hambre_max = 
        sed = 
        sed_max = 
        felicidad = 
        felicidad_max = 
        sueño = 
        sueño_max = 
        estamina = 
        estamina_max = 
        energia = 
        energia_max = 
        super().__init__(self, vitalidad, meditacion, robustez, mana, mana_max, sabio, vida, medico, agilidad, apetito, deportista, mentalidad_fuerte, superviviente, insomnio, crecimento_emocional, autodidacta, eficiente, vida_max, defensa, defensa_max, p_habilidad, p_atributo, p_habilidad_max, p_atributo_max, nivel, exp, exp_max, velocidad, velocidad_max, hambre, hambre_max, sed, sed_max, felicidad, felicidad_max, sueño, sueño_max, estamina, estamina_max, energia, energia_max, daño_base)
        self.daño_base = daño_base
        self.vida = vida
        self.vida_max = vida_max
        self.defensa = defensa
        self.defensa_max = defensa_max