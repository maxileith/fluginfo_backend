# this file contains custom errors of the
# amadeus connector

class AmadeusBadRequest(Exception):
    """
    Raised on bad request by the user.
    """


class AmadeusNothingFound(Exception):
    """
    Raised if nothing was found.
    """


class AmadeusServerError(Exception):
    """
    Amadeus experiences a server error.
    """
