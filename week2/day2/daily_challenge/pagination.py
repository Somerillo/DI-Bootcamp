# # ascii_art = """
# #
# #
# #
# #       :::::::::::          :::    :::     ::: ::::::::::: ::::::::::          ::::::::   ::::::::  :::::::::
# #          :+:              :+:    :+:   :+: :+:   :+:     :+:                :+:    :+: :+:    :+: :+:    :+:
# #         +:+              +:+    +:+  +:+   +:+  +:+     +:+                +:+    +:+ +:+    +:+ +:+    +:+
# #        +#+              +#++:++#++ +#++:++#++: +#+     +#++:++#           +#+    +:+ +#+    +:+ +#++:++#+
# #       +#+              +#+    +#+ +#+     +#+ +#+     +#+                +#+    +#+ +#+    +#+ +#+
# #      #+#              #+#    #+# #+#     #+# #+#     #+#                #+#    #+# #+#    #+# #+#
# # ###########          ###    ### ###     ### ###     ##########          ########   ########  ###
# #
# #
# #
# # """
# #     Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# #     The Pagination class will accept 2 parameters:
# #         items (default: None): It will contain a list of contents to paginate.
# #         pageSize (default: 10): The amount of items to show in each page.

# #     So for example we could initialize our pagination like this:

# #     alphabetList = list("abcdefghijklmnopqrstuvwxyz")

# #     p = Pagination(alphabetList, 4)


# #     The Pagination class will have a few methods:
# #         getVisibleItems() : returns a list of items visible depending on the pageSize

# #     So for example we could use this method like this:

# #     p.getVisibleItems()
# #     # ["a", "b", "c", "d"]

# #         You will have to implement various methods to go through the pages such as:
# #             prevPage()
# #             nextPage()
# #             firstPage()
# #             lastPage()
# #             goToPage(pageNum)

# # Here’s a continuation of the example above using nextPage and lastPage:

# # alphabetList = list("abcdefghijklmnopqrstuvwxyz")

# # p = Pagination(alphabetList, 4)

# # p.getVisibleItems()
# # # ["a", "b", "c", "d"]

# # p.nextPage()

# # p.getVisibleItems()
# # # ["e", "f", "g", "h"]

# # p.lastPage()

# # p.getVisibleItems()
# # # ["y", "z"]


# # Notes

# #     The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# #     The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# #     Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# #     If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).


class Pagination:
    """
    creates a class to handle paginated content in a website, its parameters are: \n
    -   items (default: None): It will contain a list of contents to paginate. \n
    -   pageSize (default: 10): The amount of items to show in each page.

    """

    def __init__(self, items=None, pageSize=10):
        self.items = items or []
        # could be a float, in that case just convert it to an int
        self.pageSize = int(pageSize)
        # set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0:
        self.totalPages = max(
            # paper & pencil from the example in instructions
            1, (len(self.items) + self.pageSize - 1) // self.pageSize)
        self.currentPage = 1

    def getVisibleItems(self):
        """
        returns a list of items visible depending on the pageSize
        """
        # minus one because page numeration starts in 1, but python lists indexes start in 0
        # multiply by self.pageSize to get 1st index of current page
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]  # to be chainable

    def prevPage(self):  # chainable, so you can call them one after the other like this: p.nextPage().nextPage()
        self.currentPage = max(1, self.currentPage - 1)  # cant reach to zero
        return self  # to be chainable

    def nextPage(self):  # chainable, so you can call them one after the other like this: p.nextPage().nextPage()
        # cant be more than total pages
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self  # to be chainable

    def firstPage(self):
        self.currentPage = 1
        return self  # to be chainable

    def lastPage(self):
        self.currentPage = self.totalPages
        return self  # to be chainable

    def goToPage(self, pageNum):
        # could be a float, in that case just convert it to an int
        # If a page is outside of the totalPages attribute,
        # then the goToPage method should go to the closest page to the number provided
        pageNum = int(pageNum)
        self.currentPage = max(1, min(self.totalPages, pageNum))
        return self  # to be chainable



alphabetList = list("abcdefghijklmnopqrstuvwxyz")

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  # ['a', 'b', 'c', 'd']

p.nextPage()
print(p.getVisibleItems())  # ['e', 'f', 'g', 'h']

p.lastPage()
print(p.getVisibleItems())  # ['y', 'z']

p.goToPage(10).prevPage()
print(p.currentPage)  # 6 (bc only 7 pages in total)

p.firstPage().nextPage().nextPage()
print(p.getVisibleItems())  # ['i', 'j', 'k', 'l']