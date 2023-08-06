import requests
import json
import collections

from .error import DataError, DatabaseError, OperationalError, check_response


class Cursor(object):
    """Represent cursor object."""

    def __init__(self, conn, headers=None, payload_template=None):
        """

        Args:
            conn (Connection): Connection object.
            headers (dict): Headers for request.
            payload_template (dict): Payload template.
        """
        self.description = tuple()
        """tuple: This read-only attribute is a sequence of 7-item sequences.
        Each of these sequences contains information describing one result column.
        We do not have any information about structure of json rpc result.
        So simple empty tuple.
        """
        self.rowcount = -1
        """int: This read-only attribute specifies the number of rows that the last .execute*()
         produced (for DQL statements like SELECT ) or affected (for DML statements like UPDATE or INSERT )."""
        self.arraysize = 1
        self._data = None
        self._pos = 0
        self.conn = conn
        """Connection: Read-only, reference to connection object."""
        self.auth = conn.auth
        if not headers:
            headers = {'content-type': 'application/json'}
        self.headers = headers
        if not payload_template:
            payload_template = self._get_payload_template()
        self.payload_template = payload_template

    def close(self):
        """Do not support, this method with void functionality."""
        pass

    def execute(self, operation, *args):
        """Execute remote procedure.

        Possible types of result returned by request (s - mean scalar):
            * s
            * [s, s, ..., s]
            * dict
            * [different types]
        Args:
            operation (str): Remote method.
            *args: Used only first argument, it should be dict with 'params' key.
        """
        self.rowcount = -1
        self._data = None
        self._pos = 0
        if len(args) == 0:
            params = {
                'params': None
            }
        else:
            params = args[0]
        payload = self.payload_template.copy()
        payload['method'] = operation
        payload.update(params)
        url = self.conn.get_url()
        response = requests.post(url,
                                 json.dumps(payload),
                                 headers=self.headers,
                                 auth=self.auth)
        try:
            response = response.json()
            check_response(response)
            self._save_data(response)
            self._update_rowcount(response)
        except ValueError as e:
            raise OperationalError()

    def executemany(self, operation, *args):
        # TODO realize method.
        pass

    def fetchone(self):
        """Fetch the next row of a query result set, returning a single sequence,
        or None when no more data is available.
        """
        try:
            result = self._data[self._pos]
            self._pos += 1
            return result
        except IndexError:
            return None

    def fetchmany(self, size=None):
        # TODO realize method
        if not size:
            size = self.arraysize
        return None

    def fetchall(self):
        """Fetch all (remaining) rows of a query result,
        returning them as a sequence of sequences (e.g. a list of tuples)."""
        return self._data

    def _update_rowcount(self, data):
        """Update rowcount.

        Simple save len of transformed data.
        """
        if self._data:
            self.rowcount = len(self._data) + 1
        else:
            self.rowcount = 0

    def _save_data(self, data):
        """Get result of response.

        Transform result and save it in _data attribute.
        Args:
            data (dict): Json response.

        """
        result = data['result']
        self._data = self._prepare_all_result(result)

    @staticmethod
    def _get_payload_template(params=None):
        """Construct payload template.

        Args:
            params: Additional params.

        Returns:
            dict: Return payload dict.
        """
        if not params:
            params = {}
        payload_template = {
            "method": "",
            "params": params,
            "jsonrpc": "2.0",
            "id": 0,
        }
        return payload_template

    def _prepare_all_result(self, data):
        """

        Returns:
            * data = [] -> []
            * data = s -> [(s,)]
            * data = str -> [(str, )]
            * data = dict -> [dict]
            * data = [s, s, ..., s] -> [(s, ), (s, ), ... (s, )]
            * data = [str, ...] -> [(str, ), ... ]
            * data = [array, ...] -> [tuple(array), ...]
            * data = [dict, ...] -> [dict, ...]
            * data = [[], ...] -> []
        """
        if not data:
            return []  # data = [] -> []
        if isinstance(data, str):
            return [(data,)]  # data = str -> [(str, )]
        if isinstance(data, collections.Mapping):
            return [data]  # data = dict -> [dict]
        try:
            one = data[0]
        except TypeError:
            return [(data,)]  # data = s -> [(s,)]
        except IndexError:
            return []
        # multiply results in array
        if isinstance(one, collections.Mapping):
            return data  # data = [dict, ...] -> [dict, ...]
        elif isinstance(one, str):
            return [(el,) for el in data]  # data = [str, ...] -> [(str, ), ... ]
        else:
            try:
                probe = one[0]
            except TypeError:
                return [(el,) for el in data]  # data = [s, s, ..., s] -> [(s, ), (s, ), ... (s, )]
            except IndexError:
                return []
        return [tuple(el) for el in data]
