from ExpertSystem.api.esBooleanRuleBase import BooleanRuleBase
from ExpertSystem.api.esRuleVariable import RuleVariable
from ExpertSystem.api.esCondition import Condition
from ExpertSystem.api.esRule import Rule
from ExpertSystem.api.esClause import Clause

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

        tamanho = RuleVariable(self.br, "tamanho")
        tamanho.set_prompt_text("3. Qual o tamanho do veículo?")
        tamanho.set_labels("pequeno médio grande")

        motor = RuleVariable(self.br, "motor")
        motor.set_prompt_text("4. O veículo tem um motor? (sim/não)")
        motor.set_labels("sim não")

        numero_de_rodas = RuleVariable(self.br, "numero_de_rodas")
        numero_de_rodas.set_prompt_text("5. Quantas rodas o veículo possui?")
        numero_de_rodas.set_labels("2 3 4")

        numero_de_portas = RuleVariable(self.br, "numero_de_portas")
        numero_de_portas.set_prompt_text("6. Quantas portas o veículo tem?")
        numero_de_portas.set_labels("2 3 4")

        c_equals = Condition("=")
        c_more_than = Condition(">")
        c_less_than = Condition("<")

        regra01 = Rule(self.br, "Regra 01",
                       [Clause(numero_de_rodas, c_less_than, "4")],
                       Clause(veiculo, c_equals, "velocipede"))

        regra02 = Rule(self.br, "Regra 02",
                       [Clause(numero_de_rodas, c_equals, "4"),
                        Clause(motor, c_equals, "sim")],
                       Clause(veiculo, c_equals, "automotivo"))

        regra03 = Rule(self.br, "Regra 03",
                       [Clause(veiculo, c_equals, "velocipede"),
                        Clause(numero_de_rodas, c_equals, "2"),
                        Clause(motor,c_equals, "nao")],
                       Clause(tipo_de_veiculo, c_equals, "bicicleta"))

        regra04 = Rule(self.br, "Regra 04",
                       [Clause(veiculo, c_equals, "velocipede"),
                        Clause(numero_de_rodas, c_equals, "3"),
                        Clause(motor, c_equals, "nao")],
                       Clause(tipo_de_veiculo, c_equals, "triciclo"))

        regra05 = Rule(self.br, "Regra 05",
                       [Clause(veiculo, c_equals, "velocipede"),
                        Clause(numero_de_rodas, c_equals, "2"),
                        Clause(motor, c_equals, "sim")],
                       Clause(tipo_de_veiculo, c_equals, "motocicleta"))

        regra06 = Rule(self.br, "Regra 06",
                       [Clause(veiculo, c_equals, "automotivo"),
                        Clause(tamanho,c_equals, "medio"),
                        Clause(numero_de_portas, c_equals, "2")],
                       Clause(tipo_de_veiculo, c_equals, "carroEsporte"))

        regra07 = Rule(self.br, "Regra 07",
                       [Clause(veiculo, c_equals, "automotivo"),
                        Clause(tamanho, c_equals, "medio"),
                        Clause(numero_de_portas, c_equals, "4")],
                       Clause(tipo_de_veiculo, c_equals, "sedan"))

        regra08 = Rule(self.br, "Regra 08",
                       [Clause(veiculo, c_equals, "automotivo"),
                        Clause(tamanho, c_equals, "medio"),
                        Clause(numero_de_portas, c_equals, "3")],
                       Clause(tipo_de_veiculo, c_equals, "minivan"))

        regra09 = Rule(self.br, "Regra 09",
                       [Clause(veiculo, c_equals, "automotivo"),
                        Clause(tamanho, c_equals, "grande"),
                        Clause(numero_de_portas, c_equals, "4")],
                       Clause(tipo_de_veiculo, c_equals, "veiculoEsporteUtilitario"))

        return self.br

    def demo_fc(self, LOG):
        LOG.append(
            " --- Ajustando valores para Transporte para demo ForwardChain ---")
        self.br.set_variable_value("veiculo", None)
        self.br.set_variable_value("tipo_de_veiculo", None)
        self.br.set_variable_value("tamanho", "grande")
        self.br.set_variable_value("numero_de_rodas", 4)
        self.br.set_variable_value("numero_de_portas", 4)
        self.br.set_variable_value("motor", "sim")
        self.br.display_variables(LOG)

    def demo_bc(self, LOG):
        LOG.append(
            " --- Ajustando valores para Transporte para demo BackwardChain ---")
        self.br.set_variable_value("veiculo", None)
        self.br.set_variable_value("tipo_de_veiculo", None)
        self.br.set_variable_value("tamanho", None)
        self.br.set_variable_value("numero_de_rodas", None)
        self.br.set_variable_value("numero_de_portas", None)
        self.br.set_variable_value("motor", "sim")
        self.br.display_variables(LOG)