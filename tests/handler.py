from database.realtime_handler import Handler
from database.account import Account

class TestHandler:

    def test_push_data(self):
        data = {'name': 'test', 'id': 123}
        child = 'Test'
        assert Handler.push_data(data, child)
        assert type(Handler.push_data(data, child)) == bool

    def test_set_data(self):
        data = {'name': 'test', 'id': 123}
        child = 'Test'
        assert Handler.set_data(data, data['name'], child)
        assert type(Handler.set_data(data, data['name'], child)) == bool

    def test_update_data(self):
        data = {'name': 'test', 'id': 123}
        child = 'Test'
        assert Handler.update_data(data, data['name'], child)
        assert type(Handler.update_data(data, data['name'], child)) == bool

    def test_delete_data(self):
        data = {'name': 'test', 'id': 123}
        child = 'Test'
        assert Handler.delete_data(data, child)
        assert type(Handler.delete_data(data, child)) == bool

    def test_get_data(self):
        child = 'Test'
        assert Handler.get_data(child) != None
        assert type(Handler.get_data(child)) == list





