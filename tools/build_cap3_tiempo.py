#!/usr/bin/env python3
"""Construye el cap 3 «Tiempo» de Principios Económicos.

Cap con 5 figuras adaptadas a la paleta del libro (SVG inline):
  Fig 2: cancha de fútbol + escritorio    (escala superficie Tierra / minas)
  Fig 3: alberca olímpica + vaso de agua  (escala volumen Tierra / minas)
  Fig 4: barras de 50 productos básicos   (variación precio + abundancia)
  Fig 5: petróleo 1980-2020               (consumo vs reservas)
  Fig 6: oro 1900-2020                    (reservas totales + crecimiento %)

Sin notas al pie.
"""
import re

EYEBROW = "Parte I · Fundamentos"
TITLE = "Tiempo"
SUBTITLE = "Saifedean Ammous — Principios de Economía"


# ===================== FIGURAS SVG =====================

def fig2_cancha_escritorio():
    """Cancha de fútbol 105×68 con escritorio 1.22×0.61 como escala.
    No es dato, es ilustración: proporciones reales, colores del libro."""
    return '''<svg class="scale-fig" viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cancha de fútbol con un escritorio pequeño a escala">
  <!-- CANCHA (105 x 68, ratio 1.544) -->
  <g transform="translate(60,20)">
    <rect x="0" y="0" width="600" height="252" class="field"/>
    <line x1="300" y1="0" x2="300" y2="252" class="field-line"/>
    <circle cx="300" cy="126" r="34" class="field-line" fill="none"/>
    <circle cx="300" cy="126" r="3" class="field-dot"/>
    <rect x="0" y="52" width="70" height="148" class="field-line" fill="none"/>
    <rect x="0" y="92" width="24" height="68" class="field-line" fill="none"/>
    <rect x="530" y="52" width="70" height="148" class="field-line" fill="none"/>
    <rect x="576" y="92" width="24" height="68" class="field-line" fill="none"/>
    <text x="300" y="-6" class="dim" text-anchor="middle">105 m</text>
    <text x="614" y="130" class="dim">68 m</text>
  </g>
  <!-- ESCRITORIO (122 x 61 cm, ratio 2.0) — minúsculo al pie -->
  <g transform="translate(305,295)">
    <rect x="0" y="0" width="22" height="11" class="desk"/>
    <line x1="2"  y1="11" x2="2"  y2="18" class="desk-leg"/>
    <line x1="20" y1="11" x2="20" y2="18" class="desk-leg"/>
    <text x="-6" y="7" class="dim-small" text-anchor="end">1.22 m</text>
    <text x="28" y="7" class="dim-small">0.61 m</text>
  </g>
</svg>'''


def fig3_alberca_vaso():
    """Alberca olímpica 50×25 (10 carriles) + vaso de agua al pie.
    Escala volumen Tierra / volumen de todas las minas."""
    return '''<svg class="scale-fig" viewBox="0 0 720 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Alberca olímpica con un vaso de agua al pie como escala">
  <g transform="translate(90,20)">
    <!-- borde azul oscuro -->
    <rect x="0" y="0" width="540" height="252" class="pool-edge"/>
    <!-- agua -->
    <rect x="10" y="10" width="520" height="232" class="pool-water"/>
    <!-- carriles -->
    <g class="pool-lane">
      ''' + ''.join(
          f'<line x1="10" y1="{10 + i * 232/10}" x2="530" y2="{10 + i * 232/10}"/>'
          for i in range(1, 10)
      ) + '''
    </g>
    <text x="270" y="-6" class="dim" text-anchor="middle">50 m</text>
  </g>
  <!-- Vaso de agua con lupa (muy chico) -->
  <g transform="translate(330,290)">
    <circle cx="0" cy="0" r="14" class="lens" fill="none"/>
    <rect x="-4" y="-5" width="8" height="10" class="glass-outline" fill="none"/>
    <rect x="-3" y="-1" width="6" height="5" class="glass-water"/>
  </g>
</svg>'''


# Datos extraídos de la figura 4 del libro, en el mismo orden.
COMMODITIES = [
    ("Azúcar", -86.2, 7.25), ("Cuero", -86.2, 7.23), ("Carne de cerdo", -86.1, 7.20),
    ("Café", -85.9, 7.11), ("Salmón", -85.1, 6.72), ("Gas Natural, UE", -85.0, 6.68),
    ("Algodón", -85.0, 6.65), ("Cacahuate", -83.0, 5.89), ("Cacao", -82.2, 5.63),
    ("Uranio", -82.0, 5.54), ("Aluminio", -81.3, 5.34), ("Carne de cordero", -81.1, 5.30),
    ("Plata", -80.7, 5.19), ("Estaño", -80.1, 5.03), ("Petróleo crudo", -78.2, 4.58),
    ("Arroz", -76.4, 4.24), ("Caucho", -76.3, 4.21), ("Trigo", -76.1, 4.18),
    ("Cebada", -75.7, 4.11), ("Camarones", -75.6, 4.11), ("Gas natural, EEUU", -75.2, 4.04),
    ("PROMEDIO", -75.2, 4.03), ("Aceite palma", -74.8, 3.97), ("Platino", -74.6, 3.94),
    ("Madera para pulpa", -74.5, 3.93), ("Maíz", -74.2, 3.88), ("Sorgo", -74.0, 3.85),
    ("Soja", -72.4, 3.62), ("GNL, Japón", -71.6, 3.52), ("Fertilizante", -71.6, 3.52),
    ("Aceite de coco", -70.8, 3.42), ("Naranja", -70.8, 3.42), ("Carbón", -70.5, 3.39),
    ("Troncos", -70.4, 3.38), ("Canola", -69.9, 3.32), ("Lana", -69.7, 3.30),
    ("Té", -68.3, 3.15), ("Madera aserrada", -67.6, 3.09), ("Carne de res", -67.0, 3.03),
    ("Madera terciada", -63.6, 2.75), ("Aceite de girasol", -63.0, 2.70), ("Tabaco", -62.5, 2.67),
    ("Plomo", -60.7, 2.55), ("Níquel", -58.8, 2.43), ("Carne de pollo", -58.2, 2.39),
    ("Cobre", -44.8, 1.81), ("Harina de pescado", -44.6, 1.81), ("Oro", -43.2, 1.76),
    ("Zinc", -42.0, 1.72), ("Plátano", -37.5, 1.60), ("Mineral de hierro", -24.4, 1.32),
]


