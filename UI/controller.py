from flet import ft
from UI.view import View
from model.model import Model
from UI.alert import AlertManager

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        soglia_txt = self._view.txt_soglia.value
        if soglia_txt is None or soglia_txt.strip() == "":
            AlertManager('Inserire un numero')
            return
        try:
            soglia = float(soglia_txt)
        except:
            AlertManager('La soglia deve essere un numero')
            return
        self._model.costruisci_grafo(soglia)
        num_hub = self._model.get_num_nodes()
        num_tratte = self._model.get_num_edges()
        edges = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()
        self._view.lista_visualizzazione.controls.append(ft.Text(f'Hub nel grafo: {num_hub}'))
        self._view.lista_visualizzazione.controls.append(ft.Text(f'Tratte con guadagno >= : {soglia}: {num_tratte}'))
        self._view.lista_visualizzazione.controls.append(ft.Text(f'Tratte valide:'))

        for u,v,peso in edges:
            self._view.lista_visualizzazione.controls.append(ft.Text(f'{u.nome} - {v.nome} (media:{peso:.2f} euro'))


