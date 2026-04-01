import pygame

def dibujar_boton(ventana, texto,x,y,ancho,alto,color,color_texto=(0,0,0)):
    rect = pygame.Rect(x,y,ancho,alto)
    pygame.draw.rect(ventana,color,rect,border_radius=8)
    pygame.draw.rect(ventana, (80, 80, 80), rect, 2, border_radius=8)

    fuente = pygame.font.SysFont("Arial", 20)
    label = fuente.render(texto, True, color_texto)

    texto_x = x + (ancho - label.get_width()) // 2
    texto_y = y + (alto - label.get_height()) // 2
    ventana.blit(label, (texto_x, texto_y))
    
    return rect

def mostrar_menu(ventana,ancho,alto):
    fuente_titulo = pygame.font.SysFont("Arial",28, bold =True)
    
    ejecutando = True

    while ejecutando:
        ventana.fill((240,240,240)) #fondo gris claro

        #titulo

        titulo = fuente_titulo.render("Selecciona el tipo de búsqueda", True, (30,30,30))

        ventana.blit(titulo,(ancho // 2 - titulo.get_width() // 2, 80))
        
        
        btn_no_inf = dibujar_boton(ventana, "No Informada", (ancho // 2 - 200 // 2),200, 200, 50, (100, 149, 237), (255,255,255))
        btn_inf    = dibujar_boton(ventana, "Informada",  (ancho // 2 - 200 // 2),280 , 200, 50, (60,  179, 113), (255,255,255))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_no_inf.collidepoint(event.pos):
                    return "no_informada"
                if btn_inf.collidepoint(event.pos):
                    return "informada"
def mostrar_submenu(ventana, ancho, alto, categoria):
    fuente_titulo = pygame.font.SysFont("Arial", 24, bold=True)

    if categoria == "no_informada":
        opciones = [
            ("Amplitud",   "amplitud"),
            ("Costo Uniforme", "costo"),
            ("Profundidad", "profundidad"),
        ]
    else:
        opciones = [
            ("Avara",  "avara"),
            ("A*",     "a_estrella"),
        ]

    ejecutando = True
    while ejecutando:
        ventana.fill((240, 240, 240))

        titulo = fuente_titulo.render("Selecciona el algoritmo", True, (30, 30, 30))
        ventana.blit(titulo, (ancho // 2 - titulo.get_width() // 2, 80))

        botones = []
        for idx, (texto, clave) in enumerate(opciones):
            btn = dibujar_boton(ventana, texto,
                                ancho // 2 - 100,
                                180 + idx * 80,   # separados 80px entre sí
                                200, 50, (70, 130, 180), (255, 255, 255))
            botones.append((btn, clave))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn, clave in botones:
                    if btn.collidepoint(event.pos):
                        return clave