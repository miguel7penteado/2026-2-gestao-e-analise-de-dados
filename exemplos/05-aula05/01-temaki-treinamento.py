import numpy as np
from sklearn.linear_model import LinearRegression

# --------------------------------------------------
# Dados de TREINO
# X = índice do bairro
# y = preço do temaki (R$)
# --------------------------------------------------

X_train = np.array([
    [3.0],   # Santana
    [4.0],   # Tatuapé
    [5.0],   # Mooca
    [6.0],   # Perdizes
    [7.0],   # Pinheiros
    [8.0],   # Vila Mariana
    [10.0]   # Itaim Bibi
])

y_train = np.array([
    24,
    27,
    29,
    33,
    35,
    39,
    44
])

# --------------------------------------------------
# Criando o modelo
# --------------------------------------------------

modelo = LinearRegression()

# --------------------------------------------------
# TREINAMENTO
# Aqui o modelo descobre w e b
# --------------------------------------------------

modelo.fit(X_train, y_train)

# --------------------------------------------------
# Parâmetros encontrados
# --------------------------------------------------

w = modelo.coef_[0]
b = modelo.intercept_

print(f"w = {w:.4f}")
print(f"b = {b:.4f}")

print()
print(f"Modelo treinado:")
print(f"y = {w:.4f}x + {b:.4f}")