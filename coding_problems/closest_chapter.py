"""
Create a function that returns which chapter is nearest to the page you're on. If two chapters are equidistant, return the chapter with the higher page number.

Examples
nearest_chapter({
  "Chapter 1" : 1,
  "Chapter 2" : 15,
  "Chapter 3" : 37
}, 10) ➞ "Chapter 2"


nearest_chapter({
  "New Beginnings" : 1,
  "Strange Developments" : 62,
  "The End?" : 194,
  "The True Ending" : 460
}, 200) ➞ "The End?"


nearest_chapter({
  "Chapter 1a" : 1,
  "Chapter 1b" : 5
}, 3) ➞ "Chapter 1b"
"""

def nearest_chapter(chapter_map, page):
    lookup_map = {}
    for key in chapter_map:
        lookup_map[chapter_map[key]] = key
    chapter_array = []
    for key in chapter_map:
        chapter_array.append(chapter_map[key])
    chapter_array = sorted(chapter_array)
    chapter_index = 0
    while page > chapter_array[chapter_index]:
        chapter_index += 1
    if abs(page - chapter_array[chapter_index]) > abs(page - chapter_array[chapter_index - 1]):
        return lookup_map[chapter_array[chapter_index - 1]]
    else:
        return lookup_map[chapter_array[chapter_index]]


print(nearest_chapter({
  "Chapter 3" : 37,
  "Chapter 1" : 1,
  "Chapter 2" : 15

}, 10) )

print(nearest_chapter({
  "New Beginnings" : 1,
  "Strange Developments" : 62,
  "The End?" : 194,
  "The True Ending" : 460
}, 200))

print(nearest_chapter({
  "Chapter 1a" : 1,
  "Chapter 1b" : 5
}, 3))
