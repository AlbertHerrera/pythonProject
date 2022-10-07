
def horas_a_segundos(horas):
    minutos = horas*60
    segundos = minutos * 60
    return segundos
def monedas_por_segundo(time):
    monedas_por_juego=146
    segundos_por_juego=1.20*60
    time = float(time)
    monedas = time/segundos_por_juego*monedas_por_juego
    return monedas


segundos = horas_a_segundos(1)
segundos = segundos + 180
print(segundos)
