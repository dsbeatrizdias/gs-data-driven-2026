# 🛰️ Sistema de Monitoramento de Dados Espaciais

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte da avaliação **Global Solutions** da disciplina **Data Driven Application**, do curso de Data Science na FIAP.

O sistema simula um programa de monitoramento de eventos climáticos e ambientais (como queimadas, inundações e secas) detectados por satélites no território brasileiro. Os dados são coletados manualmente pelo usuário, validados em tempo real e, ao final, é gerado um **relatório de análise** completo com os principais indicadores dos eventos registrados.

---

## 🎯 Objetivo

Praticar os fundamentos da linguagem Python aplicados à análise de dados, utilizando exclusivamente:

- Estruturas condicionais (`if`, `else`)
- Laços de repetição (`for`, `while`)
- Listas nativas do Python (`list`)
- Funções nativas `max()` e `.index()`

> ⚠️ **Nenhuma biblioteca externa** (como Pandas) é utilizada neste projeto.

---

## 📊 O que o programa faz?

1. Solicita a quantidade de eventos a serem registrados
2. Coleta os dados de cada evento com **validação de entrada**:
   - A intensidade deve estar entre **1 e 10**
   - A área afetada deve ser **maior que zero**
3. Processa os dados e gera um relatório com:
   - Total de eventos registrados
   - Área total afetada (km²)
   - Média de intensidade
   - Região com maior número de ocorrências
   - Eventos acima da média de intensidade
   - Densidade média de ocorrências
   - Evento mais crítico (por intensidade e área)

---

## 🗂️ Estrutura do Projeto

```
📦 global-solutions/
├── 26.1.GS.<AnaJuliaBeatriz>.py   # Script principal
└── README.md                    # Este arquivo
```

---

## ▶️ Como rodar o script

### Pré-requisitos

- Ter o **Python 3** instalado na sua máquina.  
  Para verificar, abra o terminal e execute:
  ```bash
  python --version
  ```
  ou
  ```bash
  python3 --version
  ```

### Passo a passo

1. **Clone ou baixe** este repositório para sua máquina.

2. Abra o **terminal** (Prompt de Comando no Windows, Terminal no Mac/Linux).

3. Navegue até a pasta onde o arquivo foi salvo:
   ```bash
   cd caminho/para/a/pasta
   ```

4. Execute o script com o comando:
   ```bash
   python 26.1.GS.<AnaJuliaBeatriz>.py
   ```
   ou, dependendo da sua instalação:
   ```bash
   python3 26.1.GS.<AnaJuliaBeatriz>.py
   ```

5. Siga as instruções exibidas no terminal para inserir os dados dos eventos.

---

## 💡 Exemplo de Uso

```
=============================================
  SISTEMA DE MONITORAMENTO DE SATÉLITES
=============================================

Quantos eventos deseja registrar? 2

--- Evento 1 de 2 ---
Tipo do evento: Queimada
País: Brasil
Região: Norte
Cidade: Manaus
Número de ocorrências registradas: 5
Intensidade do evento (1 a 10): 8
Área afetada (em km², deve ser > 0): 1200.5
  ✅ Evento 1 registrado com sucesso!
```

---

## 👩‍💻 Tecnologias Utilizadas

| Tecnologia | Versão  |
|------------|---------|
| Python     | 3.x     |

---

