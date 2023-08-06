# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2017 Tijme Gommers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from collections import OrderedDict
from nyawc.http.Response import Response
from nyawc.QueueItem import QueueItem
from nyawc.helpers.URLHelper import URLHelper

class Queue:
    """A 'hash' queue containing all the requests of the crawler.

    Note:
        This queue uses a certain hash (from :meth:`__get_hash`) to prevent
        duplicate entries and improve the time complexity by checking if the
        hash exists instead of iterating over all items.

    Attributes:
        __options (:class:`nyawc.Options`): The options to use (used when generating queue item hashes).
        count_total (int): The total count of requests in the queue.
        count_queued (int): The amount of queued items in the queue.
        count_in_progress (int): The amount of in progress items in the queue.
        count_finished (int): The amount of finished items in the queue.
        count_cancelled (int): The amount of cancelled items in the queue.
        count_errored (int): The amount of errored items in the queue.
        items_queued list(:class:`nyawc.QueueItem`): The queued items (yet to be executed).
        items_in_progress list(:class:`nyawc.QueueItem`): The items currently being executed.
        items_finished list(:class:`nyawc.QueueItem`): The finished items.
        items_cancelled list(:class:`nyawc.QueueItem`): Items that were cancelled.
        items_errored list(:class:`nyawc.QueueItem`): Items that generated an error.

    """

    def __init__(self, options):
        """Constructs a Queue instance.

        Args:
            options (:class:`nyawc.Options`): The options to use.

        """

        self.__options = options
        self.count_total = 0
        self.count_queued = 0
        self.count_in_progress = 0
        self.count_finished = 0
        self.count_cancelled = 0
        self.count_errored = 0
        self.items_queued = OrderedDict()
        self.items_in_progress = OrderedDict()
        self.items_finished = OrderedDict()
        self.items_cancelled = OrderedDict()
        self.items_errored = OrderedDict()

    def add_request(self, request):
        """Add a request to the queue.

        Args:
            request (:class:`nyawc.http.Request`): The request to add.

        Returns:
            :class:`nyawc.QueueItem`: The created queue item.

        """

        queue_item = QueueItem(request, Response(request.url))
        self.add(queue_item)
        return queue_item

    def has_request(self, request):
        """Check if the given request already exists in the queue.

        Args:
            request (:class:`nyawc.http.Request`): The request to check.

        Returns:
            bool: True if already exists, False otherwise.

        """

        queue_item = QueueItem(request, Response(request.url))
        key = self.__get_hash(queue_item)

        for status in QueueItem.STATUSES:
            if key in self.__get_var("items_" + status).keys():
                return True

        return False

    def add(self, queue_item):
        """Add a request/response pair to the queue.

        Args:
            queue_item (:class:`nyawc.QueueItem`): The queue item to add.

        """

        hash_key = self.__get_hash(queue_item)
        items = self.__get_var("items_" + queue_item.status)
        items_count = self.__get_var("count_" + queue_item.status)

        if hash_key in items.keys():
            return

        self.__set_var("count_" + queue_item.status, (items_count + 1))
        items[self.__get_hash(queue_item)] = queue_item

        self.count_total += 1

    def move(self, queue_item, status):
        """Move a request/response pair to another status.

        Args:
            queue_item (:class:`nyawc.QueueItem`): The queue item to move
            status (str): The new status of the queue item.

        """

        items = self.__get_var("items_" + queue_item.status)
        items_count = self.__get_var("count_" + queue_item.status)

        del items[self.__get_hash(queue_item)]
        self.__set_var("count_" + queue_item.status, (items_count - 1))
        self.count_total -= 1

        queue_item.status = status
        self.add(queue_item)

    def get_first(self, status):
        """Get the first item in the queue that has the given status.

        Args:
            status (str): return the first item with this status.

        Returns:
            :class:`nyawc.QueueItem`: The first queue item with the given status.

        """

        items = self.get_all(status)

        if items:
            return list(items.items())[0][1]

        return None

    def get_all(self, status):
        """Get all the items in the queue that have the given status.

        Args:
            status (str): return the items with this status.

        Returns:
            list(:class:`nyawc.QueueItem`): All the queue items with the given status.

        """

        return self.__get_var("items_" + status)

    def get_progress(self):
        """Get the progress of the queue in percentage (float).

        Returns:
            float: The 'finished' progress in percentage.

        """

        count_remaining = self.count_queued + self.count_in_progress
        percentage_remaining = 100 / self.count_total * count_remaining

        return 100 - percentage_remaining

    def __get_hash(self, queue_item):
        """Generate and return the dict index hash of the given queue item.

        Note:
            Cookies should not be included in the hash calculation because
            otherwise requests are crawled multiple times with e.g. different
            session keys, causing infinite crawling recursion.

        Note:
            At this moment the keys do not actually get hashed since it works perfectly without and
            since hashing the keys requires us to built hash collision management.

        Args:
            queue_item (:class:`nyawc.QueueItem`): The queue item to get the hash from.

        Returns:
            str: The hash of the given queue item.

        """

        key = queue_item.request.method

        key += URLHelper.get_protocol(queue_item.request.url)
        key += URLHelper.get_subdomain(queue_item.request.url)
        key += URLHelper.get_hostname(queue_item.request.url)
        key += URLHelper.get_tld(queue_item.request.url)
        key += URLHelper.get_path(queue_item.request.url)

        key += str(URLHelper.get_ordered_params(queue_item.request.url))

        if queue_item.request.data is not None:
            key += str(queue_item.request.data.keys())

        return key

    def __set_var(self, name, value):
        """Set an instance/class var by name.

        Args:
            name (str): The name of the variable.
            value (obj): I'ts new value.

        """

        setattr(self, name, value)

    def __get_var(self, name):
        """Get an instance/class var by name.

        Args:
            name (str): The name of the variable.

        Returns:
            obj: I'ts value.

        """

        return getattr(self, name)
