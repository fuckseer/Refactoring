from PIL import Image
import numpy as np
import doctest


def convert_image_to_mosaic ( image , size , gradation_step ) :
    """

        Convert image to mosaic
        param image: needed image
        param size: block size mosaic
        param gradation_step: gradation of gray
        return image
        >>> convert_image_to_mosaic((np.ones((3, 3, 3)) * 200), 2, 15)
        array([[[195., 195., 195.],
            [195., 195., 195.],
            [ 90.,  90.,  90.]],
        <BLANKLINE>
           [[195., 195., 195.],
            [195., 195., 195.],
            [ 90.,  90.,  90.]],
        <BLANKLINE>
           [[ 90.,  90.,  90.],
            [ 90.,  90.,  90.],
            [ 45.,  45.,  45.]]])

    """
    for x in range ( 0 , len ( image ) , size ) :
        for y in range ( 0 , len ( image [ 0 ] ) , size ) :
            image [ x :x + size , y :y + size ] = get_average_brightness (
                image [ x :x + size , y :y + size ] , size , gradation_step )
    return image


def get_average_brightness ( block , size , gradation_step ) :
    """
    Get average brightness of image
    param block: mosaic block size
    param size: size
    param gradation_step: gradation of gray
    return int
     >>> get_average_brightness(np.ones((3, 3, 3)) * 200, 2, 15)
     195

    >>> get_average_brightness(np.ones((3, 3, 3)) * 100, 2, 15)
    90

    >>> get_average_brightness(np.ones((3, 3, 3)) * 100, 6, 6)
    24

    >>> get_average_brightness(np.ones((10, 10, 3)) * 100, 6, 6)
    96
    """

    average_color = (block [ :size , :size ].sum () / 3) // size ** 2
    res = int ( average_color // gradation_step ) * gradation_step
    return res


def main () :
    image_file = Image.open ( input ( "Введите имя файла, которое хотите конвертировать: " ) )
    block_size = int ( input ( "Введите размер блока: " ) )
    gradations_count = int ( input ( "Введите количество градаций серого: " ) )
    image = np.array ( image_file )
    gradation_step = 255 // gradations_count

    res = Image.fromarray ( convert_image_to_mosaic ( image , block_size , gradation_step ) )
    res.save ( input ( "Введите имя файла, в которой хотите сохранить результат: " ) )


if __name__ == '__main__' :
    doctest.testmod ()
    main ()
