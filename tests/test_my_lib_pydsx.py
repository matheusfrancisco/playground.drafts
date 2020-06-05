from pydsx import SinglyLinkedList


def test_append_in_slinked_list():
    slinked_list = SinglyLinkedList()
    slinked_list.append(1)
    slinked_list.append(2)
    slinked_list.append(3)
    slinked_list.append(4)
    assert len(slinked_list) == 4
