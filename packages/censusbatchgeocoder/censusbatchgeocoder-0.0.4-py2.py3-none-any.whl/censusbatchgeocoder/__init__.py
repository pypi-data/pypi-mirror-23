#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io
import csv
import six
import logging
import requests
logger = logging.getLogger(__name__)


class Geocoder(object):
    """
    Wrapper on the Census Geocoding Services API batch service.
    """
    URL = 'https://geocoding.geo.census.gov/geocoder/geographies/addressbatch'
    RESULT_HEADER = [
        'id',
        'input_address',
        'is_match',
        'is_exact',
        'geocoded_address',
        'coordinates',
        'tiger_line',
        'side',
        'state_fips',
        'county_fips',
        'tract',
        'block'
    ]

    def __init__(
        self,
        benchmark='Public_AR_Current',
        vintage='Current_Current',
        return_type='locations',
    ):
        self.benchmark = benchmark
        self.vintage = vintage
        self.return_type = return_type

    def get_payload(self):
        """
        Returns the payload to include with the geocoder request.
        """
        return {
            'benchmark': self.benchmark,
            'vintage': self.vintage,
            'returntype': self.return_type
        }

    def get_response(self, address_file, file_type='text/csv'):
        """
        Returns the raw geocoder result for the provided address file.
        """
        files = {
            'addressFile': ('batch.csv', address_file, file_type)
        }
        logger.debug("Sending request")
        return requests.post(self.URL, files=files, data=self.get_payload())

    def get_chunks(self, l, n=1000):
        """
        Breaks up the provided list into chunks no bigger than 1,000 each.
        """
        # For item i in a range that is a length of l,
        for i in range(0, len(l), n):
            # Create an index range for l of n items:
            yield l[i:i+n]

    def geocode(self, string_or_stream, file_type='text/csv'):
        """
        Accepts a file object or path with a batch of addresses and attempts to geocode it.
        """
        # Depending on what kind of data has been submitted prepare the file object
        if hasattr(string_or_stream, 'read'):
            address_file = string_or_stream
        else:
            address_file = open(string_or_stream, 'r')

        # Read it in as a csv
        address_csv = list(csv.reader(address_file))

        # Break it into chunks
        address_chunks = list(self.get_chunks(address_csv))

        # Create the string we'll build on the fly as we hit the API and process responses
        response_file = io.StringIO()

        # Toss in the header
        response_file.write(",".join(self.RESULT_HEADER) + "\n")

        # Loop through the chunks and get results for them one at a time
        for chunk in address_chunks:
            # Convert the chunk into a file object again
            if six.PY3:
                chunk_file = io.StringIO()
            else:
                chunk_file = io.BytesIO()
            chunk_writer = csv.writer(chunk_file)
            chunk_writer.writerows(chunk)

            # Request batch from the API
            if six.PY3:
                request_file = io.StringIO(chunk_file.getvalue())
            else:
                request_file = io.BytesIO(chunk_file.getvalue())
            response = self.get_response(request_file, file_type=file_type)

            # Add the response to what we return
            response_file.write(response.text)

        # Parse the response file as a CSV
        csv_file = io.StringIO(response_file.getvalue())
        response_list = csv.DictReader(csv_file)

        # Pass it back
        return list(response_list)


def geocode(
    string_or_stream,
    benchmark='Public_AR_Current',
    vintage='Current_Current',
    return_type='locations',
):
    """
    Accepts a file object or path with a batch of addresses and attempts to geocode it.
    """
    obj = Geocoder(benchmark=benchmark, vintage=vintage, return_type=return_type)
    return obj.geocode(string_or_stream)
