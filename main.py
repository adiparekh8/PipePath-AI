import pygame
import sys
import random
import math
import asyncio
import time

carp_options = list(range(5, 13))
current_carp_index = 0
num_fish = carp_options[current_carp_index]
initial_fish_count = num_fish

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))

background_color = (139, 94, 60)
murky_green = (20, 40, 20)
baby_blue = (0, 255, 255)
text_color = (0, 0, 0)
font_name = "timesnewroman"

# *** REPLACE THE POLYGON WITH A VISIBLE ONE ***
lake_polygon = [(536, 96), (535, 97), (506, 97), (505, 99), (484, 99), (482, 101), (475, 101), (473, 103), (469, 103), (468, 104), (463, 104), (462, 106), (456, 106), (455, 108), (450, 108), (449, 109), (445, 109), (443, 111), (441, 111), (439, 113), (436, 113), (435, 115), (433, 115), (430, 118), (430, 120), (429, 121), (429, 140), (430, 142), (430, 146), (433, 149), (433, 151), (443, 163), (445, 163), (453, 173), (455, 173), (461, 180), (461, 182), (464, 187), (464, 188), (469, 194), (469, 195), (470, 197), (470, 199), (472, 201), (472, 202), (473, 204), (473, 209), (475, 211), (475, 244), (473, 245), (473, 254), (472, 256), (472, 262), (470, 264), (470, 273), (469, 274), (469, 280), (468, 281), (468, 288), (466, 290), (466, 293), (464, 295), (464, 297), (463, 299), (463, 300), (459, 305), (457, 305), (456, 307), (445, 307), (443, 305), (439, 305), (437, 304), (435, 304), (433, 302), (430, 302), (429, 300), (427, 300), (426, 299), (423, 299), (421, 297), (420, 297), (419, 295), (417, 295), (416, 293), (414, 293), (413, 292), (412, 292), (410, 290), (409, 290), (407, 288), (406, 288), (403, 285), (402, 285), (399, 281), (398, 281), (396, 280), (394, 280), (393, 278), (392, 278), (390, 276), (389, 276), (387, 274), (386, 274), (384, 273), (383, 273), (380, 269), (378, 269), (374, 264), (373, 264), (371, 262), (370, 262), (369, 261), (367, 261), (366, 259), (364, 259), (363, 257), (360, 257), (359, 256), (357, 256), (356, 254), (355, 254), (353, 252), (350, 252), (349, 250), (347, 250), (346, 249), (343, 249), (341, 247), (340, 247), (339, 245), (334, 245), (333, 244), (327, 244), (326, 242), (323, 242), (321, 240), (317, 240), (315, 238), (312, 238), (310, 237), (306, 237), (304, 235), (297, 235), (296, 233), (260, 233), (258, 235), (254, 235), (253, 237), (248, 237), (247, 238), (231, 238), (229, 240), (208, 240), (206, 242), (198, 242), (197, 244), (191, 244), (190, 245), (185, 245), (184, 247), (181, 247), (179, 249), (176, 249), (175, 250), (174, 250), (162, 264), (162, 266), (156, 273), (156, 274), (147, 286), (147, 288), (145, 290), (145, 292), (143, 293), (143, 297), (142, 299), (142, 302), (141, 304), (141, 307), (139, 309), (139, 314), (138, 316), (138, 319), (135, 323), (135, 324), (128, 333), (128, 336), (129, 338), (129, 340), (132, 343), (132, 350), (133, 352), (133, 409), (135, 410), (135, 421), (136, 422), (136, 427), (138, 429), (138, 433), (139, 434), (139, 436), (148, 446), (149, 446), (152, 450), (154, 450), (155, 452), (156, 452), (158, 453), (159, 453), (161, 455), (163, 455), (165, 457), (169, 457), (171, 458), (175, 458), (176, 460), (181, 460), (182, 462), (188, 462), (190, 464), (195, 464), (197, 465), (201, 465), (202, 467), (205, 467), (206, 469), (212, 469), (214, 470), (263, 470), (264, 469), (268, 469), (270, 467), (271, 467), (272, 465), (276, 465), (277, 464), (278, 464), (280, 462), (281, 462), (283, 460), (287, 460), (288, 458), (292, 458), (294, 457), (298, 457), (300, 455), (303, 455), (304, 453), (310, 453), (312, 452), (313, 452), (314, 453), (321, 453), (323, 455), (326, 455), (327, 457), (331, 457), (333, 458), (337, 458), (339, 460), (343, 460), (344, 462), (347, 462), (349, 464), (351, 464), (353, 465), (356, 465), (357, 467), (359, 467), (360, 469), (362, 469), (363, 470), (366, 470), (367, 472), (369, 472), (371, 476), (373, 476), (374, 477), (376, 477), (377, 479), (378, 479), (382, 482), (383, 482), (386, 486), (387, 486), (392, 491), (393, 491), (399, 498), (400, 498), (409, 508), (409, 510), (412, 513), (412, 515), (414, 519), (414, 520), (417, 524), (417, 525), (420, 529), (420, 531), (432, 544), (432, 546), (433, 548), (433, 553), (435, 555), (435, 558), (436, 560), (436, 562), (437, 563), (437, 565), (441, 568), (441, 570), (442, 572), (442, 574), (445, 577), (445, 579), (448, 582), (448, 584), (456, 594), (457, 594), (462, 599), (463, 599), (464, 601), (466, 601), (469, 605), (470, 605), (472, 606), (473, 606), (475, 608), (478, 608), (479, 610), (480, 610), (482, 611), (485, 611), (486, 613), (489, 613), (491, 615), (495, 615), (496, 617), (504, 617), (505, 618), (512, 618), (513, 620), (521, 620), (522, 622), (538, 622), (539, 623), (550, 623), (552, 622), (564, 622), (565, 620), (571, 620), (572, 618), (577, 618), (578, 617), (582, 617), (584, 615), (586, 615), (588, 613), (590, 613), (591, 611), (592, 611), (593, 610), (595, 610), (597, 608), (598, 608), (599, 606), (601, 606), (604, 603), (605, 603), (607, 601), (608, 601), (609, 599), (611, 599), (613, 598), (614, 598), (624, 586), (624, 584), (628, 579), (628, 577), (633, 572), (633, 570), (634, 568), (635, 568), (642, 560), (642, 558), (645, 555), (645, 553), (647, 551), (647, 550), (650, 546), (650, 544), (652, 541), (652, 539), (654, 538), (654, 536), (657, 532), (657, 531), (658, 529), (658, 527), (660, 525), (660, 522), (661, 520), (661, 519), (663, 517), (663, 515), (664, 513), (664, 512), (671, 503), (671, 501), (672, 500), (672, 498), (674, 496), (674, 491), (677, 488), (677, 486), (676, 484), (676, 482), (677, 481), (677, 477), (678, 476), (678, 474), (691, 458), (693, 458), (697, 453), (699, 453), (701, 450), (703, 450), (704, 448), (707, 448), (708, 446), (710, 446), (711, 445), (713, 445), (714, 443), (715, 443), (717, 441), (719, 441), (720, 440), (721, 440), (723, 438), (724, 438), (726, 436), (730, 436), (731, 434), (740, 434), (742, 433), (749, 433), (750, 434), (766, 434), (767, 436), (778, 436), (779, 438), (783, 438), (785, 440), (786, 440), (787, 441), (789, 441), (792, 445), (793, 445), (794, 446), (796, 446), (797, 448), (799, 448), (800, 450), (803, 450), (805, 452), (806, 452), (807, 453), (809, 453), (810, 455), (812, 455), (813, 457), (816, 457), (817, 458), (819, 458), (821, 460), (822, 460), (823, 462), (826, 462), (828, 464), (829, 464), (830, 465), (832, 465), (833, 467), (836, 467), (837, 469), (839, 469), (840, 470), (844, 470), (846, 472), (848, 472), (849, 474), (852, 474), (853, 476), (859, 476), (860, 477), (869, 477), (871, 479), (875, 479), (876, 477), (885, 477), (886, 476), (889, 476), (891, 474), (893, 474), (895, 472), (896, 472), (898, 470), (899, 470), (901, 469), (902, 469), (903, 467), (905, 467), (907, 465), (908, 465), (909, 464), (910, 464), (912, 462), (914, 462), (915, 460), (916, 460), (918, 458), (919, 458), (921, 457), (922, 457), (923, 455), (925, 455), (926, 453), (929, 453), (930, 452), (932, 452), (934, 450), (935, 450), (938, 446), (939, 446), (941, 445), (942, 445), (944, 443), (945, 443), (946, 441), (948, 441), (950, 440), (951, 440), (952, 438), (954, 438), (955, 436), (958, 436), (959, 434), (964, 434), (965, 433), (969, 433), (971, 431), (977, 431), (978, 429), (984, 429), (985, 427), (991, 427), (993, 426), (1000, 426), (1001, 424), (1021, 424), (1024, 427), (1027, 427), (1028, 429), (1032, 429), (1034, 431), (1037, 431), (1038, 433), (1043, 433), (1044, 434), (1047, 434), (1048, 436), (1050, 436), (1051, 438), (1052, 438), (1056, 441), (1057, 441), (1059, 445), (1061, 445), (1063, 446), (1064, 446), (1065, 448), (1067, 448), (1068, 450), (1071, 450), (1073, 452), (1075, 452), (1077, 453), (1087, 453), (1088, 452), (1090, 452), (1091, 450), (1093, 450), (1094, 448), (1095, 448), (1097, 446), (1099, 446), (1116, 426), (1116, 424), (1122, 417), (1122, 415), (1123, 414), (1123, 412), (1124, 410), (1124, 409), (1126, 407), (1126, 405), (1127, 403), (1127, 400), (1129, 398), (1129, 369), (1127, 367), (1127, 357), (1126, 355), (1126, 347), (1124, 345), (1124, 336), (1123, 335), (1123, 326), (1122, 324), (1122, 323), (1120, 321), (1122, 319), (1123, 319), (1124, 321), (1126, 321), (1127, 319), (1127, 317), (1129, 316), (1129, 314), (1127, 312), (1130, 309), (1133, 309), (1134, 307), (1137, 307), (1138, 309), (1142, 309), (1143, 311), (1146, 311), (1147, 312), (1152, 312), (1152, 311), (1150, 309), (1152, 307), (1152, 285), (1150, 285), (1149, 286), (1146, 286), (1144, 288), (1142, 288), (1140, 290), (1138, 290), (1138, 292), (1137, 293), (1136, 293), (1134, 292), (1131, 292), (1130, 290), (1127, 290), (1123, 285), (1123, 281), (1122, 280), (1120, 280), (1117, 276), (1116, 276), (1114, 274), (1113, 274), (1106, 266), (1106, 264), (1104, 262), (1104, 259), (1103, 257), (1103, 250), (1101, 249), (1101, 244), (1100, 242), (1100, 238), (1099, 237), (1099, 233), (1097, 231), (1097, 230), (1095, 228), (1095, 225), (1094, 223), (1094, 219), (1093, 218), (1093, 216), (1091, 214), (1091, 211), (1090, 209), (1090, 206), (1088, 204), (1088, 202), (1087, 201), (1087, 199), (1086, 197), (1086, 195), (1084, 194), (1084, 192), (1083, 190), (1083, 188), (1081, 187), (1081, 185), (1080, 183), (1080, 182), (1077, 178), (1077, 176), (1075, 175), (1075, 173), (1074, 171), (1074, 168), (1070, 163), (1070, 161), (1057, 146), (1056, 146), (1037, 123), (1036, 123), (1030, 116), (1028, 116), (1025, 113), (1024, 113), (1021, 109), (1020, 109), (1016, 106), (1015, 106), (1014, 104), (1011, 104), (1009, 103), (1004, 103), (1002, 101), (993, 101), (991, 103), (985, 103), (984, 104), (979, 104), (978, 106), (977, 106), (975, 108), (972, 108), (971, 109), (968, 109), (966, 111), (965, 111), (964, 113), (961, 113), (959, 115), (957, 115), (955, 116), (954, 116), (952, 118), (951, 118), (950, 120), (948, 120), (942, 127), (941, 127), (932, 137), (932, 139), (930, 140), (930, 142), (929, 144), (929, 147), (928, 149), (928, 152), (926, 154), (926, 163), (925, 164), (925, 173), (923, 175), (923, 182), (922, 183), (922, 188), (921, 190), (921, 195), (919, 197), (919, 204), (918, 206), (918, 213), (916, 214), (916, 221), (915, 223), (915, 228), (914, 230), (914, 235), (912, 237), (912, 242), (910, 244), (910, 247), (909, 249), (909, 252), (908, 254), (908, 256), (907, 257), (907, 259), (905, 261), (905, 262), (903, 264), (903, 266), (901, 269), (901, 271), (899, 273), (899, 274), (898, 276), (898, 278), (896, 280), (896, 281), (893, 285), (893, 286), (892, 288), (892, 290), (889, 293), (889, 295), (880, 305), (879, 305), (875, 311), (873, 311), (872, 312), (871, 312), (867, 316), (865, 316), (864, 317), (862, 316), (860, 316), (858, 312), (856, 312), (855, 311), (853, 311), (852, 309), (848, 309), (846, 307), (836, 307), (835, 309), (833, 309), (832, 311), (829, 311), (828, 312), (823, 312), (822, 314), (819, 314), (817, 316), (816, 316), (815, 317), (813, 317), (810, 321), (809, 321), (805, 326), (803, 326), (801, 328), (799, 328), (797, 329), (796, 329), (794, 331), (793, 331), (792, 333), (790, 333), (787, 336), (786, 336), (785, 338), (781, 338), (780, 340), (779, 338), (773, 338), (772, 340), (758, 340), (757, 338), (724, 338), (723, 336), (703, 336), (701, 335), (695, 335), (694, 333), (691, 333), (690, 331), (688, 331), (687, 329), (684, 329), (683, 328), (681, 328), (680, 326), (678, 326), (677, 324), (676, 324), (664, 311), (664, 309), (663, 307), (663, 304), (661, 302), (661, 293), (660, 292), (660, 257), (661, 256), (661, 240), (663, 238), (663, 230), (664, 228), (664, 221), (665, 219), (665, 211), (667, 209), (667, 202), (668, 201), (668, 188), (670, 187), (670, 173), (671, 171), (671, 163), (670, 161), (670, 147), (671, 146), (674, 146), (676, 147), (678, 147), (680, 149), (681, 149), (683, 151), (686, 151), (686, 144), (687, 142), (687, 128), (686, 127), (686, 123), (684, 123), (683, 125), (681, 125), (680, 127), (678, 127), (677, 128), (674, 128), (674, 130), (672, 132), (671, 130), (668, 130), (667, 128), (665, 128), (661, 123), (661, 121), (656, 115), (654, 115), (652, 113), (650, 113), (645, 108), (644, 108), (642, 106), (641, 106), (640, 104), (637, 104), (635, 103), (628, 103), (627, 101), (622, 101), (621, 99), (614, 99), (613, 97), (585, 97), (584, 96)]


