from PIL import Image, ImageFilter

#Ler imagem
im = Image.open( './images/eu.jpg' )

#Convertento imagem em tons de cinza
shade_gray = im.convert('L')

#Aplicando um filtros à imagem
blur = shade_gray.filter( ImageFilter.BLUR )
blur_kernel = blur.filter( ImageFilter.Kernel((3,3), (1,1,1,1,1,1,1,1,1),1,0) ) 

find_edhes = shade_gray.filter( ImageFilter.FIND_EDGES )
find_edhes_kernel = find_edhes.filter( ImageFilter.Kernel((3,3), (1,0,-1,2,0,-2,1,0,-1), 1, 0) )

sharpen = shade_gray.filter( ImageFilter.SHARPEN )
sharpen_kernel = sharpen.filter( ImageFilter.Kernel((3,3), (1,2,1,0,0,0,-1,-2,-1),1,0) )

#Salvando a imagem filtradas
blur_kernel.save( './images/image_blur.jpg', 'JPEG' )
sharpen_kernel.save( './images/image_sharpened.jpg', 'JPEG' )
find_edhes_kernel.save('./images/image_find_edhes.jpg', 'JPEG')