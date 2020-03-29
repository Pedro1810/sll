from sll import *
import pytest

linked_list = None

def setup():
    global linked_list
    linked_list = SingleLinkedList()

def teardown():
    global linked_list
    linked_list = None

@pytest.mark.skip
def test_create_node():
    node = Node(1)
    assert isinstance(node, Node)
    assert node.data == 1
    node.next = Node(2)
    assert node.next.data == 2

def test_is_empty_on_new_list():
    assert linked_list.isempty() == True

def test_add():
    linked_list.add(1)
    assert linked_list.isempty() == False
    linked_list.add(2)
    assert linked_list.isempty() == False
    tmp = linked_list.add(3).add(4).add(5)
    assert isinstance(tmp, SingleLinkedList)

@pytest.mark.skip
def test_clear():
    linked_list.add(1).add(2).add(3)
    assert linked_list.isempty() == False
    linked_list.clear()
    assert linked_list.isempty() == True

def test_size():
    assert linked_list.size() == 0
    assert linked_list.add(1).size() == 1
    assert linked_list.add(2).size() == 2

def test_list_in_loop():
    linked_list.add(1).add(2).add(3)
    for item in linked_list:
        print(item)

def test_get():
    '''Получаем значение узла по его индексу'''
    linked_list.add(42).add(21).add(33).add(13)
    assert linked_list.get(0) == 13
    assert linked_list.get(1) == 33
    assert linked_list.get(2) == 21
    assert linked_list.get(3) == 42

def test_contains():
    '''Возвращает True/False для item'''
    linked_list.add(42).add(21).add(33)
    assert linked_list.contains(21) == True
    assert linked_list.contains(210) == False

def test_index():
    '''Возвращает индекс узла для item'''
    linked_list.add(42).add(21)
    assert linked_list.index(21) == 0
    assert linked_list.index(42) == 1
    linked_list.add(33)
    assert linked_list.index(33) == 0
    assert linked_list.index(42) == 2