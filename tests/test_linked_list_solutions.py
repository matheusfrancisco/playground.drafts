from solutions import remove_duplicates
from pydsx import SinglyLinkedList

"""
if you want to see SinglyLinkedList implementation
go to :github.com/xico-labs/data_structures_and_algorithms_py

"""


def test_remove_duplicate_nodes():
    slinked_list = SinglyLinkedList()
    assert len(slinked_list) == len(remove_duplicates(slinked_list))

    slinked_list.append(1)
    slinked_list.append(2)
    slinked_list.append(3)
    slinked_list.append(3)
    slinked_list.append(4)
    assert [4, 3, 2, 1] == [item for item in remove_duplicates(slinked_list)]
