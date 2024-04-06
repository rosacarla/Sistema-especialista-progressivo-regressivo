# 🤖 Sistema Especialista Progressivo e Regressivo em Python  

Projeto contém versões de sistemas especialistas com encadeamento progressivo e regressivo, desenvolvido em Python como atividade avaliativa da disciplina Engenharia do Conhecimento do curso Tecnologia em Inteligência Artificial Aplicada da PUCPR.  
</br>

<p align='center'>
  <img src='https://github.com/rosacarla/Sistema-especialista-progressivo-regressivo/blob/main/images/sistema-especialista.jpeg' height=580 width=580>  
</p>  

_Crédito da imagem: gerada com IA Copilot_

---   
#### 🧠 SOBRE OS SISTEMAS ESPECIALISTAS  

<p align='justify'> São <b>sistemas de inteligência artificial</b> que tentam igualar-se ao raciocínio humano em um domínio específico de conhecimento. São construídos com uma base de conhecimento que contém uma série de regras de produção que representam o conhecimento especializado em um determinado domínio.</p>  

[[Continue lendo]](https://github.com/rosacarla/Sistema-especialista-progressivo-regressivo/blob/main/Sistema_Especialista_Progressivo_Regressivo.ipynb)

---  

#### 🧰 TECNOLOGIAS UTILIZADAS  
- Linguagem Python 3.10
- ChatGPT 3.4
- Copilot
- Google Colab
- IDE PyCharm 2023.3.8
- IDE VS Code 1.88.0
- Postimage

---  

#### 🚗 CLASSE RuleBaseVehicle.py DO SOFTWARE ExpertSystem V2
``` python
class RuleBaseVehicle:
    def __init__(self, nome, goals_list):
        self.br = BooleanRuleBase(nome)
        self.goals_list = goals_list

    def get_goal_list(self):
        return self.goals_list

    def create(self):

        veiculo = RuleVariable(self.br, "veiculo")
        veiculo.set_prompt_text("1. Que veículo é esse?")
        veiculo.set_labels("velocipede automotivo")

        tipo_de_veiculo = RuleVariable(self.br, "tipo_de_veiculo")
        tipo_de_veiculo.set_prompt_text("2. Que tipo de veículo é esse?")
        tipo_de_veiculo.set_labels("bicicleta triciclo motocicleta carroEsporte sedan minivan veiculoEsporteUtilitario")

```
[[Ver mais...]](https://github.com/rosacarla/Sistema-especialista-progressivo-regressivo/blob/main/ExpertSystem%20V2/ExpertSystem/ExpertSystem/app/cinema/RuleBaseVehicle.py) 

---   
#### ✍️ AUTORA  
Carla Edila Silveira  
Contato: rosa.carla@pucpr.edu.br  

---

#### ©️ LICENÇA

[MIT](https://choosealicense.com/licenses/mit/)  

---  
