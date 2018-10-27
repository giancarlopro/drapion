import pytest
import responses

from drapion import DObject, Drapion


class TestDObject:

    @pytest.fixture
    def sample(self):
        return DObject(
            attributes={
                'name': 'John',
                'age': 20,
                'email': 'john@mail.com'
            },
            values=[
                0,
                1,
                2,
                3
            ]
        )

    def test_get_attr(self, sample):
        assert sample.name == 'John'
        assert sample.age == 20
        assert sample.email == 'john@mail.com'

        with pytest.raises(AttributeError):
            sample.username

    def test_get_item(self, sample):
        for i in range(4):
            assert sample[i] == i

        assert sample['name'] == 'John'
        assert sample['age'] == 20
        assert sample['email'] == 'john@mail.com'

        with pytest.raises(KeyError):
            sample['username']

    def test_iter(self, sample):
        list_ = ['John', 20, 'john@mail.com', 0, 1, 2, 3]
        output = [x for x in sample]

        assert output == list_


class TestDrapion:

    def test_get_attr(self):
        obj = Drapion('http://api.com/api/')

        assert obj.endpoint == 'http://api.com/api'
        assert obj.users.endpoint == 'http://api.com/api/users'

    @responses.activate
    def test_call(self):
        responses.add(
            responses.GET,
            'http://api.com/api/users',
            json=[
                {
                    'name': 'Roger',
                    'age': 20
                }, {
                    'name': 'Robert',
                    'age': 21
                }
            ],
            status=200
        )

        api = Drapion('http://api.com/api/')

        obj = api.users()

        assert obj[0].name == 'Roger'
        assert obj[1].name == 'Robert'
        assert obj[0].age == 20
        assert obj[1].age == 21
