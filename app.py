import streamlit as st

# 1️⃣ BASE DE DATOS DE 9 PREGUNTAS (SUMAS Y RESTAS)
preguntas = [
    {"texto": "¿Cuánto es 5 + 3?", "opciones": ["6", "7", "8", "9"], "correcta": "8"},
    {"texto": "¿Cuánto es 10 - 4?", "opciones": ["5", "6", "7", "8"], "correcta": "6"},
    {"texto": "¿Cuánto es 7 + 6?", "opciones": ["12", "13", "14"], "correcta": "13"},
    {"texto": "¿Cuánto es 15 - 9?", "opciones": ["5", "6", "7"], "correcta": "6"},
    {"texto": "¿Cuánto es 4 + 9?", "opciones": ["12", "13", "14"], "correcta": "13"},
    {"texto": "¿Cuánto es 20 - 5?", "opciones": ["14", "15", "16"], "correcta": "15"},
    {"texto": "¿Cuánto es 8 + 7?", "opciones": ["14", "15", "16"], "correcta": "15"},
    {"texto": "¿Cuánto es 12 - 3?", "opciones": ["8", "9", "10"], "correcta": "9"},
    {"texto": "¿Cuánto es 9 + 5?", "opciones": ["13", "14", "15"], "correcta": "14"}
]

# CONFIGURACIÓN
st.title("➕➖ Examen de Sumas y Restas")
st.write("Responde y pulsa el botón para ver tu nota.")

with st.form("quiz_form"):

    respuestas_usuario = []

    for i, pregunta in enumerate(preguntas):
        st.subheader(pregunta["texto"])

        opciones = ["Dejar en blanco"] + pregunta["opciones"]

        eleccion = st.radio(
            "Elige una opción:",
            opciones,
            key=f"pregunta_{i}"
        )

        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar Examen")

# 3️⃣ CORRECCIÓN
if boton_enviar:

    aciertos = 0
    errores = 0
    total = len(preguntas)

    resultados_detalle = []

    for i in range(total):

        if respuestas_usuario[i] == "Dejar en blanco":
            resultados_detalle.append(f"❔ Pregunta {i+1}: Sin responder")
            continue

        elif respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1
            resultados_detalle.append(f"✅ Pregunta {i+1}: Correcta")

        else:
            errores += 1
            resultados_detalle.append(
                f"❌ Pregunta {i+1}: Incorrecta (Correcta: {preguntas[i]['correcta']})"
            )

    # Penalización: cada error resta 0.5
    puntuacion = aciertos - (errores * 0.5)

    if puntuacion < 0:
        puntuacion = 0

    nota = (puntuacion / total) * 10

    # 🔵 REDONDEO
    nota = round(nota, 2)

    st.divider()
    st.header(f"Resultado final: {nota} / 10")

    # 4️⃣ FEEDBACK POR TRAMOS
    if nota < 2:
        st.error("Muy insuficiente 😢 Necesitas practicar más.")
    elif 2 <= nota < 5:
        st.warning("Insuficiente 😕 Sigue practicando.")
    elif 5 <= nota < 6:
        st.info("Suficiente 🙂 Has aprobado por poco.")
        st.balloons()
    elif 6 <= nota < 7:
        st.success("Bien 👍 Buen trabajo.")
        st.balloons()
    elif 7 <= nota < 9:
        st.success("Notable 👏 Muy buen resultado.")
        st.balloons()
    elif 9 <= nota < 10:
        st.success("Sobresaliente 🌟 Excelente trabajo.")
        st.balloons()
    elif nota == 10:
        st.success("🏆 EXCELENTE 🏆 ¡Perfecto!")
        st.balloons()
        st.snow()

    # 5️⃣ TAB CON INFORME
    tab1, tab2 = st.tabs(["📊 Resultado", "📝 Informe Detallado"])

    with tab2:
        st.markdown("## Informe del examen")
        st.markdown(f"**Aciertos:** {aciertos}")
        st.markdown(f"**Errores:** {errores}")
        st.markdown(f"**Nota final:** {nota}/10")
        st.markdown("---")

        for resultado in resultados_detalle:
            st.markdown(resultado)
