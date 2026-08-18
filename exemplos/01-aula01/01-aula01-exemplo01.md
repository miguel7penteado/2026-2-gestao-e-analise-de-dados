# Exemplo 01 -
Uma pesquisa foi realizada com o objetivo de verificar se existe associação entre a falta de sono e a capacidade de as pessoas resolverem problemas simples. Foram testadas 10 pessoas, mantendo-se sem dormir por um determinado número de horas. Após cada um destes períodos, cada pessoa teve de resolver um teste com adições simples, anotando-se então os erros cometidos. Os dados resultantes são os seguintes:

| Pessoa Observada (i) | **Número de Horas sem Dormir ( X )** | **Número de Erros ( Y )** |
|:--------------------:|:------------------------------------:|:-------------------------:|
|           1          |                  8                   |             6             |
|           2          |                  8                   |             8             |
|           3          |                  12                  |             6             |
|           4          |                  12                  |            10             |
|           5          |                  16                  |             8             |
|           6          |                  16                  |            14             |
|           7          |                  20                  |            12             |
|           8          |                  20                  |            14             |
|           9          |                  24                  |            12             |
|          10          |                  24                  |            16             |

- a) Calcule o **coeficiente de correlação linear** de Pearson, interprete e teste sua significância a **5%**.
- b) Ajuste, **teste e interprete o modelo de regressão linear** simples.

No python Comece importando os cabeçalhos:
- importe a biblioteca **numpy** para criar vetores de valores
- importe a biblioteca **stats** para usar as funções para `linregress` para calcular a regressão linear
- importe a biblioteca **stats** para usar as funções para `pearsonr`   para calcular o coeficiente de correlação `r`


```
import numpy as np
from scipy import stats
from yt_dlp.extractor import agora
```

Agora precisamos criar uma função para calcular a **regressão linear**


```
def calcular_regressao_linear(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    """Calcula os parâmetros e o teste de significância da regressão linear simples."""
    print("--- b) Modelo de Regressão Linear Simples ---")
    # Ajustando a reta de regressão e obtendo estatísticas completas
    inclinacao_reta, interceptacao, correlacao_r, valor_p, erro_padrao = stats.linregress(x, y)
    print(f"Coeficiente Angular ( m ): {inclinacao_reta:.4f}")
    print(f"Intercepto ( n ): {interceptacao:.4f}")
    print(f"Equação ajustada: Y_hat = {interceptacao:.4f} + {inclinacao_reta:.4f} * X")
    print(f"P-valor do coeficiente angular (teste do modelo): {valor_p:.5f}")

    if ( valor_p < 0.05):
        print("Conclusão: O modelo de regressão linear é estatisticamente significativo a 5%.")
    else:
        print("Conclusão: O modelo não é estatisticamente significativo.")

    return interceptacao, inclinacao_reta, valor_p

```

Agora precisamos criar uma função para calcular o **coeficiente de correlação** `r`


```
def calcular_correlacao_pearson(v_independentes_x: np.ndarray, v_dependentes_y: np.ndarray) -> tuple[float, float]:
    """Calcula o coeficiente de correlação de Pearson e o p-valor correspondente."""
    print("--- a) Coeficiente de Correlação de Pearson e Teste ---")
    coeficiente_de_correlacao_r, valor_de_p = stats.pearsonr(v_independentes_x, v_dependentes_y)

    print(f"Coeficiente de Correlação (r): {coeficiente_de_correlacao_r:.4f}")
    print(f"P-valor da correlação: {valor_de_p:.5f}")

    if ( valor_de_p < 0.05):
        print("Conclusão: Rejeitamos a Hipótese. A correlação é estatisticamente relevante a 5%.\n")
    else:
        print("Conclusão: Não rejeitamos a Hipótese.\n")
    return coeficiente_de_correlacao_r, valor_de_p
```

Agora vamos definir a ordem de execução das funções:


```
def funcao_principal() -> None:
    # Carregar os valores de X (que é a variável independente) no vetor variaveis_independentes_x
    # X: Número de horas sem dormir
    variaveis_independentes_x = np.array([8, 8, 12, 12, 16, 16, 20, 20, 24, 24])

    # # Carregar os valores de Y (que é a variável independente) no vetor variaveis_dependentes_y
    # Y: Número de erros
    variaveis_dependentes_y = np.array([6, 8, 6, 10, 8, 14, 12, 14, 12, 16])

    # Executando a correlação
    calcular_correlacao_pearson(variaveis_independentes_x, variaveis_dependentes_y)

    # Executando a regressão linear
    calcular_regressao_linear(variaveis_independentes_x, variaveis_dependentes_y)

```

Finalmente, vamos iniciar o **fluxo principal** do programa, chamado a **funcao_principal()** que chamará todas as outras na ordem


```
if __name__ == '__main__':
    funcao_principal()
```

    --- a) Coeficiente de Correlação de Pearson e Teste ---
    Coeficiente de Correlação (r): 0.8015
    P-valor da correlação: 0.00531
    Conclusão: Rejeitamos a Hipótese. A correlação é estatisticamente relevante a 5%.
    
    --- b) Modelo de Regressão Linear Simples ---
    Coeficiente Angular ( m ): 0.4750
    Intercepto ( n ): 3.0000
    Equação ajustada: Y_hat = 3.0000 + 0.4750 * X
    P-valor do coeficiente angular (teste do modelo): 0.00531
    Conclusão: O modelo de regressão linear é estatisticamente significativo a 5%.
    

Como ficou a equação descoberta pela **regressão linear simples** ?

Uma equação de reta segue o formato $y = mx + n$.

$ y = \underbrace{m}_{\text{coeficiente angular}} x + \underbrace{n}_{\text{coeficiente linear}} $

No exercício:
 - o valor de `m` é dado pelo valor do `coeficiente angular` ;
 - o valor de `n` é dado pelo valor do `intercepto` ;

Então a equação ficou:
$$
y = 0,4750(x) + 3
$$



