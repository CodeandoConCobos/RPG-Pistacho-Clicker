class Clase:
    def __init__(self, data):
        # INFO BASE
        self.name = data['name']
        self.daño_base = data['daño_base']
        
        # STATS
        self.vida = data['vida'] # Vida actual del jugador
        self.vida_max = data['vida_max'] # Vida maxima del jugador
        self.defensa = data['defensa'] # Defensa actual del jugador
        self.defensa_max = data['defensa_max'] # Defensa actual del jugador
        self.mana = data['mana'] # Mana actual del jugador
        self.mana_max = data['mana_max'] # Mana actual del jugador
        self.velocidad = data['velocidad'] # Esta caracteristica determina quien ataca primero en un juego de turnos
        self.velocidad_max = data['velocidad_max'] # Necesitamos un maximo ya que durante el combate la velocidad puede subir 
        self.nivel = data['nivel'] # Aumenta las estadsiticas base en función de tu clase hijo como Mono() y te da puntos de atributos para poder elegir cual subir
        self.exp = data['exp'] # Experiencia normalmente 0
        self.exp_max = data['exp_max'] # cuando igualaas o superas la exp_max subes de nivel y exp pasa a 0 y exp_max aumenta un porcentaje variable en funcion de tus atributos
        self.p_atributo = data['p_atributo'] # Consumibles para mejorar solo los atributos
        self.p_atributo_max = data['p_atributo_max'] # Numero máximo de atributos para poder utilizar
        self.p_habilidad = data['p_habilidad'] # Consumibles para mejorar solo las habilidades
        self.p_habilidad_max = data['p_habilidad_max'] # Numero máximo de habilidades para poder utilizar
        self.hambre = data['hambre'] # Afecta directamente a la felicidad y al sueño si llega a 0 durante 3 dias mueres
        self.hambre_max = data['hambre_max']
        self.sed = data['sed'] # Afecta directamente a la felicidad y al sueño si llega a 0 durante 7 dias mueres
        self.sed_max = data['sed_max']
        self.felicidad = data['felicidad'] # Afecta al personaje, en caso de tener depresion se puede suicidar y tienes que crearte nuevo personaje
        self.felicidad_max = data['felicidad_max']
        self.sueño = data['sueño'] # Afecta a tus estadisticas y limita al personaje a descansar() porque sino reduce a la mitad todas las estadisticas
        self.sueño_max = data['sueño_max']
        self.estamina = data['estamina'] # La energía se consume en combate
        self.estamina_max = data['estamina_max']
        self.energia = data['energia'] # La estamina se consume para hacer acciones como abrir pistachos
        self.energia_max = data['energia_max']

        # ATRIBUTOS (afectan a las características principales) +3 por nivel
        self.vitalidad = data['vitalidad'] # Aumenta los puntos maximos de vida
        self.robustez = data['robustez'] # Aumenta los puntos de defensa base y maxima
        self.agilidad = data['agilidad'] # Aumenta los puntos de velocidad base y maxima
        self.meditacion = data['meditacion'] # Aumenta los puntos de mana base y maxima
        self.apetito = data['apetito'] # Aumenta los puntos de hambre/sed base y maxima
        self.mentalidad_fuerte = data['mentalidad_fuerte'] # Aumenta los puntos de felicidad base y maxima
        
        # HABILIDADES (afectan a las características principales) +1 por nivel
        self.superviviente = data['superviviente'] # Reduce el consumo de hambre y sed
        self.eficiente = data['eficiente'] # Crea una probabilidad de obtener 1 u 2 de puntos para atributos extra
        self.autodidacta = data['autodidacta'] # Reduce la exp_max necesaria para poder subir de nivel mas rapido
        self.crecimento_emocional = data['crecimento_emocional'] # Reduce el consumo de felicidad
        self.insomnio = data['insomnio'] # Reduce el consumo de sueño
        self.deportista = data['deportista'] # Reduce el consumo de estamina en combate
        self.medico = data['medico'] # Aumenta un porcentaje extra de curación de las pociones
        self.sabio = data['sabio'] # Reduce un porcentaje del consumo del mana
        
    def atacar(self, enemigo):
            danio_total = self.daño_base - enemigo.defensa
            
            if danio_total > 0:
                enemigo.vida -= danio_total
                print(f"{self.name} ha infligido {danio_total} puntos de daño a {enemigo.name}!")
            else:
                print(f"{self.name} no ha infligido ningún daño a {enemigo.name} debido a su defensa alta.")
        