def fig4_commodities():
    """50 productos en 2 columnas con 2 mini-barras (precio / abundancia)."""
    rows_per_col = 26
    row_h = 14
    label_w = 110
    bar_w = 55   # cada barra, ancho máximo
    name_pad = 8
    col_w = label_w + bar_w * 2 + 10 + 10
    col_gap = 20
    total_w = col_w * 2 + col_gap + 20
    header_h = 32
    total_h = header_h + rows_per_col * row_h + 24

    MAX_PCT = 100.0   # eje de precio (todas las %<100)
    MAX_MUL = 8.0     # eje de multiplicador (máx real 7.25)

    def render_row(name, pct, mul, x, y, highlight=False):
        pct_bar_w = (abs(pct) / MAX_PCT) * bar_w
        mul_bar_w = (mul / MAX_MUL) * bar_w
        cls = "row-name hl" if highlight else "row-name"
        return (
            f'<text x="{x + label_w - name_pad}" y="{y + row_h*0.72:.1f}" class="{cls}" text-anchor="end">{name}</text>'
            # barra precio (negativa, crece hacia la izquierda del eje medio)
            f'<rect x="{x + label_w + (bar_w - pct_bar_w):.1f}" y="{y + 2}" width="{pct_bar_w:.1f}" height="{row_h - 4}" class="bar-neg"/>'
            f'<text x="{x + label_w + bar_w - pct_bar_w - 4:.1f}" y="{y + row_h*0.72:.1f}" class="row-val" text-anchor="end">{pct:.1f}%</text>'
            # separador leve entre las dos barras
            f'<line x1="{x + label_w + bar_w + 4}" y1="{y + 2}" x2="{x + label_w + bar_w + 4}" y2="{y + row_h - 2}" class="row-sep"/>'
            # barra abundancia (positiva, crece hacia la derecha)
            f'<rect x="{x + label_w + bar_w + 8:.1f}" y="{y + 2}" width="{mul_bar_w:.1f}" height="{row_h - 4}" class="bar-pos"/>'
            f'<text x="{x + label_w + bar_w + 8 + mul_bar_w + 4:.1f}" y="{y + row_h*0.72:.1f}" class="row-val">{mul:.2f}×</text>'
        )

    cells = []
    # cabecera de columnas
    for col in (0, 1):
        x = 10 + col * (col_w + col_gap)
        cells.append(f'<text x="{x + label_w - name_pad}" y="16" class="col-head" text-anchor="end">producto</text>')
        cells.append(f'<text x="{x + label_w + bar_w / 2:.1f}" y="16" class="col-head" text-anchor="middle">precio</text>')
        cells.append(f'<text x="{x + label_w + bar_w + 8 + bar_w / 2:.1f}" y="16" class="col-head" text-anchor="middle">abundancia</text>')

    col1 = COMMODITIES[:rows_per_col]
    col2 = COMMODITIES[rows_per_col:]
    for i, (name, pct, mul) in enumerate(col1):
        y = header_h + i * row_h
        hl = (name == "PROMEDIO")
        cells.append(render_row(name, pct, mul, 10, y, highlight=hl))
    for i, (name, pct, mul) in enumerate(col2):
        y = header_h + i * row_h
        cells.append(render_row(name, pct, mul, 10 + col_w + col_gap, y))

    return (
        f'<svg class="commodities-fig" viewBox="0 0 {total_w} {total_h}" '
        f'xmlns="http://www.w3.org/2000/svg" role="img" '
        f'aria-label="Variación de precio y multiplicador de abundancia de 50 productos básicos entre 1980 y 2020">'
        + ''.join(cells) +
        '</svg>'
    )


# Datos aproximados extraídos de la figura 5 del libro
OIL = [
    (1980, 20, 680), (1981, 21, 700), (1982, 21, 720), (1983, 21, 750),
    (1984, 22, 780), (1985, 22, 800), (1986, 22, 920), (1987, 23, 950),
    (1988, 24, 990), (1989, 24, 1020), (1990, 24, 1020), (1991, 24, 1035),
    (1992, 24, 1030), (1993, 24, 1030), (1994, 25, 1030), (1995, 25, 1040),
    (1996, 26, 1050), (1997, 26, 1060), (1998, 26, 1200), (1999, 26, 1210),
    (2000, 27, 1300), (2001, 27, 1320), (2002, 27, 1340), (2003, 28, 1350),
    (2004, 29, 1360), (2005, 29, 1380), (2006, 29, 1400), (2007, 29, 1420),
    (2008, 29, 1500), (2009, 29, 1530), (2010, 30, 1620), (2011, 30, 1650),
    (2012, 31, 1680), (2013, 31, 1690), (2014, 32, 1700), (2015, 32, 1700),
    (2016, 33, 1720), (2017, 33, 1725), (2018, 34, 1730), (2019, 34, 1740),
    (2020, 32, 1735),
]


def fig5_oil():
    """Líneas anuales: consumo total y reservas probadas (miles de millones de barriles)."""
    X0, X1 = 70, 690
    Y_TOP, Y_BOT = 30, 330
    YMAX = 1900
    sx = lambda yr: X0 + (yr - 1980) / (2020 - 1980) * (X1 - X0)
    sy = lambda v: Y_BOT - (v / YMAX) * (Y_BOT - Y_TOP)
    grid = ''.join(
        f'<line x1="{X0}" y1="{sy(v):.1f}" x2="{X1}" y2="{sy(v):.1f}" class="grid"/>'
        for v in range(500, 2000, 500)
    )
    axes = (
        f'<line x1="{X0}" y1="{Y_BOT}" x2="{X1}" y2="{Y_BOT}" class="axis"/>'
        f'<line x1="{X0}" y1="{Y_TOP}" x2="{X0}" y2="{Y_BOT}" class="axis"/>'
    )
    xlab = ''.join(
        f'<text x="{sx(y):.1f}" y="{Y_BOT + 18}" class="tick-label" text-anchor="middle">{y}</text>'
        for y in range(1980, 2021, 5)
    )
    ylab = ''.join(
        f'<text x="{X0 - 8}" y="{sy(v) + 4:.1f}" class="tick-label" text-anchor="end">{v}</text>'
        for v in (500, 1000, 1500)
    )
    res_pts = ' '.join(f'{sx(yr):.1f},{sy(r):.1f}' for yr, _, r in OIL)
    con_pts = ' '.join(f'{sx(yr):.1f},{sy(c):.1f}' for yr, c, _ in OIL)
    legend = (
        f'<g transform="translate({X0 + 20},{Y_TOP + 10})">'
        f'<line x1="0" y1="6" x2="22" y2="6" class="line-reserves"/>'
        f'<text x="28" y="10" class="legend-text">Reservas probadas</text>'
        f'<line x1="170" y1="6" x2="192" y2="6" class="line-consumption"/>'
        f'<text x="198" y="10" class="legend-text">Consumo</text>'
        f'</g>'
    )
    return (
        '<svg class="series-fig" viewBox="0 0 720 360" '
        'xmlns="http://www.w3.org/2000/svg" role="img" '
        'aria-label="Consumo y reservas probadas de petróleo, 1980-2020 (miles de millones de barriles)">'
        f'<g>{grid}</g>'
        f'<g>{axes}</g>'
        f'<g>{xlab}</g>'
        f'<g>{ylab}</g>'
        f'<polyline points="{res_pts}" class="line-reserves" fill="none"/>'
        f'<polyline points="{con_pts}" class="line-consumption" fill="none"/>'
        '<text x="380" y="352" class="axis-title" text-anchor="middle">Miles de millones de barriles</text>'
        f'{legend}'
        '</svg>'
    )


