import joblib

def prever_resultado(time_casa, time_fora):
    try:
        modelo_resultado = joblib.load("ROBO/dados/modelo_resultado.pkl")
        modelo_gols = joblib.load("ROBO/dados/modelo_gols.pkl")
        modelo_cantos = joblib.load("ROBO/dados/modelo_cantos.pkl")
    except:
        return "⚠️ Modelos não encontrados."

    mapa_times = {
        "flamengo": 1, "chelsea": 2, "psg": 3, "al ahly": 4, "barcelona": 5, 
        "kaizer chiefs": 6, "river plate": 7, "real madrid": 8, 
        "bayern munique": 9, "zamalek": 10, "man city": 11, "esperance": 12
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

    texto_resultado = f"🏁 Resultado provável: **{resultado.upper()}**"
    texto_gols = "🔥 Mais de 2.5 gols esperados!" if gols == 1 else "⚠️ Menos de 2.5 gols esperados."
    texto_cantos = "🚩 Alta chance de +8.5 escanteios!" if cantos == 1 else "📉 Baixa chance de escanteios."

    return f"{texto_resultado}\n\n{texto_gols}\n{texto_cantos}"