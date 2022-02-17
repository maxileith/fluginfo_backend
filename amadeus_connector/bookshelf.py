from os import path
from copy import copy
import json
from .errors import AmadeusNothingFound


class Bookshelf:
    """
    The bookshelf is used to cache various dictionaries from amadeus responses and make them available for retrieval.
    """

    def __init__(self: object, initial_dictionaries: dict = copy({}), debug: bool = False, debug_output_path: str = "") -> object:
        """
        Create a new bookshelf with optional initial dictionaries.

        Args:
            self (object): Object itself.
            initial_dictionaries (dict, optional): Dictionaries that should be available right from the initialization to query. Defaults to dict().
            debug (bool, optional): Write bookshelf to json file for debugging. Defaults to False.
            debug_output_path (str, optional): Path of debugging file. Defaults to "".

        Returns:
            object: Bookshelf.
        """
        self.__dictionaries = initial_dictionaries
        self.__debug_output_path = debug_output_path
        self.__debug = debug

    def add(self: object, **dictionaries: dict):
        """
        Puts dictionaries on the bookshelf.
        Duplicate dictionaries or elements are merged.

        Args:
            self (object): Object itself.
            **dictionaries (dict): A dictionary of the dictionaries that are being put onto the shelf.

        Example of dictionaries arg:
            {
                'aircraft': {
                    'E75': 'EMBRAER 175',
                    '333': 'AIRBUS A330-300',
                    '788': 'BOEING 787-8',
                    '77W': 'BOEING 777-300ER'
                },
                'carriers': {
                    'AA': 'AMERICAN AIRLINES',
                    'AC': 'AIR CANADA',
                    'AY': 'FINNAIR',
                    'LH': 'LUFTHANSA',
                    'UA': 'UNITED AIRLINES'
                }
            }
        """

        # the examples in the comments are based of the example in the
        # docstring

        # iterate through all dictionaries given in the args
        # in our example: aircraft, carriers
        for t in dictionaries.keys():
            if t in self.__dictionaries.keys():
                # If a dictionary to be added has a key that already
                # exists in the bookshelf, merge the new one with the
                # existing one.
                self.__dictionaries[t] = {
                    **dictionaries[t], **self.__dictionaries[t]}
            else:
                # otherwise just add the dictionary
                self.__dictionaries[t] = dictionaries[t]

        # write dict as json to file if in debug mode
        if self.__debug:
            json_path = path.join(
                self.__debug_output_path, 'bookshelf.json')
            with open(json_path, 'w+', encoding='utf-8') as f:
                json.dump(self.__dictionaries, f, indent=4)

    def get(self: object, dict_type: str, item_id: str) -> dict:
        """
        Get an item of a dictionary in the bookshelf.

        Args:
            self (object): Object itself.
            dict_type (str): Identifier of the dictionary to look into.
            item_id (str): Identifier of the item in the dictionary.

        Raises:
            AmadeusNothingFound: The item cannot be found on the bookshelf.

        Returns:
            dict: The desired item.
        """
        try:
            # look for the item and return
            return self.__dictionaries[dict_type][item_id]
        except KeyError as e:
            # raise if error if at least one of the keys does not exist.
            raise AmadeusNothingFound from e
