from neurona_simple import NeuronaSimple

if __name__ == '__main__':
    print("xor 0, 0, 0")
    neurona_1= NeuronaSimple(entrada_1=0, entrada_2=0, peso_0=0.9, peso_1=0.7, peso_2=0.5)
    neurona_2 = NeuronaSimple(entrada_1=0, entrada_2=0, peso_0=0.3, peso_1=-0.9, peso_2=-1)
    neurona_3 = NeuronaSimple(entrada_1=0, entrada_2=0, peso_0=0.8, peso_1=0.35, peso_2=0.1)
    salida_1 = neurona_1.entrenamiento()
    salida_2 = neurona_2.entrenamiento()
    salida_3 = neurona_3.entrenamiento()
    neurona_4 = NeuronaSimple(entrada_1=salida_1, entrada_2=salida_2, entrada_3=salida_3, peso_0=-0.23, peso_1=-0.79, peso_2=0.56, peso_3=0.6, salida_esperada=0)
    salida_4 = neurona_4.entrenamiento()
    for i in range(100000):
        salida_1_back = neurona_1.entrenamiento_back(salida_4)
        salida_2_back = neurona_2.entrenamiento_back(salida_4)
        salida_3_back = neurona_3.entrenamiento_back(salida_4)
        neurona_4.entrada_1 = salida_1_back
        neurona_4.entrada_2 = salida_1_back
        neurona_4.entrada_3 = salida_1_back
        salida_4 = neurona_4.entrenamiento()
    print(f"neurona_4: {neurona_4}")
    print("xor 0, 1, 1")
    neurona_1= NeuronaSimple(entrada_1=0, entrada_2=1, peso_0=0.9, peso_1=0.7, peso_2=0.5)
    neurona_2 = NeuronaSimple(entrada_1=0, entrada_2=1, peso_0=0.3, peso_1=-0.9, peso_2=-1)
    neurona_3 = NeuronaSimple(entrada_1=0, entrada_2=1, peso_0=0.8, peso_1=0.35, peso_2=0.1)
    salida_1 = neurona_1.entrenamiento()
    salida_2 = neurona_2.entrenamiento()
    salida_3 = neurona_3.entrenamiento()
    neurona_4 = NeuronaSimple(entrada_1=salida_1, entrada_2=salida_2, entrada_3=salida_3, peso_0=-0.23, peso_1=-0.79, peso_2=0.56, peso_3=0.6, salida_esperada=1)
    salida_4 = neurona_4.entrenamiento()
    for i in range(100000):
        salida_1_back = neurona_1.entrenamiento_back(salida_4)
        salida_2_back = neurona_2.entrenamiento_back(salida_4)
        salida_3_back = neurona_3.entrenamiento_back(salida_4)
        neurona_4.entrada_1 = salida_1_back
        neurona_4.entrada_2 = salida_1_back
        neurona_4.entrada_3 = salida_1_back
        salida_4 = neurona_4.entrenamiento()
    print(f"neurona_4: {neurona_4}")
    print("xor 1, 0, 1")
    neurona_1= NeuronaSimple(entrada_1=1, entrada_2=0, peso_0=0.9, peso_1=0.7, peso_2=0.5)
    neurona_2 = NeuronaSimple(entrada_1=1, entrada_2=0, peso_0=0.3, peso_1=-0.9, peso_2=-1)
    neurona_3 = NeuronaSimple(entrada_1=1, entrada_2=0, peso_0=0.8, peso_1=0.35, peso_2=0.1)
    salida_1 = neurona_1.entrenamiento()
    salida_2 = neurona_2.entrenamiento()
    salida_3 = neurona_3.entrenamiento()
    neurona_4 = NeuronaSimple(entrada_1=salida_1, entrada_2=salida_2, entrada_3=salida_3, peso_0=-0.23, peso_1=-0.79, peso_2=0.56, peso_3=0.6, salida_esperada=1)
    salida_4 = neurona_4.entrenamiento()
    for i in range(100000):
        salida_1_back = neurona_1.entrenamiento_back(salida_4)
        salida_2_back = neurona_2.entrenamiento_back(salida_4)
        salida_3_back = neurona_3.entrenamiento_back(salida_4)
        neurona_4.entrada_1 = salida_1_back
        neurona_4.entrada_2 = salida_1_back
        neurona_4.entrada_3 = salida_1_back
        salida_4 = neurona_4.entrenamiento()
    print(f"neurona_4: {neurona_4}")
    print("xor 1, 1, 0")
    neurona_1= NeuronaSimple(entrada_1=1, entrada_2=1, peso_0=0.9, peso_1=0.7, peso_2=0.5)
    neurona_2 = NeuronaSimple(entrada_1=1, entrada_2=1, peso_0=0.3, peso_1=-0.9, peso_2=-1)
    neurona_3 = NeuronaSimple(entrada_1=1, entrada_2=1, peso_0=0.8, peso_1=0.35, peso_2=0.1)
    salida_1 = neurona_1.entrenamiento()
    salida_2 = neurona_2.entrenamiento()
    salida_3 = neurona_3.entrenamiento()
    neurona_4 = NeuronaSimple(entrada_1=salida_1, entrada_2=salida_2, entrada_3=salida_3, peso_0=-0.23, peso_1=-0.79, peso_2=0.56, peso_3=0.6, salida_esperada=0)
    salida_4 = neurona_4.entrenamiento()
    for i in range(100000):
        salida_1_back = neurona_1.entrenamiento_back(salida_4)
        salida_2_back = neurona_2.entrenamiento_back(salida_4)
        salida_3_back = neurona_3.entrenamiento_back(salida_4)
        neurona_4.entrada_1 = salida_1_back
        neurona_4.entrada_2 = salida_1_back
        neurona_4.entrada_3 = salida_1_back
        salida_4 = neurona_4.entrenamiento()
    print(f"neurona_4: {neurona_4}")
