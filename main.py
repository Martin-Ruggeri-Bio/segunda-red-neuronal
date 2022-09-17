from neurona_simple import NeuronaSimple

if __name__ == '__main__':
    red_neuronal = {}
    neurona_1= NeuronaSimple(entrada_1=0, entrada_2=0, peso_0=0.9, peso_1=0.7, peso_2=0.5)
    neurona_2 = NeuronaSimple(entrada_1=0, entrada_2=0, peso_0=0.3, peso_1=-0.9, peso_2=-1)
    salida_1 = neurona_1.entrenamiento()
    salida_2 = neurona_2.entrenamiento()
    neurona_3 = NeuronaSimple(entrada_1=salida_1, entrada_2=salida_2, peso_0=0.8, peso_1=0.35, peso_2=0.1)
    neurona_4 = NeuronaSimple(entrada_1=salida_1, entrada_2=salida_2, peso_0=-0.23, peso_1=-0.79, peso_2=0.56)
    neurona_5 = NeuronaSimple(entrada_1=salida_1, entrada_2=salida_2, peso_0=0.6, peso_1=-0.6, peso_2=0.22)
    salida_1 = neurona_3.entrenamiento()
    salida_2 = neurona_4.entrenamiento()
    salida_3 = neurona_5.entrenamiento()
    neurona_6 = NeuronaSimple(entrada_1=salida_1, entrada_2=salida_2, entrada_3=salida_3, peso_0=-0.22, peso_1=-0.55, peso_2=0.31, peso_3=-0.32)
    salida_4 = neurona_6.entrenamiento()
    print(f"neurona_1: {neurona_1}")
    print(f"neurona_2: {neurona_2}")
    print(f"neurona_3: {neurona_3}")
    print(f"neurona_4: {neurona_4}")
    print(f"neurona_5: {neurona_5}")
    print(f"neurona_6: {neurona_6}")

