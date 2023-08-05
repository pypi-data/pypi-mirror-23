from __future__ import absolute_import

try:
    # noinspection PyUnresolvedReferences
    from typing import Optional
except ImportError:
    pass

from datetime import datetime
from ...utilities import timezone


class ComparisonSide(object):
    def __init__(self, file_type, source_url, display_name):
        # type: (str, Optional[str], Optional[str]) -> None
        self.__file_type = file_type
        self.__source_url = source_url
        self.__display_name = display_name

    @property
    def file_type(self):
        # type: () -> str
        return self.__file_type

    @property
    def source_url(self):
        # type: () -> Optional[str]
        return self.__source_url

    @property
    def display_name(self):
        # type: () -> Optional[str]
        return self.__display_name

    def __str__(self):
        # type: () -> str
        return '{{file_type: {}{}{}}}'.format(
            repr(self.file_type),
            ', source_url: {}'.format(repr(self.source_url)) if self.source_url else '',
            ', display_name: {}'.format(repr(self.display_name)) if self.display_name else '',
        )

    def __repr__(self):
        # type: () -> str
        return 'ComparisonSide(file_type={}, source_url={}, display_name={})'.format(
            repr(self.file_type),
            repr(self.source_url),
            repr(self.display_name),
        )


class Comparison(object):
    def __init__(self,
                 identifier,     # type: str
                 left,           # type: ComparisonSide
                 right,          # type: ComparisonSide
                 public,         # type: bool
                 creation_time,  # type: datetime
                 expiry_time,    # type: Optional[datetime]
                 ready,          # type: bool
                 failed,         # type: Optional[bool]
                 error_message   # type: Optional[str]
                 ):
        self.__identifier = identifier
        self.__left = left
        self.__right = right
        self.__creation_time = creation_time
        self.__public = public
        self.__expiry_time = expiry_time
        self.__ready = ready
        self.__failed = failed
        self.__error_message = error_message

    @property
    def identifier(self):
        # type: () -> str
        return self.__identifier

    @property
    def left(self):
        # type: () -> ComparisonSide
        return self.__left

    @property
    def right(self):
        # type: () -> ComparisonSide
        return self.__right

    @property
    def public(self):
        # type: () -> bool
        return self.__public

    @property
    def creation_time(self):
        # type: () -> datetime
        return self.__creation_time

    @property
    def expiry_time(self):
        # type: () -> Optional[datetime]
        return self.__expiry_time

    @property
    def ready(self):
        # type: () -> bool
        return self.__ready

    @property
    def failed(self):
        # type: () -> Optional[bool]
        return self.__failed

    @property
    def error_message(self):
        # type: () -> Optional[str]
        return self.__error_message

    def __str__(self):
        # type: () -> str
        return 'Comparison(identifier={}, left={}, right={}, public={}, creation_time={}, expiry_time={}, ready={}, failed={}, error_message={})'.format(
            repr(self.identifier),
            str(self.left),
            str(self.right),
            str(self.public),
            self.creation_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
            self.expiry_time.strftime('%Y-%m-%dT%H:%M:%SZ') if self.expiry_time else None,
            str(self.ready),
            str(self.failed),
            '<{} chars>'.format(len(self.error_message)) if self.error_message is not None else None,
        )

    def __repr__(self):
        # type: () -> str
        return 'Comparison(identifier={}, left={}, right={}, public={}, creation_time={}, expiry_time={}, ready={}, failed={}, error_message={})'.format(
            repr(self.identifier),
            repr(self.left),
            repr(self.right),
            repr(self.public),
            repr(self.creation_time),
            repr(self.expiry_time),
            repr(self.ready),
            repr(self.failed),
            repr(self.error_message),
        )


def _parse_datetime(iso_format_string):
    # type: (str) -> datetime
    try:
        return datetime.strptime(iso_format_string, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
    except ValueError:
        # Sometimes the datetime can be missing the milliseconds, in which case the strptime call fails.
        return datetime.strptime(iso_format_string, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def _comparison_side_from_response(side_data):
    # type: (dict) -> ComparisonSide
    return ComparisonSide(file_type=str(side_data['file_type']), source_url=side_data.get('source_url'), display_name=side_data.get('display_name'))


def comparison_from_response(data):
    # type: (dict) -> Comparison
    return Comparison(
        identifier = str(data['identifier']),
        left = _comparison_side_from_response(data['left']),
        right = _comparison_side_from_response(data['right']),
        public = data.get('public', False),
        creation_time = _parse_datetime(data['creation_time']),
        expiry_time = _parse_datetime(data['expiry_time']) if 'expiry_time' in data else None,
        ready = data.get('ready'),
        failed = data.get('failed'),
        error_message = data.get('error_message'),
    )
