![image](https://github.com/edpadua/Real_Estate_Analysis_App/blob/main/capture.gif)

# 🏡 Aplicativo de Análise e Recomendação Imobiliária
**(Real Estate Analysis and Recommendation App)**

Um projeto full-stack (Web e Data Science) desenvolvido em Python que utiliza um modelo de Machine Learning para estimar o "Preço Justo" de um imóvel com base em suas características e fornece uma recomendação de investimento clara.

---

## ✨ Funcionalidades Principais

* **Previsão de Preços:** Utiliza um modelo de **Regressão Linear Múltipla** (Scikit-learn) para calcular o valor de mercado esperado (Preço Justo) de um imóvel.
* **Recomendação de Investimento:** Compara o preço de venda informado pelo usuário com o preço previsto pelo modelo, classificando o imóvel como **'Ótima Oportunidade'**, **'Preço Alinhado'** ou **'Preço Elevado'**.
* **Interface Web Interativa:** Apresentação dos dados e resultados em um painel web dinâmico e fácil de usar, construído com **Streamlit**.
* **Transparência do Modelo:** Exibe a **Influência Estatística** das diferentes características (Área, Quartos, Distância do Centro) sobre o preço final.

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Uso Principal |
| :--- | :--- | :--- |
| **Linguagem** | Python | Lógica principal, Análise de Dados e Back-end. |
| **Modelagem** | Scikit-learn (Linear Regression) | Treinamento do modelo preditivo de preços. |
| **Web Framework** | Streamlit | Criação da interface web interativa (Front-end). |
| **Manipulação de Dados** | Pandas e NumPy | Simulação (ou carregamento) e tratamento dos dados. |
| **Empacotamento** | joblib | Salvar e carregar o modelo treinado. |

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação na sua máquina.

### 1. Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.8+ recomendada).

### 2. Instalação das Dependências

Crie um arquivo `requirements.txt` com as seguintes bibliotecas e instale-as:

```bash
# requirements.txt
pandas
numpy
scikit-learn
streamlit
joblib
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Execução da Aplicação

```bash
python -m streamlit run app_en.py
```

O aplicativo será aberto automaticamente no seu navegador, geralmente em http://localhost:8501.

## 📊 Estrutura e Data Science (O Processo)

O projeto demonstra as seguintes etapas de um **pipeline de Ciência de Dados**:

* **Aquisição de Dados:** Utiliza um dataset simulado (na versão inicial) com características-chave de imóveis (Área, Quartos, Distância).
* **Modelagem:** O modelo de **Regressão Linear** é treinado para entender o peso (coeficientes) de cada característica no preço final do imóvel.
* **Deploy:** O modelo treinado é carregado na aplicação **Streamlit**, permitindo a **inferência** em tempo real a partir da entrada do usuário.

### Exemplo de Previsão

Quando o usuário insere os dados, o modelo faz a previsão utilizando a equação:

$$
\text{Preço Estimado} = C_0 + C_1 \cdot (\text{Área}) + C_2 \cdot (\text{Quartos}) + C_3 \cdot (\text{Distância ao Centro})
$$

*Onde $C_n$ são os coeficientes (pesos) aprendidos pelo modelo durante o treinamento.*

---

## 🧑‍💻 Autor

Seu Nome
* [https://linkedin.com/in/edupadua/]



