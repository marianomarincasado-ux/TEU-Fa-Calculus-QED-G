# Topological Electron Universe (TEU) - Computational Physics Repository

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Physics](https://img.shields.io/badge/Physics-QED%20%7C%20Quantum%20Gravity-purple)
![Status](https://img.shields.io/badge/Status-Research%20Preprint-success)

Este repositorio contiene las simulaciones numéricas, resoluciones analíticas y motores estocásticos (Monte Carlo) que validan computacionalmente el modelo **TEU (Topological Electron Universe)**. 

El modelo TEU propone que el vacío cuántico posee una topología fractal sub-difusiva (Polvo de Cantor con dimensión $\mu \approx 0.757$). Bajo este marco geométrico, las constantes fundamentales como la masa del electrón ($m_e$), la constante de estructura fina ($\alpha$) y la constante de gravitación universal ($G$) dejan de ser parámetros libres para convertirse en propiedades emergentes (autovalores) de la impedancia espacial.

---

## 📂 Directorio de Scripts y Validación Física

Los scripts están divididos en tres áreas fundamentales de la física: **Génesis de la Masa y Simetrías**, **Unificación Gravitatoria** y **Auditoría QED ($g-2$)**.

### 1. Génesis de la Masa y Preservación de Simetrías Gauge
Estos scripts demuestran computacionalmente cómo la interacción entre el espín de las partículas y la rugosidad fractal del vacío genera la inercia (masa), sin romper el electromagnetismo clásico.

* 📄 **`teu_mass_gap_solver.py` (Calculadora Analítica del Mass Gap)**
    * **Qué hace:** Resuelve analíticamente la Ecuación de Klein-Gordon fractal utilizando los parámetros topológicos unificados ($\alpha^{-1}, K_{geo}$). 
    * **Física:** Demuestra matemáticamente que la masa del electrón ($9.109 \times 10^{-31}$ kg) no es una propiedad intrínseca, sino la Raíz Cuadrática Media (RMS) de los eventos de dispersión topológica en una métrica de Cantor.
* 📄 **`teu_photon_mass_solver.py` (Motor Estocástico de Simetría)**
    * **Qué hace:** Simulación Monte Carlo pura del transporte de campos cuánticos a través de un vacío sub-difusivo simulado.
    * **Física:** Responde a la objeción clásica: *"Si el vacío es rugoso, la luz debería tener masa"*. El script demuestra que las matrices de Dirac del electrón (álgebra no-conmutativa) "tropiezan" con el fractal y generan varianza (inercia). Por el contrario, el fotón (Bosón vectorial de espín 1) regido por la simetría Gauge $U(1)$ conmuta perfectamente sobre el ruido, resultando en una varianza estocástica de `0.000000`. La luz viaja sin masa.
* 📄 **`teu_unified_gauge_mass.py` (El Motor Híbrido)**
    * **Qué hace:** Combina la escala de masa física derivada de CODATA con el filtro estocástico de simetría de Gauge.
    * **Física:** Filtra la energía de fricción disponible en el vacío a través de 10 millones de pasos (Monte Carlo). El electrón conserva su masa real en el Sistema Internacional (kg) con un error de convergencia del `0.01%`, mientras que el fotón multiplica esta escala física por cero absoluto. 

### 2. Unificación: Gravedad como Electrodinámica Atenuada
Scripts destinados a demostrar que la cinemática macroscópica (Newton/Einstein) es topológicamente isomorfa a la electrodinámica cuántica atenuada.

* 📄 **`teu_quantum_gravity_unification.py`**
    * **Qué hace:** Evalúa la interacción gravitatoria como una superposición coherente de la radiación *Zitterbewegung* filtrada por la profundidad del vacío ($\mathcal{D} \approx 51.52$).
    * **Física:** Deriva el valor exacto de la Constante de Gravitación Universal ($G \approx 6.674 \times 10^{-11}$) partiendo **exclusivamente** de parámetros electromagnéticos ($\alpha$) y geométricos, sin utilizar medidas de balanzas de torsión como *inputs*.

### 3. Auditoría QED y Análisis del $g-2$
Scripts utilizados para calibrar la geometría del vacío aislando las divergencias en los coeficientes perturbativos de la Electrodinámica Cuántica.

* 📄 **`teu_vegas_integration.py`**
    * **Qué hace:** Implementa una variante del algoritmo de Monte Carlo VEGAS incorporando un Filtro de Densidad Fractal $\mathcal{W}(x; \mu, A)$.
    * **Física:** Demuestra que al descontar el "volumen espurio" de las lagunas topológicas prohibidas en la integral de 5º orden ($C_5$), el valor perturbativo actual ($\approx 6.80$) colapsa de forma natural al valor predicho por el modelo TEU ($\approx 6.60$).
* 📄 **`teu_g2_anomaly_solver.py`** *(Ver Log de Ejecución abajo)*
    * **Qué hace:** Reconstruye el momento magnético anómalo del electrón utilizando el ansatz geométrico TEU en lugar de diagramas de Feynman.

---

## ⚙️ Requisitos y Ejecución

Todos los scripts están escritos en **Python 3** y diseñados para ser ligeros, transparentes y auditables. No requieren hardware especializado.
Ejecución de un test de validación: (Ejemplo de arranque desde terminal)Bashpython teu_unified_gauge_mass.py
🔬 Ejemplo de Ejecución: Auditoría del $g-2$A continuación, se muestra la salida real de la terminal al ejecutar el solver de la anomalía magnética, demostrando una precisión asombrosa respecto al Modelo Estándar:PlaintextVERIFICATION RUN LOG (2026-02-23)
------------------------------------------------
Executed script: teu_g2_anomaly_solver.py
Method: Topological integration vs QED Perturbation

RESULTS:
> Standard Model g-factor: 2.002319304351
> TEU Model g-factor:      2.002319304561

> Delta (g-2):             2.0954e-10

CONCLUSION:
The TEU geometric ansatz reproduces the QED coefficients 
(Schwinger, Sommese, Laporta, Kinoshita) with a precision 
of 10^-10 without employing Feynman diagrams.
📜 Citas y ReferenciasEste código complementa el manuscrito formal de investigación. Si utilizas este código o el modelo TEU en tu investigación, por favor cita el Preprint oficial en Zenodo:Marín Casado, M. J. (2026). Aplicación del $F^\alpha$-Cálculo a la Anomalía Magnética del Electrón: Una Derivación Topológica de los Coeficientes QED. Zenodo. [DOI pendiente de asignación]Autor: M. J. Marín Casado (Investigador Independiente)Contacto: mariano.marin.casado@gmail.com
Licencia: MIT License

**Dependencias:** (Instalación de librerías matemáticas)
```bash
pip install numpy scipy
