# Copyright 2017 QuantRocket - All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from quantrocket.houston import houston
from quantrocket.cli.utils.output import json_to_cli

def _load_or_show_crontab(service, filename=None):
    if filename:
        return load_crontab(service, filename)
    else:
        return get_crontab(service)

def get_crontab(service):
    """
    Returns the current crontab.

    Parameters
    ----------
    service : str, required
        the name of the service, e.g. ``countdown-usa``

    Returns
    -------
    str
        string representation of crontab
    """
    response = houston.get("/{0}/crontab".format(service))
    response.raise_for_status()
    return response.text

def load_crontab(service, filename):
    """
    Uploads a new crontab.

    Parameters
    ----------
    service : str, required
        the name of the service, e.g. ``countdown-usa``
    filename : str, required
        the crontab file to upload to the countdown service

    Returns
    -------
    dict
        status message
    """
    with open(filename) as file:
        response = houston.put("/{0}/crontab".format(service), data=file.read())
    return houston.json_if_possible(response)

def get_timezone(service):
    """
    Returns the service timezone.

    Parameters
    ----------
    service : str, required
        the name of the service, e.g. ``countdown-usa``

    Returns
    -------
    dict
        dict with key timezone
    """
    response = houston.get("/{0}/timezone".format(service))
    return houston.json_if_possible(response)

def _cli_get_timezone(*args, **kwargs):
    return json_to_cli(get_timezone, *args, **kwargs)
