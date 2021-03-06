from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0,255,255 ]

# test matrix functions
m1 = new_matrix()
m2 = new_matrix(cols=0)
print("Testing add_edge... adding (1, 2, 3), (4, 5, 6). m2 =")
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)

print("Testing ident... m1 =")
ident(m1)
print_matrix(m1)

print("Testing matrix_mult... m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)

m1 = new_matrix(cols=0)
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print("Testing add_edge... m1 =")
print_matrix(m1)

print("Testing matrix_mult... m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)

# make piano image
edges = new_matrix(cols=0)

# legs
add_edge(edges, 40, 60, 0, 40, 230, 0)
add_edge(edges, 40, 60, 0, 50, 57, 0)
add_edge(edges, 50, 57, 0, 50, 227, 0)
add_edge(edges, 50, 57, 0, 55, 60, 0)
add_edge(edges, 55, 60, 0, 55, 195, 0)
add_edge(edges, 50, 227, 0, 40, 230, 0)
add_edge(edges, 300, 180, 0, 300, 10, 0)
add_edge(edges, 290, 183, 0, 290, 13, 0)
add_edge(edges, 290, 183, 0, 290, 13, 0)
add_edge(edges, 290, 13, 0, 300, 10, 0)
add_edge(edges, 300, 10, 0, 305, 13, 0)
add_edge(edges, 305, 13, 0, 305, 153, 0)

# keyboard
add_edge(edges, 50, 207, 0, 290, 163, 0)
add_edge(edges, 50, 200, 0, 290, 156, 0)
add_edge(edges, 50, 197, 0, 290, 153, 0)
add_edge(edges, 300, 150, 0, 350, 175, 0)
add_edge(edges, 300, 180, 0, 350, 205, 0)
add_edge(edges, 350, 205, 0, 340, 208, 0)
add_edge(edges, 300, 180, 0, 290, 183, 0)
add_edge(edges, 290, 183, 0, 340, 208, 0)
add_edge(edges, 110, 231, 0, 50, 207, 0)
add_edge(edges, 50, 227, 0, 110, 251, 0)
add_edge(edges, 40, 230, 0, 100, 255, 0)
add_edge(edges, 100, 255, 0, 110, 251, 0)

# back
add_edge(edges, 350, 285, 0, 350, 35, 0)
add_edge(edges, 310, 195, 0, 110, 231, 0)
add_edge(edges, 110, 79, 0, 198, 63, 0)
add_edge(edges, 208, 62, 0, 213, 61, 0)
add_edge(edges, 223, 59, 0, 228, 58, 0)
add_edge(edges, 243, 56, 0, 290, 46, 0)
add_edge(edges, 305, 42, 0, 350, 35, 0)
add_edge(edges, 110, 79, 0, 110, 185, 0)
add_edge(edges, 110, 231, 0, 110, 329, 0)
add_edge(edges, 350, 35, 0, 400, 60, 0)
add_edge(edges, 400, 60, 0, 400, 305, 0)

# lid
add_edge(edges, 105, 330, 0, 355, 284, 0)
add_edge(edges, 105, 330, 0, 105, 340, 0)
add_edge(edges, 355, 284, 0, 355, 294, 0)
add_edge(edges, 355, 284, 0, 405, 309, 0)
add_edge(edges, 105, 340, 0, 155, 365, 0)
add_edge(edges, 105, 340, 0, 355, 294, 0)
add_edge(edges, 355, 294, 0, 405, 319, 0)
add_edge(edges, 405, 319, 0, 405, 309, 0)
add_edge(edges, 405, 319, 0, 155, 365, 0)

# pedals
add_edge(edges, 250, 61, 0, 225, 49, 0)
add_edge(edges, 240, 63, 0, 215, 50, 0)
add_edge(edges, 235, 64, 0, 210, 51, 0)
add_edge(edges, 225, 66, 0, 200, 53, 0)
add_edge(edges, 220, 67, 0, 195, 54, 0)
add_edge(edges, 210, 69, 0, 185, 56, 0)
add_edge(edges, 225, 49, 0, 215, 50, 0)
add_edge(edges, 210, 51, 0, 200, 53, 0)
add_edge(edges, 195, 54, 0, 185, 56, 0)

# keys
add_edge(edges, 115, 229, 0, 90, 218, 0)
add_edge(edges, 125, 227, 0, 100, 217, 0)
add_edge(edges, 135, 225, 0, 110, 214, 0)
add_edge(edges, 165, 220, 0, 140, 209, 0)
add_edge(edges, 175, 218, 0, 150, 207, 0)
add_edge(edges, 205, 213, 0, 180, 202, 0)
add_edge(edges, 215, 211, 0, 190, 200, 0)
add_edge(edges, 225, 209, 0, 200, 198, 0)
add_edge(edges, 255, 204, 0, 230, 193, 0)
add_edge(edges, 265, 202, 0, 240, 191, 0)
add_edge(edges, 295, 197, 0, 270, 186, 0)
add_edge(edges, 305, 195, 0, 280, 184, 0)

# stand
add_edge(edges, 150, 250, 0, 200, 241, 0)
add_edge(edges, 250, 232, 0, 315, 220, 0)
add_edge(edges, 315, 220, 0, 305, 215, 0)
add_edge(edges, 150, 250, 0, 140, 245, 0)
add_edge(edges, 140, 245, 0, 305, 215, 0)
add_edge(edges, 200, 238, 0, 200, 300, 0)
add_edge(edges, 200, 238, 0, 250, 230, 0)
add_edge(edges, 250, 230, 0, 250, 290, 0)
add_edge(edges, 250, 290, 0, 200, 300, 0)

shift(edges, 30, 60)

draw_lines(edges, screen, color )

save_ppm_ascii(screen, 'pic1.ppm')
save_extension(screen, 'piano.png')

# make face image to display
screen = new_screen()
color = [ 255,0,255 ]

edges = new_matrix(cols=0)

add_edge(edges, 50, 450, 0, 100, 450, 0)
add_edge(edges, 50, 450, 0, 50, 400, 0)
add_edge(edges, 100, 450, 0, 100, 400, 0)
add_edge(edges, 100, 400, 0, 50, 400, 0)

add_edge(edges, 200, 450, 0, 250, 450, 0)
add_edge(edges, 200, 450, 0, 200, 400, 0)
add_edge(edges, 250, 450, 0, 250, 400, 0)
add_edge(edges, 250, 400, 0, 200, 400, 0)

add_edge(edges, 150, 400, 0, 130, 360, 0)
add_edge(edges, 150, 400, 0, 170, 360, 0)
add_edge(edges, 130, 360, 0, 170, 360, 0)

add_edge(edges, 100, 340, 0, 200, 340, 0)
add_edge(edges, 100, 320, 0, 200, 320, 0)
add_edge(edges, 100, 340, 0, 100, 320, 0)
add_edge(edges, 200, 340, 0, 200, 320, 0)

draw_lines(edges, screen, color )

save_ppm_ascii(screen, 'pic2.ppm')
save_extension(screen, 'face.png')
display(screen)
