from oappend import OverrideAppendArgumentParser


class OAppendTests:
    def test_default(self):
        parser = OverrideAppendArgumentParser()
        parser.add_argument('-n', action='oappend', default=['a', 'b'])
        args = parser.parse_args([])
        assert args.n == ['a', 'b']

    def test_append(self):
        parser = OverrideAppendArgumentParser()
        parser.add_argument('-n', action='oappend', default=['a', 'b'])
        args = parser.parse_args(['-nc', '-nd'])
        assert args.n == ['c', 'd']

    def test_type(self):
        parser = OverrideAppendArgumentParser()
        parser.add_argument('-n', action='oappend', type=int, default=[1, 2])
        args = parser.parse_args(['-n3', '-n4'])
        assert args.n == [3, 4]
