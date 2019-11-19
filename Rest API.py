import requests
import pytest
import json


def Synchronizations_list(authorized_user_headers):

    return requests.get(f"https://test.bimstreamer.com/backend/bim-server/rest/bim/synchronizations?")
    print(response)