class Mono(Clase):
    def __init__(self, data):
        super().__init__(data)
        
        # INFO BASE
        self.name = data.get('name', 'Mono')
        self.daño_base = data.get('daño_base', 3)
        
        # STATS
        self.vida = data.get('vida', 50)
        self.vida_max = data.get('vida_max', 50)
        self.defensa = data.get('defensa', 3)
        self.defensa_max = data.get('defensa_max', 5)
        self.mana = data.get('mana', 0)
        self.mana_max = data.get('mana_max', 0)
        self.velocidad = data.get('velocidad', 5)
        self.velocidad_max = data.get('velocidad_max', 10)
        self.nivel = data.get('nivel', 0)
        self.exp = data.get('exp', 0)
        self.exp_max = data.get('exp_max', 100)
        self.p_atributo = data.get('p_atributo', 0)
        self.p_atributo_max = data.get('p_atributo_max', 0)
        self.p_habilidad = data.get('p_habilidad', 0)
        self.p_habilidad_max = data.get('p_habilidad_max', 0)
        self.hambre = data.get('hambre', 25)
        self.hambre_max = data.get('hambre_max', 25)
        self.sed = data.get('sed', 25)
        self.sed_max = data.get('sed_max', 25)
        self.felicidad = data.get('felicidad', 25)
        self.felicidad_max = data.get('felicidad_max', 50)
        self.sueño = data.get('sueño', 25)
        self.sueño_max = data.get('sueño_max', 50)
        self.estamina = data.get('estamina', 20)
        self.estamina_max = data.get('estamina_max', 20)
        self.energia = data.get('energia', 50)
        self.energia_max = data.get('energia_max', 50)
        
        # ATRIBUTOS
        self.vitalidad = data.get('vitalidad', 0)
        self.robustez = data.get('robustez', 0)
        self.agilidad = data.get('agilidad', 0)
        self.meditacion = data.get('meditacion', 0)
        self.apetito = data.get('apetito', 0)
        self.mentalidad_fuerte = data.get('mentalidad_fuerte', 0)
        
        # HABILIDADES
        self.superviviente = data.get('superviviente', 0)
        self.eficiente = data.get('eficiente', 0)
        self.autodidacta = data.get('autodidacta', 0)
        self.crecimento_emocional = data.get('crecimiento_emocional', 0)
        self.insomnio = data.get('insomnio', 0)
        self.deportista = data.get('deportista', 0)
        self.medico = data.get('medico', 0)
        self.sabio = data.get('sabio', 0)

class Payaso(Clase):
    def __init__(self, data):
        super().__init__(data)
        
        # INFO BASE
        self.name = data.get('name', 'Payaso')
        self.daño_base = data.get('daño_base', 7)
        
        # STATS
        self.vida = data.get('vida', 20)
        self.vida_max = data.get('vida_max', 20)
        self.defensa = data.get('defensa', 7)
        self.defensa_max = data.get('defensa_max', 10)
        self.mana = data.get('mana', 15)
        self.mana_max = data.get('mana_max', 15)
        self.velocidad = data.get('velocidad', 8)
        self.velocidad_max = data.get('velocidad_max', 16)
        self.nivel = data.get('nivel', 0)
        self.exp = data.get('exp', 0)
        self.exp_max = data.get('exp_max', 210)
        self.p_atributo = data.get('p_atributo', 0)
        self.p_atributo_max = data.get('p_atributo_max', 0)
        self.p_habilidad = data.get('p_habilidad', 0)
        self.p_habilidad_max = data.get('p_habilidad_max', 0)
        self.hambre = data.get('hambre', 25)
        self.hambre_max = data.get('hambre_max', 25)
        self.sed = data.get('sed', 25)
        self.sed_max = data.get('sed_max', 25)
        self.felicidad = data.get('felicidad', 25)
        self.felicidad_max = data.get('felicidad_max', 50)
        self.sueño = data.get('sueño', 25)
        self.sueño_max = data.get('sueño_max', 50)
        self.estamina = data.get('estamina', 15)
        self.estamina_max = data.get('estamina_max', 15)
        self.energia = data.get('energia', 35)
        self.energia_max = data.get('energia_max', 35)
        
        # ATRIBUTOS
        self.vitalidad = data.get('vitalidad', 0)
        self.robustez = data.get('robustez', 0)
        self.agilidad = data.get('agilidad', 0)
        self.meditacion = data.get('meditacion', 0)
        self.apetito = data.get('apetito', 0)
        self.mentalidad_fuerte = data.get('mentalidad_fuerte', 0)
        
        # HABILIDADES
        self.superviviente = data.get('superviviente', 0)
        self.eficiente = data.get('eficiente', 0)
        self.autodidacta = data.get('autodidacta', 0)
        self.crecimento_emocional = data.get('crecimento_emocional', 3)
        self.insomnio = data.get('insomnio', 5)
        self.deportista = data.get('deportista', 0)
        self.medico = data.get('medico', 0)
        self.sabio = data.get('sabio', 0)