# Datos aproximados extraídos de la figura 6 del libro
GOLD = [
    (1900, 25000, 1.4), (1905, 28000, 1.6), (1910, 32000, 2.3), (1915, 36000, 1.5),
    (1920, 38000, 1.3), (1925, 41000, 1.4), (1930, 45000, 1.8), (1935, 50000, 2.1),
    (1940, 55000, 2.5), (1945, 58000, 1.5), (1950, 62000, 1.4), (1955, 67000, 1.5),
    (1960, 72000, 1.6), (1965, 79000, 1.75), (1970, 85000, 1.5), (1975, 92000, 1.6),
    (1980, 98000, 1.3), (1985, 106000, 1.5), (1990, 115000, 1.65), (1995, 128000, 1.9),
    (2000, 140000, 1.95), (2005, 156000, 1.7), (2010, 170000, 1.8),
    (2015, 185000, 1.75), (2020, 201000, 1.7),
]


def fig6_gold():
    """Doble eje: reservas totales (toneladas, izq) y crecimiento anual (%, der)."""
    X0, X1 = 70, 650
    Y_TOP, Y_BOT = 30, 310
    RES_MAX, PCT_MAX = 200000, 3.0
    sx = lambda yr: X0 + (yr - 1900) / (2020 - 1900) * (X1 - X0)
    syR = lambda v: Y_BOT - (v / RES_MAX) * (Y_BOT - Y_TOP)
    syP = lambda v: Y_BOT - (v / PCT_MAX) * (Y_BOT - Y_TOP)
    grid = ''.join(
        f'<line x1="{X0}" y1="{syR(v):.1f}" x2="{X1}" y2="{syR(v):.1f}" class="grid"/>'
        for v in (50000, 100000, 150000, 200000)
    )
    axes = (
        f'<line x1="{X0}" y1="{Y_BOT}" x2="{X1}" y2="{Y_BOT}" class="axis"/>'
        f'<line x1="{X0}" y1="{Y_TOP}" x2="{X0}" y2="{Y_BOT}" class="axis"/>'
        f'<line x1="{X1}" y1="{Y_TOP}" x2="{X1}" y2="{Y_BOT}" class="axis"/>'
    )
    xlab = ''.join(
        f'<text x="{sx(y):.1f}" y="{Y_BOT + 18}" class="tick-label" text-anchor="middle">{y}</text>'
        for y in range(1900, 2021, 10)
    )
    ylab_res = ''.join(
        f'<text x="{X0 - 8}" y="{syR(v) + 4:.1f}" class="tick-label" text-anchor="end">{v // 1000:d} 000</text>'
        for v in (50000, 100000, 150000, 200000)
    )
    ylab_pct = ''.join(
        f'<text x="{X1 + 8}" y="{syP(v) + 4:.1f}" class="tick-label" text-anchor="start">{int(v)}%</text>'
        for v in (1, 2, 3)
    )
    res_pts = ' '.join(f'{sx(yr):.1f},{syR(r):.1f}' for yr, r, _ in GOLD)
    pct_pts = ' '.join(f'{sx(yr):.1f},{syP(p):.1f}' for yr, _, p in GOLD)
    legend = (
        f'<g transform="translate({X0 + 10},{Y_BOT + 36})">'
        f'<line x1="0"   y1="6" x2="22" y2="6" class="line-reserves"/>'
        f'<text x="28"  y="10" class="legend-text">Reservas de oro, toneladas (eje izquierdo)</text>'
        f'<line x1="0"   y1="26" x2="22" y2="26" class="line-consumption"/>'
        f'<text x="28"  y="30" class="legend-text">Crecimiento anual de las reservas (eje derecho)</text>'
        f'</g>'
    )
    return (
        '<svg class="series-fig" viewBox="0 0 720 400" '
        'xmlns="http://www.w3.org/2000/svg" role="img" '
        'aria-label="Reservas totales de oro en toneladas y crecimiento anual, 1900-2020">'
        f'<g>{grid}</g>'
        f'<g>{axes}</g>'
        f'<g>{xlab}</g>'
        f'<g>{ylab_res}</g>'
        f'<g>{ylab_pct}</g>'
        f'<polyline points="{res_pts}" class="line-reserves" fill="none"/>'
        f'<polyline points="{pct_pts}" class="line-consumption" fill="none"/>'
        f'{legend}'
        '</svg>'
    )


