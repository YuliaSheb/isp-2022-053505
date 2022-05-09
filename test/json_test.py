import unittest
from test_data import *
from serializer.provider import Provider


class JsonTestCase(unittest.TestCase):
    def setUp(self):
        self.serializer = Provider.create_serializer('JSON')

    def tearDown(self):
        pass

    def test_int(self):
        x = None
        with open("test.json", "w") as fl:
            self.serializer.dump(int_data, fl)
        with open("test.json", "r") as fl:
            x = self.serializer.load(fl)
        assert x == int_data

    def test_int_s(self):
        x = self.serializer.dumps(int_data)
        res_data = self.serializer.loads(x)
        assert res_data == int_data

    def test_float(self):
        x = None
        with open("test.json", "w") as fl:
            self.serializer.dump(float_data, fl)
        with open("test.json", "r") as fl:
            x = self.serializer.load(fl)
        assert x == float_data

    def test_float_s(self):
        x = self.serializer.dumps(float_data)
        res_data = self.serializer.loads(x)
        assert res_data == float_data

    def test_bool(self):
        x = None
        with open("test.json", "w") as fl:
            self.serializer.dump(bool_data, fl)
        with open("test.json", "r") as fl:
            x = self.serializer.load(fl)
        assert x == bool_data

    def test_bool_s(self):
        x = self.serializer.dumps(bool_data)
        res_data = self.serializer.loads(x)
        assert res_data == bool_data

    def test_str(self):
        x = None
        with open("test.json", "w") as fl:
            self.serializer.dump(str_data, fl)
        with open("test.json", "r") as fl:
            x = self.serializer.load(fl)
        assert x == str_data

    def test_str_s(self):
        x = self.serializer.dumps(str_data)
        res_data = self.serializer.loads(x)
        assert res_data == str_data

    def test_simple_list(self):
        x = None
        with open("test.json", "w") as fl:
            self.serializer.dump(list_data, fl)
        with open("test.json", "r") as fl:
            x = self.serializer.load(fl)
        assert x == list_data

    def test_simple_list_s(self):
        x = self.serializer.dumps(list_data)
        res_data = self.serializer.loads(x)
        assert res_data == list_data

    def test_tuple_s(self):
        x = self.serializer.dumps(tuple_data)
        res_data = self.serializer.loads(x)
        assert res_data == tuple_data

    def test_complex_list(self):
        x = None
        with open("test.json", "w") as fl:
            self.serializer.dump(complex_list_data, fl)
        with open("test.json", "r") as fl:
            x = self.serializer.load(fl)
        assert x == complex_list_data

    def test_complex_list_s(self):
        x = self.serializer.dumps(complex_list_data)
        res_data = self.serializer.loads(x)
        assert res_data == complex_list_data

    def test_simple_dict(self):
        x = None
        with open("test.json", "w") as fl:
            self.serializer.dump(dict_data, fl)
        with open("test.json", "r") as fl:
            x = self.serializer.load(fl)
        assert x == dict_data

    def test_simple_dict_s(self):
        x = self.serializer.dumps(dict_data)
        res_data = self.serializer.loads(x)
        assert res_data == dict_data

    def test_complex_dict(self):
        x = None
        with open("test.json", "w") as fl:
            self.serializer.dump(complex_dict_data, fl)
        with open("test.json", "r") as fl:
            x = self.serializer.load(fl)
        assert x == complex_dict_data

    def test_complex_dict_s(self):
        x = self.serializer.dumps(complex_dict_data)
        res_data = self.serializer.loads(x)
        assert res_data == complex_dict_data

    def test_function(self):
        x = None
        with open("test.json", "w") as fl:
            self.serializer.dump(myprint, fl)
        with open("test.json", "r") as fl:
            x = self.serializer.load(fl)
        assert x(5) == myprint(5)
        assert type(x) == type(myprint)

    def test_function_s(self):
        x = self.serializer.dumps(myprint)
        res_data = self.serializer.loads(x)
        assert res_data(5) == myprint(5)
        assert type(res_data) == type(myprint)

    def test_type(self):
        x = None
        with open("test.json", "w") as fl:
            self.serializer.dump(Person, fl)
        with open("test.json", "r") as fl:
            x = self.serializer.load(fl)
        assert type(x) == type(Person)

    def test_type_s(self):
        x = self.serializer.dumps(Person)
        res_data = self.serializer.loads(x)
        assert type(res_data) == type(Person)

    def test_obj(self):
        x = None
        with open("test.json", "w") as fl:
            self.serializer.dump(person, fl)
        with open("test.json", "r") as fl:
            x = self.serializer.load(fl)
        assert x.say_hello() == person.say_hello()

    def test_obj_s(self):
        x = self.serializer.dumps(person)
        res_data = self.serializer.loads(x)
        assert res_data.say_hello() == person.say_hello()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(JsonTestCase))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')