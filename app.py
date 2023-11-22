import numpy as np
import pickle
import streamlit as st

# Path del modelo preentrenado
MODEL_PATH = 'models/pickle_model.pkl'

# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):
    expected_features = len(model.support_vectors_[0])
    print("Número de características esperadas por el modelo:", expected_features)

    x = np.asarray(x_in).reshape(1, -1)
    preds = model.predict(x)

    return preds

def main():
    model = ''

    # Se carga el modelo
    if model == '':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA DE DETECCION DE RIESGO OBSTETRICO PRENATAL </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Lectura de datos
    EDAD   = st.text_input("EDAD  :")
    ESTADO_ACTUAL_DE_USUARIA = st.text_input("ESTADO_ACTUAL_DE_USUARIA:")
    GESTACIONS = st.text_input("GESTACIONS:")
    PARTOS = st.text_input("PARTOS:")
    CESAREAS = st.text_input("CESAREAS:")
    ABORTOS   = st.text_input("ABORTOS  :")
    MUERTOS = st.text_input("MUERTOS:")
    VIVOS = st.text_input("VIVOS:")
    ETIQUETA_DIABETES = st.text_input("ETIQUETA_DIABETES:")
    HIPERTENSION_ARTERIAL = st.text_input("HIPERTENSION_ARTERIAL:")
    VIH = st.text_input("VIH:")
    TUBERCULOSIS = st.text_input("TUBERCULOSIS:")
    SIFILIS = st.text_input("SIFILIS:")
    HABITOS_DE_RIESGO = st.text_input("HABITOS_DE_RIESGO:")
 
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 
        x_in = [np.float_(EDAD.title()),
                np.float_(ESTADO_ACTUAL_DE_USUARIA.title()),
                np.float_(GESTACIONS.title()),
                np.float_(PARTOS.title()),
                np.float_(CESAREAS.title()),
                np.float_(ABORTOS.title()),
                np.float_(MUERTOS.title()),
                np.float_(VIVOS.title()),
                np.float_(ETIQUETA_DIABETES.title()),
                np.float_(HIPERTENSION_ARTERIAL.title()),
                np.float_(VIH.title()),
                np.float_(TUBERCULOSIS.title()),
                np.float_(SIFILIS.title()),
                np.float_(HABITOS_DE_RIESGO.title())]  # Agregar esta línea para la última característica

        predictS = model_prediction(x_in, model)
        st.success('¿ La madre tendra complicaciones durante el parto ?: {}'.format("Sí" if predictS[0] == 1 else "No"))

if __name__ == '__main__':
    main()