lake_mask_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
pygame.draw.polygon(lake_mask_surface, (255, 255, 255), lake_polygon)
lake_mask = pygame.mask.from_surface(lake_mask_surface)

def draw_reset_button():
    reset_radius, reset_center = 50, (screen_width - 70, screen_height - 70)
    pygame.draw.circle(screen, (255, 0, 0), reset_center, reset_radius)
    font_small = pygame.font.SysFont(font_name, 30)
    draw_text("Reset", font_small, (255, 255, 255), reset_center)
    return reset_center, reset_radius

def draw_home_screen():
    screen.fill((70, 130, 180))
    pygame.draw.polygon(screen, (150, 255, 150), lake_polygon)  # Draw lake for debug
    # DEBUG TEXT: remove this after you see the lake!
    font_debug = pygame.font.SysFont(font_name, 40)
    screen.blit(font_debug.render("Debug Lake Visible", True, (0,0,0)), (screen_width//2-180, 20))

    title_font = pygame.font.SysFont(font_name, 80, bold=True)
    title_text = title_font.render("Protect Our Lakes From Carp!", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))
    screen.blit(title_text, title_rect)

    desc_font = pygame.font.SysFont(font_name, 40)
    desc_text = desc_font.render("An Interactive Game Modeling Westlake, Sacramento", True, (255, 255, 255))
    desc_rect = desc_text.get_rect(center=(screen_width // 2, screen_height // 4 + 100))
    screen.blit(desc_text, desc_rect)

    button_font = pygame.font.SysFont(font_name, 50)
    button_text = button_font.render("START", True, (255, 255, 255))
    button_rect = button_text.get_rect(center=(screen_width // 2, screen_height // 1.5))

    pygame.draw.rect(screen, (0, 100, 0), button_rect.inflate(40, 20), border_radius=10)
    screen.blit(button_text, button_rect)

    return button_rect

class Fish:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/carp.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(225 * 0.6), int(100 * 0.6)))
        self.rect = self.image.get_rect(center=(x, y))
        while True:
            self.vx = random.choice([-5, -4, -3, 3, 4, 5])
            self.vy = random.choice([-5, -4, -3, 3, 4, 5])
            if self.vx != 0 or self.vy != 0:
                break

    def draw(self):
        screen.blit(self.image, self.rect)

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

    def distance_to(self, other):
        return math.hypot(self.rect.centerx - other.rect.centerx, self.rect.centery - other.rect.centery)

    def move(self, lake_mask):
        stuck_frames = getattr(self, 'stuck_frames', 0)
        new_x = self.rect.centerx + self.vx
        new_y = self.rect.centery + self.vy
        fish_points = [
            (new_x, new_y),
            (new_x - self.rect.width // 2, new_y - self.rect.height // 2),
            (new_x + self.rect.width // 2, new_y - self.rect.height // 2),
            (new_x - self.rect.width // 2, new_y + self.rect.height // 2),
            (new_x + self.rect.width // 2, new_y + self.rect.height // 2)
        ]
        if all(lake_mask.get_at((x, y)) for x, y in fish_points if 0 <= x < screen_width and 0 <= y < screen_height):
            self.rect.centerx = new_x
            self.rect.centery = new_y
            self.stuck_frames = 0
        else:
            self.vx = random.choice([-5, -4, -3, 3, 4, 5])
            self.vy = random.choice([-5, -4, -3, 3, 4, 5])
            self.stuck_frames = stuck_frames + 1
            if self.stuck_frames > 30:
                spawn_attempts = 0
                while spawn_attempts < 100:
                    x, y = random.randint(0, screen_width - 1), random.randint(0, screen_height - 1)
                    fish_points = [
                        (x, y),
                        (x - self.rect.width // 2, y - self.rect.height // 2),
                        (x + self.rect.width // 2, y - self.rect.height // 2),
                        (x - self.rect.width // 2, y + self.rect.height // 2),
                        (x + self.rect.width // 2, y + self.rect.height // 2)
                    ]
                    if all(lake_mask.get_at((px, py)) for (px, py) in fish_points if 0 <= px < screen_width and 0 <= py < screen_height):
                        self.rect.center = (x, y)
                        break
                    spawn_attempts += 1
                self.stuck_frames = 0

fish_group, num_fish = [], 8
fish_distance = 150

def valid_location(new):
    return all(new.distance_to(f) >= fish_distance for f in fish_group)

def create_fish_group():
    global fish_group, num_fish, initial_fish_count
    num_fish = carp_options[current_carp_index]
    initial_fish_count = num_fish
    fish_group = []

    for _ in range(num_fish):
        spawn_attempts = 0
        while spawn_attempts < 100:
            x, y = random.randint(0, screen_width - 1), random.randint(0, screen_height - 1)
            new = Fish(x, y)
            fish_points = [
                (x, y),
                (x - new.rect.width // 2, y - new.rect.height // 2),
                (x + new.rect.width // 2, y - new.rect.height // 2),
                (x - new.rect.width // 2, y + new.rect.height // 2),
                (x + new.rect.width // 2, y + new.rect.height // 2)
            ]
            if all(lake_mask.get_at((px, py)) for (px, py) in fish_points if 0 <= px < screen_width and 0 <= py < screen_height):
                if valid_location(new):
                    fish_group.append(new)
                    break
            spawn_attempts += 1

create_fish_group()

start_time = end_time = elapsed_time = personal_best_time = None

def remove_fish(pos):
    global start_time, end_time, elapsed_time, personal_best_time
    for f in fish_group:
        if f.clicked(pos):
            fish_group.remove(f)
            if start_time is None:
                start_time = time.time()
            if not fish_group:
                end_time = time.time()
                elapsed_time = end_time - start_time
                if personal_best_time is None or elapsed_time < personal_best_time:
                    personal_best_time = elapsed_time
            break

def reset_game():
    global start_time, end_time, elapsed_time
    create_fish_group()
    start_time = end_time = elapsed_time = None

def reset_best_time():
    global personal_best_time
    personal_best_time = None

def interpolate_color(start, end, t):
    t = max(0.0, min(1.0, t))
    sharp_t = t ** 0.5
    return tuple(int(start[i] + (end[i] - start[i]) * sharp_t) for i in range(3))

def draw_text(text, font, color, center):
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=center)
    screen.blit(surf, rect)
    return rect

def draw_main_page():
    global elapsed_time
    screen.fill(background_color)

    fish_removed = initial_fish_count - len(fish_group)
    percent_per_carp = 10
    clarity_improvement = fish_removed * percent_per_carp
    clarity_improvement = min(clarity_improvement, 100)

    lake_color = interpolate_color(murky_green, baby_blue, clarity_improvement / 100)
    pygame.draw.polygon(screen, lake_color, lake_polygon)

    for f in fish_group:
        f.move(lake_mask)
        f.draw()

    font_large = pygame.font.SysFont(font_name, 55)
    font_small = pygame.font.SysFont(font_name, 30)
    draw_text("Adi Parekh", font_large, text_color, (150, screen_height - 40))

    reset_radius, reset_center = 50, (screen_width - 70, screen_height - 70)
    pygame.draw.circle(screen, (255, 0, 0), reset_center, reset_radius)
    draw_text("Reset", font_small, (255, 255, 255), reset_center)

    info_font = pygame.font.SysFont(font_name, 28)
    pad = 20
    info_text = info_font.render("More Info About Carp", True, (255, 255, 255))
    info_rect = pygame.Rect(20, 20, info_text.get_width() + pad, info_text.get_height() + pad)
    pygame.draw.rect(screen, (0, 100, 0), info_rect)
    screen.blit(info_text, (info_rect.x + pad // 2, info_rect.y + pad // 2))

    carp_font = pygame.font.SysFont(font_name, 28)
    carp_text = carp_font.render(f"Carp: {num_fish}", True, (255, 255, 255))
    carp_rect = pygame.Rect(screen_width - 200, 20, 180, 40)
    pygame.draw.rect(screen, (0, 100, 0), carp_rect)
    screen.blit(carp_text, (carp_rect.x + 10, carp_rect.y + 5))

    time_x = screen_width - 350
    time_y_base = screen_height - 120
    if start_time and not end_time:
        elapsed_time = time.time() - start_time
    if elapsed_time:
        draw_text(f"Time: {elapsed_time:.2f} s", font_small, text_color, (time_x, time_y_base))
    if personal_best_time:
        draw_text(f"Best Time: {personal_best_time:.2f} s", font_small, text_color, (time_x, time_y_base + 40))

    if not fish_group:
        mid_x, mid_y = screen_width // 2, screen_height // 2
        draw_text(f"You've removed {fish_removed} invasive carp!", font_large, text_color, (mid_x, mid_y - 40))
        draw_text(f"Water clarity improved by ~{clarity_improvement:.1f}%!", font_large, text_color, (mid_x, mid_y + 40))

    return reset_center, reset_radius, info_rect, carp_rect

def draw_more_info_page(scroll_offset=0):
    screen.fill((139, 94, 60))
    container_width = screen_width - 100
    container_height = screen_height * 2
    container = pygame.Surface((container_width, container_height))
    container.fill((255, 255, 255))
    lines = [
    "Growing up in Westlake, California, I've always had a special connection with our community lake.",
    "From the moment I learned how to hold a fishing rod, weekend mornings by the lake became my favorite tradition.",
    "My friends and I would wake up early, the sky still tinted pink with dawn, and rush down to the water’s edge.",
    "Those peaceful mornings, with rods in hand and the sound of water lapping gently at the shore, became the background music of my childhood.",
    "",
    "Over time, I began noticing changes in our beloved lake.",
    "The clear, shimmering water slowly turned murky, and the vibrant underwater plants started disappearing.",
    "Fishing, once a joy, became increasingly frustrating as the catches dwindled.",
    "It wasn’t until I did a bit of research that I discovered the culprits behind this drastic transformation—carp.",
    "",
    "Carp, specifically invasive species like common carp, have been silently wreaking havoc beneath the surface of our waters.",
    "These fish, originally introduced from Europe and Asia, may seem harmless or even beneficial at first glance.",
    "They grow quickly, reproduce rapidly, and can survive in various conditions.",
    "However, this resilience makes them exceptionally dangerous for delicate ecosystems like our lake in Westlake.",
    "",
    "Driven by curiosity and concern, I delved deeper into understanding the problem.",
    "I spent countless hours researching scientific articles, local ecological studies, and even reaching out to wildlife experts.",
    "The more I learned, the more worried I became.",
    "Carp are bottom feeders; they stir up the sediment at the bottom of lakes while searching for food.",
    "This simple action releases phosphorus and nitrogen into the water, nutrients that significantly accelerate algae growth.",
    "Excessive algae cloud the water, blocking sunlight necessary for aquatic plants to grow and reducing oxygen levels.",
    "This creates a 'dead zone' where most fish species, including the ones I used to catch and release with excitement, cannot survive.",
    "",
    "My research revealed startling statistics from similar communities facing the same issue.",
    "Lakes invaded by carp had lost most of their native fish populations, drastically affecting local wildlife and recreational activities.",
    "The economic impact, too, was significant, with towns having to spend substantial sums on lake restoration projects.",
    "",
    "Armed with knowledge and a sense of urgency, I wondered what I could do to help my own community.",
    "Awareness seemed to be the first logical step.",
    "If people understood the severity of the issue, perhaps they’d feel inspired to take action.",
    "But pamphlets and posters didn’t seem impactful enough.",
    "I wanted something interactive—something that would resonate with both kids and adults, something informative yet engaging.",
    "And that's when I had the idea of creating a game.",
    "",
    "My interactive game, 'Carp Cleanup,' allows players to experience firsthand the impact carp have on our lakes.",
    "As the game progresses, the lake transforms from murky green back to its original clear, vibrant state, mirroring the impact of removing carp from real lakes.",
    "The gameplay involves catching carp, each removal symbolizing a step towards restoration.",
    "I included facts about carp’s environmental effects at different points in the game to educate players, hoping to foster a deeper understanding of the issue.",
    "",
    "Creating the game was more than just a technical project—it became personal.",
    "Every line of code reminded me of sunny afternoons spent beside our lake.",
    "Every carp removed in-game represented a memory I wanted to preserve and restore in reality.",
    "The significance was not lost on me.",
    "This wasn't just a fun pastime; it was my small contribution toward preserving our community's cherished ecosystem.",
    "",
    "Through this project, my goal is not only to educate but also to inspire action within our community.",
    "I dream of returning our lake to the beautiful, lively place it once was—a place where future generations can experience the simple joys of fishing or just sitting by clear waters, watching fish dart beneath the surface.",
    "I believe that by raising awareness and encouraging active participation through my game, we can collectively make a difference.",
    "",
    "The issue of invasive carp is not one that can be solved overnight, but together, our community can take steps toward restoration.",
    "Westlake, with its beautiful lakes and rich natural surroundings, deserves our attention and care.",
    "It’s my hope that through understanding and action, we can reclaim the pristine waters and thriving wildlife that once defined our beloved lake."
    ]
    font = pygame.font.SysFont(font_name, 26)
    line_height = font.get_linesize()
    text_x, text_y = 20, 20
    for line in lines:
        text_surface = font.render(line, True, (0, 0, 0))
        container.blit(text_surface, (text_x, text_y))
        text_y += line_height + 5

    screen.blit(container, (50, 50), area=pygame.Rect(0, scroll_offset, container_width, screen_height - 100))
    back_rect = pygame.Rect(screen_width - 170, 20, 150, 60)
    pygame.draw.rect(screen, (0, 100, 0), back_rect)
    back_text = font.render("Back", True, (255, 255, 255))
    screen.blit(back_text, (back_rect.x + 20, back_rect.y + 15))
    return back_rect

running, current_page = True, "home"

async def main():
    global running, current_page, start_time, elapsed_time, num_fish, current_carp_index
    running, current_page = True, "home"
    clock = pygame.time.Clock()
    scroll_offset = 0
    scroll_speed = 20

    while running:
        mouse_clicked, mouse_pos = False, (0, 0)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_clicked, mouse_pos = True, e.pos
                elif e.button == 4:
                    scroll_offset = max(0, scroll_offset - scroll_speed)
                elif e.button == 5:
                    scroll_offset += scroll_speed

        if current_page == "home":
            start_button = draw_home_screen()
            if mouse_clicked and start_button.collidepoint(mouse_pos):
                current_page = "main"
                start_time = time.time()
        elif current_page == "main":
            reset_center, reset_radius, info_rect, carp_rect = draw_main_page()
            carp_dropdown_rect = pygame.Rect(screen_width - 200, 20, 150, 40)
            pygame.draw.rect(screen, (0, 100, 0), carp_dropdown_rect)
            dropdown_text = pygame.font.SysFont(font_name, 24).render(f"Carp: {carp_options[current_carp_index]}", True, (255, 255, 255))
            screen.blit(dropdown_text, (carp_dropdown_rect.x + 10, carp_dropdown_rect.y + 10))
            if mouse_clicked:
                if math.hypot(mouse_pos[0] - reset_center[0], mouse_pos[1] - reset_center[1]) <= reset_radius:
                    reset_game()
                elif info_rect.collidepoint(mouse_pos):
                    current_page = "more_info"
                elif carp_dropdown_rect.collidepoint(mouse_pos):
                    current_carp_index = (current_carp_index + 1) % len(carp_options)
                    num_fish = carp_options[current_carp_index]
                    create_fish_group()
                    reset_best_time()
                elif lake_mask.get_at(mouse_pos):
                    remove_fish(mouse_pos)
        elif current_page == "more_info":
            back_rect = draw_more_info_page(scroll_offset)
            if mouse_clicked and back_rect.collidepoint(mouse_pos):
                current_page = "main"
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())
pygame.quit()
# No sys.exit() for pygbag/web
