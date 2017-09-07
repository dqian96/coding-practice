# Problem: Paginate

"""

Paginate from a list given that there should be unique ids on each page, unless
there are none left, then pad in order.

"""

from collections import defaultdict, namedtuple

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node):
        if self.head == node and self.tail == node:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node        
        node.prev = self.tail
        node.next = None
        self.tail = node

def paginate(num, results):
    Listing = namedtuple("Listing", ['host_id', 'csv_line'])  # host id as a field to prevent repeated parsing
    
    # linkedlist containing unpaged listings in order; allows fast removals of paged listings anywhere
    listings = LinkedList()

    # keeps track of unpaged listings host ids,
    # which avoids traversing whole list when no listings with unique hosts are left for the page
    hosts_to_num_listings_left = defaultdict(int)

    for csv_line in results:
        # pre-processing
        host_id = csv_line.split(',')[0]
        listing = Node(Listing(host_id, csv_line))
        listings.append(listing)
        hosts_to_num_listings_left[host_id] += 1

    paged_listings = []

    added_to_page = 0
    hosts_on_page = set()
    curr = listings.head
    while curr is not None:
        # keeping adding listings to page if there exists more to add
        
        while curr.data.host_id in hosts_on_page and len(hosts_on_page) < len(hosts_to_num_listings_left):
            # host is already on page, and there are still more hosts to add
            curr = curr.next

        if len(hosts_on_page) >= len(hosts_to_num_listings_left):
            # no more unique hosts left to add to page; add from the start of remaining listings
            curr = listings.head
            if curr is None:
                # no more left
                break

        # add listing to page
        listings.remove(curr)

        hosts_to_num_listings_left[curr.data.host_id] -= 1

        hosts_on_page.add(curr.data.host_id)

        paged_listings.append(curr.data.csv_line)
        added_to_page += 1

        if added_to_page == num:
            # done filling out the page

            for host_id in hosts_on_page:
                if hosts_to_num_listings_left[host_id] == 0:
                    # no more of this host left on listings
                    hosts_to_num_listings_left.pop(host_id)

            # reset conditions
            added_to_page = 0
            hosts_on_page.clear()
            curr = listings.head
            if curr is not None:
                # new page
                paged_listings.append('')

    return paged_listings
