import os

from safeds.data.tabular.containers import Table

from safeds_examples.tabular import ExampleTable

_path = os.path.join(os.path.dirname(__file__), "data", "titanic.csv")


def load_titanic() -> ExampleTable:
    """
    Loads the "Titanic" dataset.

    Returns
    -------
    ExampleTable
        The "Titanic" dataset.
    """

    return ExampleTable(
        Table.from_csv_file(_path),
        column_descriptions={
            "id": "A unique identifier",
            "name": "Name of the passenger",
            "sex": "Sex of the passenger",
            "age": "Age of the passenger at the time of the accident",
            "siblings_spouses": "Number of siblings or spouses aboard",
            "parents_children": "Number of parents or children aboard",
            "ticket": "Ticket number",
            "travel_class": "Travel class (1 = first, 2 = second, 3 = third)",
            "fare": "Fare",
            "cabin": "Cabin number",
            "port_embarked": "Port of embarkation",
            "survived": "Whether the passenger survived the accident (0 = no, 1 = yes)",
        }
    )