# ===================== CONTENIDO =====================
CONTENT = [
    # Epígrafe
    ("quote",
     'El hombre está sujeto al paso del tiempo. Nace, crece, envejece y muere. Su tiempo es escaso. Debe economizarlo como economiza otros bienes escasos. La economización del tiempo tiene un carácter peculiar debido a la singularidad e irreversibilidad del orden temporal.',
     'Ludwig von Mises'),

    # ============== 3.1 ==============
    ("section", "El recurso definitivo"),

    ("lead",
     'La acción humana se desarrolla a lo largo del tiempo. Todas las decisiones económicas tienen lugar a través del tiempo, y la producción requiere tiempo. Al ser mortal, el tiempo del hombre en la Tierra es escaso, y esa escasez lo convierte en un bien económico y le da valor. La naturaleza irreversible del tiempo lo convierte en un bien económico único: no se puede recuperar el tiempo invertido en algo, ni seguir incrementándolo indefinidamente.'),

    'Mises y los economistas austriacos escribieron con elocuencia sobre la importancia de comprender la dimensión temporal de la acción humana. Este capítulo también se basará en el trabajo del economista Julian Simon para argumentar que el tiempo humano es el <em>recurso definitivo</em> y que la escasez económica es una consecuencia de la escasez del tiempo humano. La economía del tiempo es el acto economizador por excelencia, del que se derivan todas las decisiones económicas. Si se dispone de más tiempo, los seres humanos pueden producir más de cualquier bien económico. Es únicamente la escasez del tiempo lo que nos obliga a elegir entre bienes económicos, creando su escasez.',

    'Cuando un niño nace en este mundo, comienza su tiempo en él. Ese tiempo es incierto. Puede durar una hora o un siglo entero. Nadie sabe cuánto vivirá, pero todo el mundo pronto se da cuenta de que es imposible vivir para siempre, y que el tiempo de uno sólo disminuirá hasta agotarse por completo. Al darse cuenta de ello, y con la madurez, los seres humanos comienzan a economizar el tiempo.',

    'En contraste con la escasez relativa y en constante disminución de los objetos materiales, la escasez absoluta del tiempo humano aumenta con el tiempo. Esto es intuitivamente cierto a nivel individual: el crecimiento y el envejecimiento hacen que el hombre se dé cuenta de que su tiempo en la Tierra sólo se hace más escaso, dándole más valor. También se observa en el precio de mercado que se paga por el trabajo humano: a medida que el ser humano pasa más tiempo trabajando y produciendo, aumenta la abundancia de objetos materiales, haciéndoles perder valor medido en términos de trabajo humano.',

    'En su libro <em>El recurso definitivo</em>, Simon sostiene que el tiempo humano, o el trabajo humano, es el recurso definitivo, ya que puede utilizarse para fabricar todos los bienes y recursos económicos. La dedicación de tiempo a cualquier proceso de producción daría lugar a un aumento de su producción. El término «recurso» para describir los bienes materiales es inapropiado, ya que los recursos materiales son los productos del despliegue del recurso definitivo —el tiempo humano— para transformar materiales cuya abundancia es prácticamente infinita en bienes económicos útiles. Las materias primas, los metales y los combustibles no nos son dados como maná caído del cielo; son el complejo resultado de sofisticados procesos de producción.',

    'La concepción de Simon del tiempo humano como el recurso definitivo aclara la naturaleza de la escasez económica. Mientras que los economistas habían postulado a la escasez de bienes materiales como punto de partida del análisis económico, sería más acertado entender la escasez en función de la naturaleza finita del tiempo humano. Si bien los bienes materiales son técnicamente escasos en la Tierra, sus cantidades absolutas dentro del planeta están muy por encima de nuestra capacidad de explotación. Lo que las hace escasas para nosotros es el tiempo que se requiere para producirlas.',

    # ============== 3.2 ==============
    ("section", "Costo de oportunidad"),

    'La escasez del tiempo es la razón por la cual los seres humanos tienen que pensar no sólo en los costos monetarios directos asociados a cualquier actividad, sino en su <em>costo de oportunidad</em>: el costo de una actividad en términos del valor renunciado de una actividad diferente en la que una persona podría haberse involucrado. El hecho de que nuestro tiempo sea escaso significa que no podemos dedicarnos a todas las actividades en todo momento. Tenemos que elegir. Aunque los recursos físicos no fueran una limitación, el tiempo necesario para llevar a cabo las actividades siempre lo es, y los seres humanos deben tener en cuenta las alternativas a las que renuncian cada vez que participan en una actividad.',

    'La inevitabilidad de la muerte y la finitud del tiempo, y por lo tanto su escasez, exigen una constante consideración del costo de oportunidad; de ahí se deriva todo el pensamiento económico y la acción economizadora del hombre. Todas las acciones humanas consumen tiempo y, por ello, tienen el costo de acciones no realizadas. Dado que el tiempo humano es escaso, es valioso. Por lo mismo, siempre existe un uso alternativo del tiempo que es valioso para un individuo y que debe tenerse en cuenta.',

    # ============== 3.3 ==============
    ("section", "Abundancia material"),

    'La medida más habitual para hablar de la abundancia de recursos es la de «reservas conocidas» o «reservas probadas», expresiones que se refieren a las cantidades de un recurso que se sabe con certeza que existen en lugares concretos y que pueden extraerse con la tecnología y los precios actuales. Esta medida ha aumentado a largo plazo para todos los recursos conocidos por el hombre. A medida que consumimos más de un recurso, éste se emplea en más usos, lo que crea una mayor demanda e incentiva su búsqueda, aumentando así sus reservas.',

    'Simon ilustra cómo estas reservas probadas aumentaron entre 1950 y 1990 para algunos metales industriales importantes. La población mundial en 1950 era de unos 2 500 millones de personas y, para 1990, había crecido hasta los 5 320 millones. Medido en dólares de 2011, se calcula que el PBI mundial pasó de 9.25 billones en 1950 a 47.04 billones en 1990. En cuarenta años, con la población multiplicada por 2.13 y la producción quintuplicada, las reservas probadas de la mayoría de los metales crecieron en lugar de agotarse, y a un ritmo mayor que el crecimiento de la población: plomo ×3, zinc ×4.21, cobre ×5.66, mineral de hierro ×8.27, petróleo ×13.1, fosfato ×14 y bauxita ×16.6.',

    'La medida de las reservas probadas no sirve como medida de los recursos totales de la Tierra, sino como medida de la cantidad de esfuerzo que dedicamos a la búsqueda y exploración. A medida que nuestra explotación de estos recursos y nuestro nivel de vida crecen, desarrollamos mejores herramientas de excavación y excavamos en más zonas. Las reservas probadas no son más que la punta del gigantesco iceberg de los recursos totales de la Tierra, que nunca podremos estimar con algún grado de precisión. La Tierra es enorme y su composición exacta es muy difícil de determinar desde la superficie.',

    'Hacerse una idea de la magnitud de la Tierra corrobora el argumento de Simon. La superficie de la Tierra es de 510.1 millones de km², y la superficie total utilizada para la minería entre los años 2000 y 2017 se estimó en 57 277 km², o el 0.011 % de la superficie del planeta. Para ponerlo en perspectiva, si la superficie de la Tierra tuviera el tamaño de un campo de fútbol (105 m × 68 m, o 7 140 m²), la superficie de todas las minas del mundo sería de 0.785 m², aproximadamente el tamaño de la superficie de un escritorio pequeño (un escritorio de 122 cm × 61 cm tiene una superficie de 0.744 m²).',

    ("figure", fig2_cancha_escritorio(),
     "Figura 2 · Si la superficie de la Tierra fuera un campo de fútbol, la superficie de todas las minas sería la de un escritorio pequeño."),

    'El diámetro de la Tierra es de 12 742 kilómetros. En cambio, la mina más profunda del mundo, la mina de oro de Mponeng, cerca de Johannesburgo, tiene «sólo» entre 3.16 km y 3.84 km de profundidad, es decir, entre el 0.024 % y el 0.03 % del diámetro de la Tierra. Para ponerlo en perspectiva, si la Tierra fuera una bola de un metro de diámetro, el agujero más profundo jamás excavado en su corteza tendría unos 0.027 centímetros, menos que el grosor de tres páginas de este libro. La inmensa mayoría de la superficie de la Tierra no ha sido excavada en busca de recursos, y en los pocos lugares donde hemos excavado apenas hemos arañado, literalmente, la superficie.',

    'La mayoría de las minas tiene una profundidad cercana a los 300 metros. Supongamos muy generosamente una profundidad promedio de un kilómetro: el volumen total de minas en el periodo 2000-2017 sería de 57 277 km³. El volumen de la Tierra es de aproximadamente 1 083 210 000 000 km³ (alrededor de un billón de kilómetros cúbicos). El volumen de todas las minas del mundo es, por lo tanto, el 0.000005 % del volumen de la Tierra. La Tierra es 18 millones de veces más grande que todas las minas que existen en ella. Si el volumen de la Tierra fuera el de una alberca olímpica, todas las minas del mundo tendrían aproximadamente el tamaño de medio vaso de agua.',

    ("figure", fig3_alberca_vaso(),
     "Figura 3 · Si la Tierra fuera una alberca olímpica, todas nuestras minas serían medio vaso de agua."),

    'Si todos los recursos que consumen los seres humanos proceden del equivalente a medio vaso de la alberca olímpica que es la Tierra, se hace evidente por qué preocuparse por la cantidad total de recursos es tan desacertado. Las estimaciones más conservadoras concluyen que la abundancia total de cualquier sustancia natural en la corteza terrestre es muchos múltiplos de la cantidad total que los seres humanos consumen de ella. Es bastante probable que la abundancia total de cualquier metal en la corteza terrestre equivalga a millones de años de consumo humano. El límite real de cuánto podemos producir de cada metal en un año determinado sigue siendo la cantidad de tiempo y recursos que dediquemos a su producción y la cantidad de otros bienes y servicios a los que estemos dispuestos a renunciar.',

    'Estas medidas agregadas de los recursos de la Tierra son, más allá de su valor ilustrativo, irrelevantes para las decisiones económicas. No hay decisiones que tengan que ver con las reservas totales de un material en la Tierra; todas se toman al margen, basándose en el costo de extraer la siguiente unidad y los ingresos marginales esperados. Una analogía útil: considerar los recursos de la Tierra como rocas y nuestro consumo como el uso de rocas para construir casas. Ninguna decisión económica necesita tener en cuenta la cantidad total de rocas que hay en la Tierra; las decisiones se refieren únicamente a la aplicación de recursos escasos —trabajo, capital y tierra— al proceso de excavación y colocación.',

    'Lo que realmente valoramos no son los recursos de la Tierra, sino los bienes económicos fabricados a partir de ellos. Eso es lo que requiere tiempo, y el tiempo es lo que escasea. El tiempo es la escasez de la que se originan todas las demás. La materia prima está por todas partes a nuestro alrededor, pero el tiempo para producir bienes económicos a partir de ella es escaso. Al enfrentarse a una mayor demanda de un bien fabricado a partir de un recurso de la Tierra, existe el incentivo de producir más e invertir más en su producción. A medida que aumenta la productividad, podemos obtener mayores cantidades por cantidad de tiempo invertido: el precio real del bien, medido en términos de trabajo humano, va disminuyendo.',

    'Aunque los precios de los productos básicos pueden y suelen subir en términos de las monedas nacionales, eso es resultado de la devaluación de las monedas. Cuando se miden con respecto a los salarios —es decir, con respecto al precio del tiempo humano—, todos los productos básicos van bajando de precio en el largo plazo, incluso cuando su consumo no deja de aumentar. En un mundo de dinero difícil de producir, como bajo el patrón oro, sería perfectamente normal esperar que los precios de todos los productos básicos disminuyeran constantemente con el tiempo.',

    'Los economistas Gale Pooley y Marian Tupy construyeron un índice en honor a Julian Simon, que mide los precios de cincuenta productos básicos en función de los salarios. Encontraron que, entre 1980 y 2020, el tiempo necesario para ganar una canasta de cincuenta productos básicos ha disminuido un 75.2 %. Una hora de trabajo en 2020 compraba 4.03 veces más de esos productos que en 1980. La abundancia tuvo una tasa de crecimiento anual del 3.55 %, es decir, se duplicó cada veinte años. A pesar de que la población humana aumentó un 75.8 % en esos cuarenta años, los precios de cincuenta productos básicos disminuyeron tres cuartas partes en términos del tiempo humano necesario para adquirirlos.',

    ("figure", fig4_commodities(),
     "Figura 4 · Variación de precio (en tiempo humano) y multiplicador de abundancia para 50 productos básicos, 1980 vs. 2020. El PROMEDIO está marcado."),

    'La única escasez es el tiempo que tienen los seres humanos para producir estos productos básicos, y por eso los salarios globales siguen aumentando, lo que hace que los productos y materiales sean cada vez más baratos en términos de trabajo humano. El único recurso cuyo precio ha subido casi continuamente a lo largo de la historia es el tiempo humano, medido por los salarios.',

    'Sólo con este marco se puede entender por qué la humanidad nunca se ha quedado sin ningún recurso, incluso después de muchos milenios de explotar la Tierra y de las incesantes predicciones de una fatalidad inminente. No sólo no se ha agotado ni uno de estos recursos, sino que los precios reales siguen bajando, la producción anual de prácticamente todos sigue aumentando cada año, y las reservas probadas no han hecho más que aumentar. Si los recursos fueran finitos, las reservas existentes disminuirían con el tiempo a medida que consumimos más. Pero aunque siempre estamos consumiendo más, los precios siguen bajando y las mejoras tecnológicas nos permiten encontrar más reservas sin explotar.',

    'El petróleo, el sustento vital de las economías modernas, es el mejor ejemplo. Aunque el consumo y la producción de petróleo siguen aumentando año tras año, las reservas probadas crecen a un ritmo aún más rápido. Según la <em>Revisión estadística de la energía mundial</em> de British Petroleum, la producción anual de petróleo en 2015 fue un 46 % superior a la de 1980, mientras que el consumo fue un 55 % mayor. Las reservas, por su parte, aumentaron un 148 %, aproximadamente el triple que el aumento de la producción y el consumo.',

    ("figure", fig5_oil(),
     "Figura 5 · Petróleo, 1980-2020: el consumo total sube poco y las reservas probadas totales suben el triple, en miles de millones de barriles."),

    'Se pueden elaborar estadísticas similares para recursos con diversos grados de prevalencia en la corteza terrestre. La rareza de un recurso determina el costo relativo de extraerlo de la Tierra. Los metales más comunes, como el hierro y el cobre, son fáciles de encontrar y relativamente baratos. Los más raros, como la plata y el oro, son más caros. Sin embargo, el límite a la cantidad que podemos producir de cada uno de esos metales, y no su cantidad absoluta, sigue siendo el costo de oportunidad de su producción. No hay mejor prueba de ello que el hecho de que uno de los metales más raros (si no el más raro) de la corteza terrestre, el oro, se extrae desde hace miles de años y se sigue extrayendo en cantidades cada vez mayores a medida que avanza la tecnología.',

    ("figure", fig6_gold(),
     "Figura 6 · Reservas totales de oro en toneladas (1900-2020) y crecimiento anual de las reservas. Las reservas crecen de forma sostenida; el ritmo anual oscila entre 1 % y 3 %."),

    'La escasez de los materiales es siempre relativa, siendo las diferencias en el costo de extracción las que determinan los grados de escasez.',

    # ============== 3.4 ==============
    ("section", "La apuesta de Simon"),

    'Después de que el presidente Nixon suspendiera la convertibilidad del dólar en oro, en 1971, todos los precios iniciaron una subida inexorable. Para la gente de los setenta, acostumbrada a precios relativamente estables bajo el patrón oro, estas subidas parecían una señal de apocalipsis económico, ya que daban la impresión de que todos nuestros preciados recursos se estaban agotando. Mientras el mundo era arrastrado por la histeria del agotamiento de los recursos y la superpoblación, Simon no se contentó con escribir para contrarrestar el ánimo. Trató de exponer la insensatez del ambiente desafiando a uno de los principales histéricos del siglo XX, Paul Ehrlich, a una apuesta pública.',

    'Simon retó a Ehrlich a especificar cualquier recurso que estuviera seguro que se agotaría o se volvería mucho más escaso en cualquier periodo superior a un año, y Simon le apostaría mil dólares a que cada uno de ellos sería de hecho más barato, en términos reales, al final del periodo.',

    'La apuesta debió parecerle un donativo a Ehrlich; tal era la convicción de sus advertencias sobre el inminente agotamiento de recursos críticos. Ehrlich especificó cinco metales y un periodo de diez años para evaluar su precio, de 1980 a 1990. Al final del periodo, cada uno de estos metales era más barato en términos reales que al principio. Treinta años después, estos metales no han hecho más que abaratarse en términos reales, mientras que su producción anual sigue aumentando cada año.',

    'La razón por la que bajó el precio de todos estos metales es porque su escasez es relativa, no absoluta. Son escasos para nosotros porque el tiempo y los factores de producción deben desviarse de la producción de otros bienes. Simon comprendió que, a medida que aumentara la demanda de estos metales, se destinaría más tiempo y más capital a su producción. El aumento de la demanda provoca una subida de los precios, lo que proporciona mayores beneficios a los productores, que disponen así de más dinero para invertir en prospección, extracción, refinado y distribución. Esta inversión conduce a un aumento de la productividad, es decir, de la producción por unidad de insumo.',

    'Como geólogo, la concepción de la escasez de Ehrlich se basaba en estimaciones del consumo comparadas con las reservas, sin tener en cuenta el papel de la acción humana. Simon, como economista, entendía la dinámica que impulsaba la producción: la escasez de estos metales dependía, en última instancia, de la cantidad de tiempo que los humanos les dedicaran, y eso dependía del incentivo que tuvieran para producirlos, no de las limitaciones geológicas. Si aumenta la demanda de un metal, no hay una cantidad limitada de reservas que agotar. Siempre hay otros suelos que prospectar y minas más profundas que excavar.',

    # ============== 3.5 ==============
    ("section", "Preferencia temporal"),

    'El tiempo humano es finito e incierto: nadie sabe con certeza cuánto tiempo vivirá, o en qué momento podría morir. Esto crea en el hombre una <em>preferencia temporal</em>, una preferencia universal por la satisfacción temprana sobre la tardía. Los individuos siempre prefieren consumir o tener un bien hoy antes que en cualquier periodo futuro, porque la supervivencia nunca es segura. La preferencia temporal siempre tiene un valor positivo. Además, en el caso de los bienes duraderos, es probable que disfruten de sus servicios durante más tiempo cuanto antes los reciban.',

    'Aunque la preferencia temporal es siempre positiva, su valor varía en función del grado en que los seres humanos descuentan —desvalorizan— la utilidad futura en comparación con la utilidad presente. Una preferencia temporal relativamente baja indica un bajo grado de descuento de la utilidad futura, lo que apunta a una preocupación relativamente mayor por el futuro. Una preferencia temporal más alta implica un mayor descuento del futuro y una fuerte orientación hacia el presente.',

    # ============== 3.6 ==============
    ("section", "Economizando el tiempo"),

    'La escasez económica es, en definitiva, la escasez del tiempo humano. En consecuencia, toda la economización humana se centra en la economización del tiempo: buscamos aumentar la cantidad y el valor subjetivo de nuestro tiempo en la Tierra. El hecho de que el tiempo sea escaso significa que los seres humanos buscan constantemente gastarlo de las formas que les ofrezcan más satisfacción o que sean más valiosas. Que el futuro sea incierto y la preferencia temporal sea universalmente positiva significa que buscan constantemente maximizar el valor de su tiempo presente.',

    'El <em>ocio</em> es el término utilizado para designar el tiempo que las personas pasan haciendo cosas que les gustan por sí mismas, cosas que les producen un placer inmediato, en contraposición a las cosas que hacen a cambio de una recompensa futura. El ocio es la forma en que los economistas se refieren a los buenos momentos. A todo el mundo le gusta pasarla bien. La vida es finita, y los seres humanos desean naturalmente pasarla haciendo las cosas que les gustan. La preferencia temporal siempre va a ser positiva.',

    'A todo el mundo le gustaría pasar toda su vida en el ocio. Pero como no somos criaturas eternas que viven en el Jardín del Edén, demasiado ocio significará inevitablemente una muerte prematura por inanición o por las fuerzas de la naturaleza. Tampoco podemos limitarnos a disfrutar del ocio indefinidamente, porque siempre somos capaces de concebir formas de mejorar la calidad y la cantidad del tiempo que tenemos en la Tierra. También nos gustaría maximizar la cantidad de tiempo —vivir vidas largas— y maximizar el valor de nuestro tiempo futuro.',

    'La razón nos permite concebir formas de actuar para aumentar nuestras posibilidades de supervivencia y mantener a nuestro yo futuro. Nos permite concebir un futuro mejor, trabajar para conseguirlo y sacrificar el disfrute presente por él. Cuanto más valore un individuo el futuro y trabaje y provea para él, más probabilidades tendrá de sobrevivir en el futuro.',

    'La cuestión económica es cómo sacrificamos la utilidad presente por la supervivencia a largo plazo y la utilidad futura. El intercambio más importante que realiza un individuo es el que lleva a cabo con su yo futuro. El intercambio más sencillo es el que implica renunciar al placer inmediato en favor del trabajo para proveer para el futuro. La comida hay que cazarla, cultivarla o adquirirla, y el techo hay que construirlo o adquirirlo. Esto exige sacrificar el disfrute presente en favor del trabajo.',

    'La razón del hombre lo lleva a darse cuenta de que puede proveer para su futuro. Entiende que el trabajo, aunque es desagradable en el momento e implica el costo de renunciar al placer, le permitirá cosechar las recompensas en el futuro. La razón y el deseo de vivir mucho y bien conspiran para reducir la preferencia temporal del hombre. Lo instan no sólo a abandonar el ocio en busca del trabajo, sino también a mantener a su yo futuro a través del aplazamiento del consumo actual, el ahorro y la acumulación de bienes duraderos y capital productivo.',

    'Es este proceso de disminución de la preferencia temporal, de orientación y de provisión para el futuro, lo que pone en marcha el proceso de civilización. Como dijo Hans-Hermann Hoppe sobre la preferencia temporal: «Una vez que es lo suficientemente baja como para permitir el ahorro y la formación de capital o de bienes de consumo duraderos, se pone en marcha una tendencia hacia la caída de la preferencia temporal, acompañada de un «proceso de civilización».',

    'A medida que los seres humanos cosechan los beneficios de la provisión para el futuro y la baja preferencia temporal, se vuelven más propensos a dedicarse a ello. El trabajo y la acumulación de capital llevan a aumentos en la productividad, incrementando el valor del tiempo del individuo. Cuanto más capaces son las personas de proveer para su futuro, éste se vuelve menos incierto, lo que a su vez fomenta un mayor interés por el futuro, el ahorro y la acumulación de capital, todo lo cual resulta en un probable aumento de la cantidad y el valor del tiempo de un individuo en la Tierra.',

    # ============== 3.7 ==============
    ("section", "Economizando la acción"),

    'No existe la opción de no participar en la economía ni en la elección económica, excepto a través de la muerte. Puede que a usted no le gusten instituciones específicas como la propiedad privada o el trabajo, pero elegir no participar en ellas simplemente lo excluye de círculos más amplios y productivos de actividad económica. Si está vivo y quiere seguir viviendo, está obligado a intentar sobrevivir a través de las herramientas de la acción economizadora. Todo el mundo realiza actos economizadores todos los días sin necesidad de aprender economía. Pero aprender economía puede ayudar a la mente a comprender la importancia de los actos en los que participa, y a entender cómo surgen estructuras e instituciones complejas a partir de los mismos.',

    'Cada uno de los nueve capítulos siguientes del libro se centrará en herramientas importantes que los seres humanos hemos desarrollado, consciente y espontáneamente, para aumentar la cantidad y el valor de nuestro tiempo: trabajo, propiedad, capital, tecnología, energía, comercio, dinero, mercado y capitalismo. Estas herramientas son, en esencia, la forma en que los seres humanos economizamos nuestro tiempo. La principal relación costo-beneficio a la que todos nos enfrentamos es que nuestro tiempo puede dedicarse al ocio, a disfrutar de las cosas que nos gustan, o puede dedicarse a la actividad económica, con el objetivo de aumentar la duración y el valor de nuestro tiempo.',

    'Todas estas herramientas económicas tienen algo en común: son pacíficas, y todos los que participan en ellas lo hacen por voluntad propia. Los medios no pacíficos de interacción humana se analizan en el capítulo 16, mientras que la defensa frente a ellos se examina en el capítulo 17.',
]


