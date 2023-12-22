from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCA_AMORTECEDORES = "Troca de amortecedores", "Troca de amortecedores"
    TROCA_OLEO = "Troca de óleo", "Troca de óleo"
    TROCA_EMBREAGEM = "Troca de embreagem", "Troca de embreagem"
    TROCA_PNEU = "Troca de pneu", "Troca de pneu"