import unittest
from kafka_influxdb.encoder import graphite_encoder
from kafka_influxdb.template import graphite


class TestGraphiteEncoder(unittest.TestCase):

    def setUp(self):
        self.encoder = self.create_encoder()

    @staticmethod
    def create_encoder(templates=None):
        return graphite_encoder.Encoder(templates)

    def test_encode_simple(self):
        self.encoder = self.create_encoder(graphite.Template([]))
        msg = b'myhost.load.load.shortterm 0.05 1436357630'
        expected = ['myhost_load_load_shortterm value=0.05 1436357630']
        self.assertEqual(self.encoder.encode(msg), expected)

    @unittest.skip("prefixes no longer supported")
    def test_encode_with_prefix(self):
        msg = b'mydatacenter.myhost.load.load.shortterm 0.45 1436357630'

        # The official documentation states that tags should be sorted for performance reasons.
        # As of now they will be sorted on the InfluxDB side anyway (which is probably faster).
        # (See https://influxdb.com/docs/v0.9/write_protocols/line.html#key for more info)
        # So we don't sort the tags to make the encoder faster.
        # As a consequence they can appear in any order. Test for all combinations.
        expected1 = ['load_load_shortterm,datacenter=mydatacenter,host=myhost value=0.45 1436357630']
        expected2 = ['load_load_shortterm,host=myhost,datacenter=mydatacenter value=0.45 1436357630']

        if self.encoder.encode(msg, prefix="mydatacenter.", prefix_tag="datacenter") == expected1:
            return
        if self.encoder.encode(msg, prefix="mydatacenter.", prefix_tag="datacenter") == expected2:
            return
        raise self.failureException()

    def test_encode_multiple_values(self):
        msg = b'26f2fc918f50.load.load.shortterm 0.05 1436357630\n' \
              b'26f2fc918f50.load.load.midterm 0.06 1436357631\n' \
              b'26f2fc918f50.load.load.longterm 0.07 1436357632'
        expected = [
            'load_load_shortterm,host=26f2fc918f50 value=0.05 1436357630',
            'load_load_midterm,host=26f2fc918f50 value=0.06 1436357631',
            'load_load_longterm,host=26f2fc918f50 value=0.07 1436357632',
        ]
        self.assertEqual(self.encoder.encode(msg), expected)

    @unittest.skip("invalid_messages to implement later")
    def test_invalid_messages(self):
        invalid_messages = [b'', b'\n', b'bla', b'foo\nbar\nbaz']
        for msg in invalid_messages:
            self.assertEqual(self.encoder.encode(msg, prefix="mydatacenter.", prefix_tag="datacenter"), [])