# ===================== CSS =====================
EXTRA_CSS = """
/* ===== Subtítulos de sección ===== */
.prose h2.section-subtitle {
  font-family: var(--font-body); font-weight: 400;
  font-size: 1.15rem; letter-spacing: 0.02em;
  color: var(--ink); margin: 2.6rem 0 0.9rem;
  padding-bottom: 0.5rem; border-bottom: 1px solid var(--rule);
}
/* ===== Citas en bloque ===== */
.prose .pull-quote {
  margin: 2.4rem 0; padding: 0.3rem 0 0.3rem 1.5rem;
  border-left: 2px solid var(--rule);
}
.prose .pull-quote p {
  font-size: 1.06rem; font-style: italic; line-height: 1.7; color: var(--ink); margin: 0 0 0.7rem;
}
.prose .pull-quote cite {
  display: block; font-style: italic; font-size: 0.88rem; line-height: 1.5; color: var(--ink-soft);
}
/* ===== Figuras ===== */
.prose .chart-fig {
  margin: 2.6rem 0; padding: 0; text-align: center;
}
.prose .chart-fig svg {
  width: 100%; max-width: 640px; height: auto;
  display: block; margin: 0 auto;
}
.prose .chart-fig .figcaption {
  margin: 1rem auto 0; max-width: 34rem;
  font-size: 0.86rem; font-style: italic; line-height: 1.55;
  color: var(--ink-soft); text-align: center;
}
/* Ilustraciones de escala (fig 2 y 3) */
.scale-fig .field       { fill: none; stroke: var(--verde); stroke-width: 1.5; }
.scale-fig .field-line  { stroke: var(--verde); stroke-width: 1; opacity: 0.6; }
.scale-fig .field-dot   { fill: var(--verde); }
.scale-fig .desk        { fill: var(--verde); opacity: 0.6; stroke: var(--ink); stroke-width: 0.5; }
.scale-fig .desk-leg    { stroke: var(--ink); stroke-width: 0.7; }
.scale-fig .pool-edge   { fill: var(--verde); opacity: 0.15; stroke: var(--verde); stroke-width: 1.5; }
.scale-fig .pool-water  { fill: var(--verde); opacity: 0.08; }
.scale-fig .pool-lane line { stroke: var(--verde); stroke-width: 0.6; opacity: 0.45; }
.scale-fig .lens        { stroke: var(--verde); stroke-width: 1; opacity: 0.5; }
.scale-fig .glass-outline { stroke: var(--ink); stroke-width: 0.6; }
.scale-fig .glass-water { fill: var(--verde); opacity: 0.55; }
.scale-fig .dim         { fill: var(--ink-soft); font-size: 13px; font-style: italic;
                          font-family: var(--font-body); }
.scale-fig .dim-small   { fill: var(--ink-soft); font-size: 9px; font-style: italic;
                          font-family: var(--font-body); }
/* Tabla de commodities (fig 4) */
.commodities-fig .col-head   { fill: var(--ink-soft); font-size: 9px; font-style: italic;
                               font-family: var(--font-body); letter-spacing: 0.04em; text-transform: uppercase; }
.commodities-fig .row-name   { fill: var(--ink); font-size: 9.5px;
                               font-family: var(--font-body); }
.commodities-fig .row-name.hl { fill: var(--verde); font-style: italic; }
.commodities-fig .row-val    { fill: var(--ink-soft); font-size: 8.5px;
                               font-family: var(--font-body); font-variant-numeric: tabular-nums; }
.commodities-fig .bar-neg    { fill: var(--ink-soft); opacity: 0.55; }
.commodities-fig .bar-pos    { fill: var(--verde);    opacity: 0.80; }
.commodities-fig .row-sep    { stroke: var(--rule); stroke-width: 0.5; opacity: 0.5; }
/* Series temporales (fig 5 y 6) */
.series-fig .grid        { stroke: var(--rule); stroke-width: 0.8; fill: none; }
.series-fig .axis        { stroke: var(--ink-soft); stroke-width: 1.2; fill: none; }
.series-fig .tick-label  { fill: var(--ink-soft); font-size: 11px;
                           font-family: var(--font-body); font-variant-numeric: tabular-nums; }
.series-fig .axis-title  { fill: var(--ink); font-size: 12px; font-style: italic;
                           font-family: var(--font-body); }
.series-fig .legend-text { fill: var(--ink); font-size: 11px;
                           font-family: var(--font-body); font-style: italic; }
.series-fig .line-reserves    { stroke: var(--verde);    stroke-width: 1.8; }
.series-fig .line-consumption { stroke: var(--ink-soft); stroke-width: 1.6; opacity: 0.85; }
"""


