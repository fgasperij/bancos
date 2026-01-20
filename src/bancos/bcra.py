"""Module to interact BCRA API."""

import httpx
import json


class BCRA:
    """Class to interact with the BCRA API."""

    def __init__(self):
        pass

    def debts(self, id: int) -> None:
        """Retrieve historical debts for a given ID from BCRA API."""
        response = httpx.get(
            f"https://api.bcra.gob.ar/centraldedeudores/v1.0/Deudas/Historicas/{id}"
        )

        if response.status_code == 200:
            print(f"Successfully retrieved debts for ID {id}")
            print(json.dumps(response.json(), indent=2))
        else:
            print(
                f"Failed to retrieve debts for ID {id}. Status Code: {response.status_code}"
            )
            print(f"Error Message: {response.text}")

        return None
