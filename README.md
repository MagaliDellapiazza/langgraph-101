# LangGraph Email Agent — Implementación tutorial Real Python

Este proyecto es una implementación de ejemplo basada en el tutorial de Real Python  
👉 [“Build Stateful AI Agents in Python With LangGraph”](https://realpython.com/langgraph-python/#work-with-conditional-edges)

La idea principal fue aprender cómo construir **agentes de lenguaje con memoria y flujo lógico**, utilizando **LangGraph** para modelar decisiones condicionales y pasos secuenciales dentro de un proceso.

---

## Objetivo

El objetivo del proyecto construir un simulador de decisiones que **analiza correos electrónicos** (emails) relacionados con incidentes o notificaciones, y decide si deben escalar a un nivel superior o no.

Cada email pasa por un grafo de decisiones donde un agente (modelo de lenguaje)  
determina si el mensaje requiere **una acción específica**, como escalarlo o generar una respuesta.

Para lograrlo, se modela el flujo de decisiones como un grafo de estado (StateGraph) usando LangGraph, donde cada nodo representa una acción o un análisis, y las aristas (edges) determinan cómo continúa el proceso según los resultados.

Por ejemplo, un correo que menciona algo como “los trabajadores fueron vistos sin arnés de seguridad” activa un nodo que evalúa la situación y define la variable requires_escalation = True.
A partir de esa decisión, el grafo puede tomar distintos caminos:

- Si la respuesta es True, se crea o envía un ticket de escalación (por ejemplo, a un responsable de seguridad o a un área legal).

- Si la respuesta es False, el flujo continúa normalmente o se cierra el caso.

---

## ¿Qué es LangGraph?
**LangGraph** es una biblioteca de Python diseñada para construir flujos de trabajo y agentes de modelos de lenguaje (LLM) con **estado**, **ciclos** y **múltiples actores**.
Extiende las funcionalidades de su biblioteca principal, **LangChain**, para simplificar el desarrollo de **aplicaciones de LLM más sofisticadas**.

Permite crear flujos de trabajo (graphs) donde cada **nodo** representa una acción o un agente, y las **aristas** (edges) definen cómo fluye la información entre ellos.  

---

## ⚙️ Estructura general

El proyecto está organizado de la siguiente manera:

    ├── chains/
    │   ├── notice_extraction.py 
    │   ├── escalation_check.py
    │   └── binary_questions.py
    │
    ├── graphs/
    │   ├── notice_extraction.py
    │   ├── notice_extraction_conditional.py 
    │   ├── notice_extraction_binary.py 
    │   └── email_agent.py
    │
    ├── utils/
    │   ├── graph_utils.py
    │   └── logging_config.py
    │
    ├── photos/
    │   ├── notice_extraction_graph.png
    │   ├── binary_notice_extraction_graph.png
    │   └── conditional_notice_extraction_graph.png
    │
    ├── example_emails.py
    ├── (all tests ...)
    ├── pyproject.toml
    ├── poetry.lock
    ├── .venv/
    └── .env


Se desarrollaron varias versiones del grafo (`notice_extraction.py`, `notice_extraction_conditional.py`, `notice_extraction_binary.py`) con el objetivo de mantener versiones funcionales independientes.
Cada una representa una evolución de la anterior, incorporando nuevas características: primero un flujo lineal básico, luego decisiones binarias y finalmente condiciones más complejas y ramificadas.