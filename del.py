from node import Node

i = "Intersection"
r = "Road"
b = "Block"

#i
"Intersection", True, True, True, True

#horizontal road

"Road", False, True, False, True

#vertical road

"Road", True, False, True, True

# blocl

"Block", False, False, False, False

map = [[
    Node("00", "Intersection", True, True, True, True),
    Node("01", "Road", False, True, False, True),
    Node("02", "Intersection", True, True, True, True),
    Node("03", "Road", False, True, False, True),
    Node("04", "Intersection", True, True, True, True)
],
    [
           Node("10", "Road", True, False, True, True),
           Node("11", "Block", False, False, False, False),
           Node("12", "Road", True, False, True, True),
           Node("13", "Block", False, False, False, False),
           Node("14", "Road", True, False, True, True)
       ], [
        Node("20", "Intersection", True, True, True, True), Node("21", "Road", False, True, False, True), Node("22", "Intersection", True, True, True, True), Node("23", "Road", False, True, False, True), Node("24", "Intersection", True, True, True, True)
       ], [
        Node("30", "Road", True, False, True, True),Node("31", "Block", False, False, False, False), Node("32", "Road", True, False, True, True), Node("33", "Block", False, False, False, False),Node("34", "Road", True, False, True, True)
       ], [
        Node("40", "Intersection", True, True, True, True), Node("41", "Road", False, True, False, True),Node("42","Intersection", True, True, True, True), Node("43", "Block", False, False, False, False),Node("44","Intersection", True, True, True, True)
       ]]
