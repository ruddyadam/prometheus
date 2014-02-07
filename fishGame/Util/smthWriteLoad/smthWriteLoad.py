#smthWriteLoad.py

something = [(134, 39), (134, 56), (134, 87),
        (134, 118), (134, 80), (137, 71), (135, 96), (133, 113),
        (132, 130), (132, 145), (134, 148), (139, 111), (139, 99), (131, 77), (131, 53),
        (131, 47), (131, 88), (132, 108), (135, 134), (136, 163), (137, 167), (137, 142),
        (136, 116), (136, 97), (136, 112), (154, 104), (167, 103), (185, 95), (145, 106),
        (139, 109), (173, 98), (173, 98), (160, 99), (172, 95), (146, 108), (154, 102),
        (156, 100), (177, 98), (181, 104), (196, 82), (194, 39), (194, 49), (194, 69),
        (194, 88), (194, 112), (194, 132), (195, 139), (195, 112), (195, 90), (195, 58),
        (195, 45), (195, 78), (195, 112), (191, 151), (198, 113), (198, 99), (197, 103),
        (196, 128), (196, 136), (196, 144), (193, 104), (193, 99), (197, 109), (198, 127),
        (249, 89), (259, 98), (280, 99), (289, 99), (296, 100), (307, 90), (303, 81),
        (286, 75), (268, 73), (256, 78), (248, 95), (248, 106), (248, 113), (255, 128),
        (268, 151), (283, 157), (312, 126), (315, 124), (301, 145), (297, 149), (306, 141),
        (302, 139), (287, 154), (275, 161), (255, 151), (252, 141), (261, 157), (254, 146),
        (250, 134), (245, 104), (246, 92), (261, 79), (281, 75), (292, 75), (304, 87), (304, 94),
        (291, 107), (275, 107), (253, 113), (252, 106), (267, 102), (269, 102), (249, 107),
        (273, 103), (262, 104), (269, 107), (275, 105), (289, 104), (296, 102), (305, 99),
        (305, 82), (301, 74), (290, 74), (273, 73), (255, 78), (252, 90), (252, 110),
        (259, 114), (252, 120), (252, 126), (252, 139), (254, 152), (263, 154), (276, 156),
        (287, 156), (303, 148), (308, 137), (349, 76), (350, 76), (354, 79), (360, 90),
        (366, 101), (368, 105), (377, 119), (377, 122), (373, 100), (356, 90), (355, 82),
        (355, 85), (363, 100), (365, 107), (367, 115), (370, 122), (373, 128), (374, 116),
        (372, 109), (358, 99), (358, 96), (416, 69), (412, 69), (398, 86), (394, 93),
        (385, 109), (391, 93), (398, 85), (407, 77), (399, 90), (383, 104), (382, 112),
        (392, 96), (390, 101), (384, 112), (379, 124), (374, 140), (368, 153), (366, 157),
        (369, 146), (372, 139), (376, 135), (375, 147), (375, 161), (369, 182), (369, 187),
        (367, 196), (366, 170), (366, 170), (367, 187), (366, 194), (366, 200), (365, 173),
        (370, 158), (373, 150), (374, 173), (368, 190), (362, 200), (353, 209), (318, 187),
        (329, 194), (330, 193), (335, 196), (336, 201), (335, 202), (342, 204), (347, 205), (353, 205),
        (358, 205), (365, 202), (360, 199), (348, 200), (327, 193), (267, 105), (268, 105),
        (264, 106), (263, 106), (252, 89), (252, 81), (262, 77), (269, 75), (282, 70), (285, 70),
        (276, 72), (297, 74), (298, 74), (305, 80), (307, 85), (199, 54), (195, 61), (195, 71),
        (195, 73), (195, 69), (198, 120), (199, 122), (134, 130), (134, 140), (134, 146), (134, 163),
        (135, 173), (136, 176), (133, 156), (133, 155), (133, 156), (137, 69), (136, 67), (135, 65),
        (133, 73), (132, 83), (131, 95), (130, 104), (130, 113), (74, 221), (74, 221), (71, 234),
        (68, 248), (68, 256), (68, 272), (73, 255), (77, 235), (77, 234), (75, 256), (74, 268),
        (74, 263), (74, 261), (74, 266), (74, 282), (74, 290), (75, 303), (75, 316),
        (75, 320), (73, 301), (73, 292), (75, 277), (75, 301), (74, 313), (73, 331),
        (73, 344), (73, 349), (71, 355), (71, 373), (73, 391), (75, 396), (78, 402), (79, 403),
        (72, 381), (72, 370), (72, 363), (72, 378), (72, 391), (73, 402), (74, 407), (82, 406),
        (95, 405), (103, 405), (117, 404), (129, 401), (140, 399), (148, 395), (160, 388),
        (166, 381), (169, 370), (169, 356), (168, 352), (136, 335), (122, 335), (113, 333),
        (99, 331), (92, 331), (92, 331), (104, 331), (118, 332), (150, 345), (160, 349),
        (164, 351), (167, 348), (149, 340), (99, 328), (104, 325), (128, 311), (139, 302),
        (149, 293), (149, 281), (149, 274), (137, 265), (124, 261), (96, 256), (87, 254),
        (83, 252), (83, 252), (83, 252), (98, 252), (111, 257), (128, 263), (136, 265),
        (145, 266), (155, 275), (154, 290), (135, 312), (127, 317), (100, 328), (93, 332),
        (108, 325), (110, 323), (113, 321), (116, 316), (119, 315), (136, 307), (141, 299),
        (147, 286), (149, 269), (148, 263), (122, 259), (107, 257), (92, 255), (82, 251),
        (79, 248), (79, 242), (296, 272), (283, 265), (253, 264), (237, 264), (220, 271),
        (205, 283), (201, 302), (201, 319), (202, 323), (203, 332), (205, 341), (205, 352),
        (207, 359), (209, 364), (224, 375), (237, 378), (251, 382), (257, 383), (272, 384),
        (287, 380), (291, 373), (301, 349), (304, 339), (308, 323), (308, 314), (308, 300),
        (307, 290), (306, 277), (291, 269), (275, 261), (247, 259), (269, 264), (269, 264),
        (267, 265), (260, 265), (249, 267), (246, 268), (236, 268), (228, 269), (211, 279),
        (208, 287), (204, 297), (203, 309), (203, 321), (203, 332), (203, 343), (205, 354),
        (209, 367), (210, 368), (213, 374), (228, 380), (241, 380), (253, 379), (263, 378),
        (269, 377), (275, 375), (280, 378), (290, 366), (296, 356), (297, 354), (302, 336),
        (303, 332), (306, 322), (309, 306), (309, 301), (308, 291), (304, 288), (300, 285),
        (299, 284), (291, 275), (287, 275), (284, 274), (280, 274), (279, 273), (270, 268),
        (256, 265), (243, 264), (231, 264), (225, 264), (213, 270), (209, 278), (207, 286),
        (206, 296), (206, 301), (206, 316), (206, 326), (206, 339), (203, 355), (203, 361),
        (203, 367), (206, 377), (212, 381), (228, 384), (236, 384), (253, 385), (267, 385),
        (280, 381), (289, 378), (311, 364), (317, 360), (317, 353), (310, 338), (307, 354),
        (305, 367), (299, 374), (296, 376), (288, 383), (287, 385), (293, 376), (293, 364),
        (297, 361), (375, 261), (374, 262), (372, 280), (372, 295), (371, 277), (371, 288),
        (371, 292), (372, 299), (375, 309), (379, 323), (381, 332), (381, 341), (383, 343),
        (387, 348), (388, 361), (392, 371), (394, 379), (395, 385), (395, 387), (386, 373),
        (382, 351), (379, 339), (375, 329), (373, 316), (372, 315), (372, 304), (369, 298),
        (366, 281), (366, 273), (381, 252), (377, 263), (378, 263), (384, 261), (395, 259),
        (400, 257), (412, 256), (427, 256), (438, 262), (444, 267), (447, 278), (446, 285),
        (442, 291), (433, 301), (424, 309), (410, 312), (399, 317), (393, 320), (391, 321),
        (391, 321), (413, 315), (427, 309), (418, 313), (401, 318), (393, 320), (388, 322),
        (384, 325), (384, 325), (405, 318), (413, 316), (429, 314), (439, 310), (445, 309),
        (450, 308), (456, 305), (458, 305), (479, 307), (493, 319), (498, 330), (503, 345),
        (503, 357), (496, 370), (484, 376), (476, 379), (446, 387), (420, 393), (405, 397),
        (396, 382), (393, 374), (389, 360), (392, 385), (394, 391), (396, 394), (404, 394),
        (408, 394), (422, 392), (434, 389), (446, 387), (457, 386), (464, 384), (469, 383),
        (463, 381), (451, 385), (442, 387), (428, 392), (422, 395), (504, 353), (505, 348),
        (504, 338), (500, 333), (494, 328), (490, 324), (486, 317), (483, 315), (472, 315),
        (465, 316), (465, 313), (465, 313), (464, 312), (472, 308), (475, 308), (464, 309),
        (456, 309), (445, 311), (431, 311), (430, 311), (425, 315), (423, 316), (591, 215),
        (589, 228), (584, 243), (584, 256), (585, 271), (586, 282), (586, 282), (585, 307),
        (585, 312), (585, 305), (585, 293), (585, 286), (585, 269), (585, 269), (586, 233),
        (587, 223), (587, 226), (587, 226), (580, 268), (580, 268), (580, 268), (580, 304),
        (580, 304), (580, 304), (580, 304), (579, 303), (577, 272), (577, 293), (577, 285), (579, 295), (581, 306),
        (585, 314), (583, 320), (581, 324), (581, 310), (580, 320), (580, 322), (584, 327),
        (584, 332), (584, 340), (583, 338), (588, 364), (582, 369), (580, 370), (582, 373),
        (589, 374), (592, 373), (590, 373), (588, 373), (589, 370), (583, 370), (582, 371), (587, 364), (583, 367), (577, 364), (584, 363), (590, 363),
        (592, 370), (592, 364), (596, 371), (594, 380)]




def writeSmth(someTupleList): #someTupleList = something
    with open('smthWrite.txt', 'w') as smthWrite: #'a' to append, 'w' to overwrite
        smthWrite.write(str(someTupleList)) #.strip('[]'))

def loadSmth(tupleTxt): #tupleTxt = smthWrite.txt
    with open(tupleTxt, 'r') as smthLoad:
        # print smthLoad.read()
        outputThis = []
        tempLen = []
        outputThis = smthLoad.read()
        print outputThis
        print "imported file is", type(outputThis)
        for n in outputThis:
            if n in something:
                tempLen.append(n)                   

        print "list output to file initailly had", len(something), "items"
        print "list writeen to, then read from has", len(tempLen), "items"

if __name__ == "__main__":
    writeSmth(something)
    loadSmth('smthWrite.txt')
    print "finished"