# ===================== BUILD =====================
def main():
    parts = ['<article class="page" id="contenido" tabindex="-1">\n',
             f'\n  <div class="chapter-eyebrow">{EYEBROW}</div>\n',
             f'  <h1 class="chapter-title">{TITLE}</h1>\n',
             f'  <p class="chapter-subtitle">{SUBTITLE}</p>\n',
             '\n  <div class="ornament">• • •</div>\n',
             '\n  <div class="prose">\n']
    for it in CONTENT:
        if isinstance(it, str):
            parts.append(f'    <p>{it}</p>\n')
        elif it[0] == "lead":
            parts.append(f'    <p class="lead">{it[1]}</p>\n')
        elif it[0] == "section":
            parts.append(f'\n    <h2 class="section-subtitle">{it[1]}</h2>\n')
        elif it[0] == "quote":
            _, qtext, cite = it
            parts.append('\n    <blockquote class="pull-quote">\n')
            parts.append(f'      <p>{qtext}</p>\n')
            parts.append(f'      <cite class="no-audio">{cite}</cite>\n')
            parts.append('    </blockquote>\n\n')
        elif it[0] == "figure":
            _, svg, caption = it
            parts.append('\n    <aside class="no-audio chart-fig">\n')
            parts.append(f'      {svg}\n')
            parts.append(f'      <p class="figcaption">{caption}</p>\n')
            parts.append('    </aside>\n\n')
    parts.append('\n  </div>\n\n</article>')
    article = ''.join(parts)

    sk = open('tres-regimenes.html', encoding='utf-8').read()
    out = sk
    out = re.sub(r'<title>.*?</title>',
                 f'<title>{TITLE} — Principios Económicos</title>',
                 out, count=1, flags=re.DOTALL)
    out = re.sub(r'<article class="page"[^>]*>.*?</article>',
                 lambda _m: article, out, count=1, flags=re.DOTALL)
    new_nav = ('<nav class="nav-foot">'
               '<a class="prev" href="valor.html">Valor</a>'
               '<a class="idx" href="index.html">Índice</a>'
               '<span></span></nav>')
    out = re.sub(r'<nav class="nav-foot">.*?</nav>',
                 lambda _m: new_nav, out, count=1, flags=re.DOTALL)
    out = out.replace('audio/tres-regimenes.mp3', 'audio/tiempo.mp3')
    out = out.replace('audio/tres-regimenes.alignment.json',
                      'audio/tiempo.alignment.json')
    out = out.replace('data-storage-key="tres-regimenes"',
                      'data-storage-key="tiempo"')
    out = out.replace('</style>', EXTRA_CSS + '</style>', 1)

    open('tiempo.html', 'w', encoding='utf-8').write(out)
    n_par = sum(1 for it in CONTENT if isinstance(it, str) or (isinstance(it, tuple) and it[0] == "lead"))
    n_sec = sum(1 for it in CONTENT if isinstance(it, tuple) and it[0] == "section")
    n_q = sum(1 for it in CONTENT if isinstance(it, tuple) and it[0] == "quote")
    n_fig = sum(1 for it in CONTENT if isinstance(it, tuple) and it[0] == "figure")
    print(f"tiempo.html creado: {n_par} párrafos, {n_sec} secciones, {n_q} citas, {n_fig} figuras")


if __name__ == "__main__":
    main()
