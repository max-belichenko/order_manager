class OrderManager:
    """
    Class OrderManager manages ordered sequence of hashable values.

    When an object of OrderManager is initialized, and empty dict() is created to store values in following format:
        {'key': int(index)}
        where 'key' is a hashable object and index is an integer that represents position of this object in sequence.
        All keys are unique. Indexes are start with 0 and change consistantly through the sequence.

    For example:
        <self.sequence>:
        {
            'a': 0,
            'b': 1,
            'c': 2,
            'x': 3,
            'f': 4,
        }
    """
    def __init__(self):
        self.sequence = dict()

    def add_key(self, key):
        """
        Add a key to the end of sequence.
        Do nothing if key is already in sequence.
        """
        if key not in self.sequence:
            self.sequence[key] = len(self)

    def get_key_by_index(self, index):
        key = [_ for _ in self.sequence if self.sequence[_] == index]
        if not key:
            return None
        else:
            return key[0]

    def change_key_index(self, index_from, index_to):
        """
        Move item from index_from to index_to position.
        index_to == 0: move item to the beginning.
        index_to == -1: move item to the end.
        """
        if index_from == -1:
            index_from = len(self) - 1
        if index_to == -1:
            index_to = len(self) - 1

        if (index_from == index_to or
                index_from < 0 or
                index_to < 0 or
                index_from >= len(self) or
                index_to >= len(self)):
            return

        key_to_move = self.get_key_by_index(index_from)
        if not key_to_move:
            return

        self.sequence.pop(key_to_move)
        self.sequence.update({key_to_move: index_to})
        for key in self.sequence:
            index = self.sequence[key]
            if index_from > index_to:
                if index_from > index >= index_to and key != key_to_move:
                    self.sequence[key] += 1
            elif index_from < index_to:
                if index_from < index <= index_to and key != key_to_move:
                    self.sequence[key] -= 1

    def delete_key(self, key):
        """
        Delete key from sequence.
        Change all indexes above removed key to keep index consistency.
        """
        index = self.sequence.pop(key)
        for k in self.sequence:
            if self.sequence[k] > index:
                self.sequence[k] -= 1

    def __str__(self):
        sequence_sorted = sorted(self.sequence.items(), key=lambda x: x[1])

        string = '<object of Order Manager>:\n'
        for key, index in sequence_sorted:
            string += f'{index:<5}{key}\n'
        return string

    def __iter__(self):
        self._iter = [x[0] for x in sorted(self.sequence.items(), key=lambda x: x[1])]
        return self

    def __next__(self):
        if not self._iter:
            raise StopIteration
        else:
            key = self._iter.pop(0)
            return key, self.sequence[key]

    def __len__(self):
        return len(self.sequence)


if __name__ == '__main__':
    class Item:
        def __init__(self, text):
            import uuid
            self.id = uuid.uuid4().__str__()
            self.text = text

        def __repr__(self):
            return f'<Item object>: text = "{self.text}" pk = {self.id}'


    items = [Item("Item #"+str(t)) for t in range(1, 11)]
    items_order = OrderManager()

    for i in items:
        items_order.add_key(i.id)

    assert len(items_order) == 10, "Ten items' keys were added to the Order Manager."
    assert items_order.get_key_by_index(0) == items[0].id, "Get first item's key."
    assert items_order.get_key_by_index(9) == items[9].id, "Get last item's key."
    assert items_order.get_key_by_index(-1) is None, "Get incorrect index."
    assert items_order.get_key_by_index(10) is None, "Get index out of range."
    assert str(items_order)[:27] == "<object of Order Manager>:\n", "Represent object as a string."

    items_order.change_key_index(4, 1)
    assert items_order.get_key_by_index(0) == items[0].id, "Changed index from 4 to 1. Testing index = 0."
    assert items_order.get_key_by_index(1) == items[4].id, "Changed index from 4 to 1. Testing index = 1."
    assert items_order.get_key_by_index(2) == items[1].id, "Changed index from 4 to 1. Testing index = 2."
    assert items_order.get_key_by_index(3) == items[2].id, "Changed index from 4 to 1. Testing index = 3."
    assert items_order.get_key_by_index(4) == items[3].id, "Changed index from 4 to 1. Testing index = 4."
    assert items_order.get_key_by_index(5) == items[5].id, "Changed index from 4 to 1. Testing index = 5."

    items_order.change_key_index(2, 5)
    assert items_order.get_key_by_index(0) == items[0].id, "Changed index from 2 to 5. Testing index = 0."
    assert items_order.get_key_by_index(1) == items[4].id, "Changed index from 2 to 5. Testing index = 1."
    assert items_order.get_key_by_index(2) == items[2].id, "Changed index from 2 to 5. Testing index = 2."
    assert items_order.get_key_by_index(3) == items[3].id, "Changed index from 2 to 5. Testing index = 3."
    assert items_order.get_key_by_index(4) == items[5].id, "Changed index from 2 to 5. Testing index = 4."
    assert items_order.get_key_by_index(5) == items[1].id, "Changed index from 2 to 5. Testing index = 5."
    assert items_order.get_key_by_index(6) == items[6].id, "Changed index from 2 to 5. Testing index = 6."

    items_order.delete_key(items[5].id)
    assert items_order.get_key_by_index(3) == items[3].id, "Deleted item id [5] from index [4]. Testing index [3]."
    assert items_order.get_key_by_index(4) == items[1].id, "Deleted item id [5] from index [4]. Testing index [4]."
    assert items_order.get_key_by_index(5) == items[6].id, "Deleted item id [5] from index [4]. Testing index [5]."
    assert items_order.get_key_by_index(6) == items[7].id, "Deleted item id [5] from index [4]. Testing index [6]."

    print('Module <order_manager> self testing completed successfully.')
