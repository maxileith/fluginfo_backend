import json
from os import path
from copy import copy, deepcopy
from hashlib import sha512
from .errors import AmadeusNothingFound


class OfferCache:
    """
    Can be used to cache and retreive original amadeus offers.
    """

    def __init__(self, initial_state: dict = copy({}), debug: bool = False, debug_output_path: str = ""):
        """
        Initialize the offer cache.

        Args:
            self (object): Object itself
            initial_state (dict): Initial cache state. Defaults to {}
            debug (bool, optional): Write offer cache to json file for debugging. Defaults to False.
            debug_output_path (str, optional): Path of debugging file. Defaults to "".
        """
        self.__debug_output_path = debug_output_path
        self.__debug = debug

        # the dictionary where all added offers
        # are cached
        self.__offers = deepcopy(initial_state)

    def add(self, offers: list) -> list:
        """
        Cache original amadeus offers.

        Args:
            self (object): Object itself.
            offers (list): List of offers to cache.

        Returns:
            list: Hash values of the added offers to reference them.
        """

        # create list where the hash values of the
        # newly cached offers are stored
        hash_list = list()

        # add every new offer to the cache
        for offer in offers:
            # create a hash of the offer to reference it later
            as_string = json.dumps(offer, sort_keys=True)
            hash_value = sha512(as_string.encode('utf-8')).hexdigest()
            # add the offer to the cache
            self.__offers[hash_value] = offer
            # save hash value
            hash_list.append(hash_value)

        # write dict as json to file
        if self.__debug:
            json_path = path.join(
                self.__debug_output_path, 'offer_cache.json')
            with open(json_path, 'w+', encoding='utf-8') as f:
                json.dump(self.__offers, f, indent=4)

        # return the hash values of the newly cached offers
        return hash_list

    def get(self, hash_values: list, ignore_missing: bool = False) -> dict:
        """
        Get original amadeus offers.

        Args:
            self (object): Object itself.
            hash_values (list): The hash values that identify the desired offers.
            ignore_missing (bool, optional): Silence error on missing offer. Defaults to False.

        Raises:
            AmadeusNothingFound: At least one offer cannot be found. See arg ignore_missing to silence.

        Returns:
            dict: Original amadeus offers with hash values as keys.
        """

        # create the dict that is gonna be returned
        offers = dict()

        for h in hash_values:
            try:
                # load offer from cache and add to return list
                offers[h] = self.__offers[h]
            except KeyError as e:
                # skip raising an error if errors are unwanted
                if not ignore_missing:
                    # raise AmadeusNothingFound if there is no offer
                    # associated with the hash value in the cache
                    raise AmadeusNothingFound from e

        # return the desired offers
        return offers
