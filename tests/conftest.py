import collections.abc
import inspect
import os
import pytest
import sys
import urllib.parse
import vcr
import vcr.filters

test_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
test_data_dir = os.path.join(test_dir, 'cassettes')

import pocketcasts



vcr.default_vcr = vcr.VCR(
    cassette_library_dir=test_data_dir,
    path_transformer=vcr.VCR.ensure_suffix('.yaml'),
    record_mode='once',
)
vcr.use_cassette = vcr.default_vcr.use_cassette


DEFAULT_USERNAME = 'REDACTED@USERNAME.COM'
DEFAULT_PASSWORD = 'REDACTED_PASSWORD'
USERNAME = os.environ.get('POCKETCAST_USERNAME', DEFAULT_USERNAME)
PASSWORD = os.environ.get('POCKETCAST_PASSWORD', DEFAULT_PASSWORD)

@pytest.fixture(scope='function')
def pocket_instance():
    return pocketcasts.Pocketcasts(USERNAME, PASSWORD)

def redacted_tuples(key, clean_value, dirty_values=None):
    if dirty_values is not None:
        if isinstance(dirty_values, str) or not isinstance(dirty_values, collections.abc.Container):
            dirty_values = {dirty_values}
    # Redact plaintext and url encoded versions of the keys and values
    for transform in [
        lambda x: x,
        urllib.parse.quote_plus,
    ]:
        def matcher(key, value, request):
            if dirty_values is None or value in [transform(v) for v in dirty_values]:
                return clean_value
            return value
        yield (transform(key), matcher)

# Can almost use filter_post_data_parameters except for this bug:
# https://github.com/kevin1024/vcrpy/issues/362
def manual_filter_post_data_parameters(request):
    if request.method == 'POST' and request.body is not None:
        return vcr.filters.replace_post_data_parameters(request, [
            *redacted_tuples('[user]email', DEFAULT_USERNAME, USERNAME),
            *redacted_tuples('[user]password', DEFAULT_PASSWORD, PASSWORD),
        ])
    return request

@pytest.fixture(scope='function', autouse=True)
def autouse_vcr_cassette(request):
    with vcr.use_cassette(**{
        'path': request.function.__name__,
        'before_record_request': manual_filter_post_data_parameters,
    }):
        yield
