
class Color_theme_wb:
    opacity_black = 0.7
    opacity_white = 0.9
    background_white =  "white"
    background_black =  "black"
    theme_color_black = [[44, 52, 55], [237, 237, 237]]
    theme_color_white = [[44, 52, 55], [44, 52, 55]]
    sqare_colors_black = [[5, 2, 2], [198, 228, 139], [123, 201, 111], [35, 154, 59], [25, 97, 39]]
    sqare_colors_white = [[235, 237, 240], [198, 228, 139], [123, 201, 111], [35, 154, 59], [25, 97, 39]]

    def convert_to_RGB(self, array) -> str:
        strs_font = " rgb(" + str(array[0]) + \
                    ", " + str(array[1]) + \
                    ", " + str(array[2]) + "); "

        return strs_font