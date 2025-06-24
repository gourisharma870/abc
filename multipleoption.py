import pickle
from streamlit_option_menu import option_menu
import streamlit as st

diabetes_model=pickle.load(open('D:\internship\sav\diabetes_model.sav','rb'))
parkinson_model=pickle.load(open('D:\internship\sav\park_models.sav','rb'))
heart_model=pickle.load(open('D:\internship\sav\heart_models.sav','rb'))

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)
if(selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    col1,col2,col3=st.columns(3)
   
    with col1:
        Pregnancies=st.text_input('Enter number of pregnancies')
    with col2:
        Glucose=st.text_input('Enter Glucose')
    with col3:
        BloodPressure=st.text_input('Enter blood Pressure')
    with col1:
        SkinThickness=st.text_input('Enter skin thickness')
    with col2:
        Insulin=st.text_input('Enter insulin')
    with col3:
        BMI=st.text_input('Enter bmi')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Enter Diabetes digree function')
    with col2:
        Age=st.text_input('Enter Age')
    dia_diagnosis=''
    if st.button('Result'):
        dia_prediction=diabetes_model.predict([[float(Pregnancies),float(Glucose),float(BloodPressure),float(SkinThickness) ,float(Insulin),float(BMI),float(DiabetesPedigreeFunction),float(Age)]])
        if(dia_prediction[0]==1):
            dia_diagnosis="You have diabetes"
        else:
            dia_diagnosis="You do not have diabetes"
    st.success(dia_diagnosis)
if(selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
   
    col1,col2,col3,col4=st.columns(4)
   
    with col1:
        age=st.text_input('Enter Age')
    with col2:
        sex=st.text_input('Enter gender')
    with col3:
        cp=st.text_input('Enter cp')
    with col4:
        trestbps=st.text_input('Enter trestbps')
    with col1:
        chol=st.text_input('Enter chol')
    with col2:
        fbs=st.text_input('Enter fbs')
    with col3:
        restecg=st.text_input('Enter restecg')
    with col4:
        thalach=st.text_input('Enter thalach')
    with col1:
        exang=st.text_input('enter exang')
    with col2:
        oldpeak=st.text_input('enter oldpeak')
    with col3:
        slope=st.text_input('slope')
    with col4:
        ca=st.text_input('Enter ca')
    with col1:
        thal=st.text_input('Enter thal')
    heart_diagnosis=''
    if st.button('Result'):
        heart_prediction=heart_model.predict([[float(age),float(sex),float(cp),float(trestbps),float(chol),float(fbs),float(restecg),float(thalach),float(exang),float(oldpeak),float(slope),float(ca),float(thal)]])
        if(heart_prediction[0]==1):
            heart_diagnosis="You have heart disease"
        else:
            heart_diagnosis="You do not have heart disease"
    st.success(heart_diagnosis)
if(selected=='Parkinsons Prediction'):
    st.title('Parkinsons Disease Prediction')
   
    col1,col2,col3,col4=st.columns(4)
    with col1:
        name = st.text_input('name')
    with col2:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz)')
    with col3:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz)')
    with col4:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz)')
    with col1:
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col4:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col1:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col2:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col3:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col4:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col1:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col2:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col3:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col4:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col1:
        spread2 = st.text_input('spread2')
    with col2:
        D2 = st.text_input('D2')
    with col3:
        PPE = st.text_input('PPE')
    diagnosis=''
    if st.button('parkinsons Test Result'):
        park_diagnosis = parkinson_model.predict([[float(name),float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz),float(MDVP_Jitter_percent), float(MDVP_Jitter_Abs), float(MDVP_RAP), float(MDVP_PPQ), float(Jitter_DDP), float(MDVP_Shimmer), float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5), float(MDVP_APQ), float(Shimmer_DDA),float(NHR), float(HNR), float(RPDE), float(DFA),float(spread1), float(spread2), float(D2), float(PPE)]])
        if(park_diagnosis[0]==1):
            diagnosis="You have parkinsons"
        else:
           diagnosis="You do not have parkinsons"
    st.success(diagnosis)