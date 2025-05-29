import joblib

def prever_resultado(time_casa, time_fora):
    try:
        modelo_resultado = joblib.load("ROBO/dados/modelo_resultado.pkl")
        modelo_gols = joblib.load("ROBO/dados/modelo_gols.pkl")
        modelo_cantos = joblib.load("ROBO/dados/modelo_cantos.pkl")
    except:
        return " encontrados."

    mapa_times = {
        "al ahly": 1, "barcelona": 2, "bayern munique": 3, "chelsea": 4,
        "esperance": 5, "flamengo": 6, "kaizer chiefs": 7, "man city": 8,
        "psg": 9, "real madrid": 10, "river plate": 11, "zamalek": 12
    }

    time_casa = time_casa.lower().strip()
    time_fora = time_fora.lower().strip()

    casa = mapa_times.get(time_casa, 0)
    fora = mapa_times.get(time_fora, 0)

    if casa == 0 or fora == 0:
        return "⚠️ Um dos times não está no banco de dados."

    dados = [[casa, fora, 2, 1]]

    resultado = modelo_resultado.predict(dados)[0]
    gols = modelo_gols.predict(dados)[0]
    cantos = modelo_cantos.predict(dados)[0]

    texto_resultado = "🏁 Resultado provável: **{}**".format(resultado.upper())
    texto_gols = "🔥 Mais de 2.5 gols esperados!" if gols == 1 else "⚠️ Menos de 2.5 gols esperados."
    texto_cantos = "🚩 Alta chance de +8.5 escanteios!" if cantos == 1 else "📉 Baixa chance de escanteios."

    return "{}\n\n{}\n{}".format(texto_resultado, texto_gols, texto_cantos)
