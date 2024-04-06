from ExpertSystem.api.esMenu import APP
from ExpertSystem.app.cinema.RuleBaseVehicle import RuleBaseVehicle

class Main:
    def __init__(self):
        self.app = APP("Rule Application")

    def main(self):
        try:
            # RuleBaseVehicle recebe dois parâmetros:
            # o primeiro é nome da base de regras e
            # o segundo é lista de variáveis presentes na base de regras.
            # Essas variáveis fazem parte dos possíveis objetivos.
            br_vehicle = RuleBaseVehicle("Categoria do veiculo",
                                      "[tipo_de_veiculo, numero_de_portas]:")
            self.app.add_rule_base(br_vehicle)
            self.app.menu()
        except Exception as e:
            print("Exception: RuleApp ", e)

if __name__ == '__main__':
    Main().main()