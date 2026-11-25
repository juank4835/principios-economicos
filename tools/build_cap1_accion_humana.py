#!/usr/bin/env python3
"""Construye el cap 1 «Acción humana» de Principios Económicos.

Capítulo con:
  - Epígrafe (Mises) antes del primer párrafo.
  - Prosa intro de 3 párrafos.
  - 4 secciones (1.1 a 1.4) con h2.section-subtitle.
  - 4 citas en bloque (Mises, Hoppe, Mises, Hayek).
Sin notas al pie (quitadas los superíndices y la sección «Notas»).
"""
import re

EYEBROW = "Parte I · Fundamentos"
TITLE = "Acción humana"
SUBTITLE = "Saifedean Ammous — Principios de Economía"

# ---- Figura 1: Phillips (inflación vs desempleo, EEUU, 61 años) ----
PHILLIPS_POINTS = [
    (-0.4, 9.2), (0.1, 5.2), (1.0, 6.6), (1.2, 8.0), (1.2, 5.5), (1.2, 4.8),
    (1.3, 5.5), (1.4, 7.3), (1.5, 5.6), (1.5, 4.5), (1.6, 9.5), (1.6, 6.1),
    (1.6, 4.5), (1.8, 3.6), (1.9, 6.9), (2.0, 8.0), (2.1, 4.3), (2.1, 4.1),
    (2.2, 5.9), (2.3, 4.9), (2.4, 3.9), (2.6, 6.0), (2.6, 5.5), (2.7, 3.9),
    (2.8, 4.7), (2.8, 4.5), (2.9, 5.5), (2.9, 6.9), (3.0, 7.4), (3.0, 3.8),
    (3.1, 5.3), (3.1, 8.9), (3.2, 9.5), (3.2, 4.6), (3.2, 5.5), (3.3, 4.0),
    (3.4, 5.0), (3.4, 6.2), (3.5, 7.1), (3.6, 6.1), (3.8, 5.7), (4.0, 5.4),
    (4.2, 6.7), (4.2, 7.5), (4.2, 5.9), (4.2, 3.6), (4.6, 5.4), (4.8, 5.2),
    (5.3, 5.6), (5.4, 3.5), (5.7, 7.7), (5.8, 4.9), (6.1, 9.7), (6.1, 4.9),
    (6.5, 7.0), (7.6, 6.0), (9.1, 8.4), (10.3, 7.5), (11.0, 5.5), (11.2, 5.8),
    (13.5, 7.1),
]

def phillips_svg():
    X0, X1 = 70, 690
    Y_TOP, Y_BOT = 30, 360
    sx = lambda v: X0 + (max(v, 0) / 15.0) * (X1 - X0)
    sy = lambda v: Y_BOT - (v / 15.0) * (Y_BOT - Y_TOP)
    grid = []
    for v in (5, 10, 15):
        grid.append(f'<line x1="{sx(v):.1f}" y1="{Y_TOP}" x2="{sx(v):.1f}" y2="{Y_BOT}" class="grid"/>')
        grid.append(f'<line x1="{X0}" y1="{sy(v):.1f}" x2="{X1}" y2="{sy(v):.1f}" class="grid"/>')
    axes = (
        f'<line x1="{X0}" y1="{Y_BOT}" x2="{X1}" y2="{Y_BOT}" class="axis"/>'
        f'<line x1="{X0}" y1="{Y_TOP}" x2="{X0}" y2="{Y_BOT}" class="axis"/>'
    )
    xlab = ''.join(
        f'<text x="{sx(v):.1f}" y="{Y_BOT + 18}" class="tick-label" text-anchor="middle">{v} %</text>'
        for v in (0, 5, 10, 15)
    )
    ylab = ''.join(
        f'<text x="{X0 - 10}" y="{sy(v) + 4:.1f}" class="tick-label" text-anchor="end">{v} %</text>'
        for v in (0, 5, 10, 15)
    )
    pts = ''.join(
        f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="4.5" class="pt"/>'
        for (x, y) in PHILLIPS_POINTS
    )
    return (
        '<svg class="phillips-chart" viewBox="0 0 720 410" '
        'xmlns="http://www.w3.org/2000/svg" role="img" '
        'aria-label="Dispersión de inflación y desempleo en EEUU: no hay trade-off visible">'
        f'<g>{"".join(grid)}</g>'
        f'<g>{axes}</g>'
        f'<g>{xlab}</g>'
        f'<g>{ylab}</g>'
        '<text x="380" y="402" class="axis-title" text-anchor="middle">Inflación</text>'
        '<text x="22" y="195" class="axis-title" text-anchor="middle" '
        'transform="rotate(-90 22 195)">Desempleo</text>'
        f'<g>{pts}</g>'
        '</svg>'
    )

# Items soportados:
#   "texto"                   → párrafo normal <p>
#   ("lead", texto)           → primer párrafo con capital <p class="lead">
#   ("section", título)       → subtítulo de sección <h2 class="section-subtitle">
#   ("quote", texto, cite)    → cita en bloque; cite no se narra
#   ("figure", svg, caption)  → figura en aside.no-audio (NO se narra)
CONTENT = [
    # Epígrafe
    ("quote",
     'El estudio de la economía no tiene que ver con las cosas y los objetos materiales tangibles, sino con los hombres, sus significados y sus acciones. Los bienes, las mercancías y la riqueza y todas las demás nociones de conducta no son elementos de la naturaleza; son elementos del significado y la conducta humanos. Quien quiera ocuparse de ellos no debe mirar al mundo exterior; debe buscarlos en el significado de los hombres que actúan.',
     'Ludwig von Mises'),

    # Intro (3 párrafos)
    ("lead",
     'La <em>opus magnum</em> de Ludwig von Mises, <em>La acción humana</em>, ofreció una redefinición explícita del campo de la economía como el estudio de la acción y la elección humanas en condiciones de escasez. Mises creía que el razonamiento económico correcto y el análisis adecuado de los fenómenos económicos debían basarse en la acción humana, más que en el análisis de los objetos materiales y sus propiedades, o de variables agregadas y abstractas. Aunque la perspectiva de Mises al principio pueda parecer pedante e improductiva, este capítulo explicará cómo la misma es una herramienta muy poderosa para entender la realidad económica.'),

    'Mises argumenta que los filósofos han intentado durante mucho tiempo estudiar la evolución y el destino de la humanidad basándose en una comprensión de lo que la historia, Dios o la naturaleza habían previsto para los seres humanos. Tales análisis se ocupaban de la humanidad en su conjunto o se centraban en conceptos colectivistas como nación, raza o iglesia, y trataban de encontrar leyes que explicaran el comportamiento de tales entidades y sus consecuencias, como si la historia tuviera leyes inamovibles que descubrir, semejantes a las de las ciencias naturales.',

    'Al escribir <em>Principios de Economía</em> en 1871, Carl Menger fue pionero en el análisis marginal de las cuestiones económicas. Esta «revolución marginal» supuso una alternativa radicalmente distinta a los métodos de estudio de los seres humanos que se usaban hasta entonces. En lugar de observar la historia basándose en la voluntad de Dios, de la naturaleza, o a través de la nación, la raza o la iglesia, el análisis marginal demostró que la sociedad humana se entiende mejor analizando sus principales fuerzas impulsoras: la elección y la acción humana a nivel individual. La escuela austriaca de economía surgió en torno a Menger en Viena. Pocos años después, Léon Walras desarrollaría su propia concepción del marginalismo, basada en un concepto de equilibrio general. El equilibrio general walrasiano se convertiría en la tradición dominante de la economía moderna, basada en la matematización y las relaciones entre agregados.',

    # ============== 1.1 ==============
    ("section", "Acción, intención y razón"),

    'Mises define la acción humana como «comportamiento intencionado», con el fin de distinguirla de los actos instintivos, impulsivos o emocionales. «La acción es la voluntad puesta en marcha y transformada en actuación; es pretender alcanzar fines y objetivos; es la reacción coherente del ego a los estímulos y las condiciones de su entorno; es el ajuste consciente de una persona al estado del universo que determina su vida».',

    'El alumno de Mises, Murray Rothbard, define la acción humana como «comportamiento intencionado dirigido hacia el logro, en algún momento futuro, de fines que implican la satisfacción de deseos que de otro modo quedarían insatisfechos». Mises postula que, para que tenga lugar la acción, se requiere que el ser humano posea un estado actual e imagine un estado más satisfactorio, y la expectativa de que un comportamiento intencionado pueda aliviar la insatisfacción actual.',

    'La acción racional es la cualidad humana por excelencia: es lo que distingue a los seres humanos de los demás animales. Los seres humanos actuamos intencionadamente porque estamos dotados de razón y somos capaces de dirigirla a la consecución de nuestros fines. Somos capaces de reconocer las relaciones causales del mundo que nos rodea y actuar en consecuencia para conseguir un estado de cosas más favorable. También somos capaces de entender que los demás pueden razonar y actuar para alcanzar sus fines. Como dice Mises:',

    ("quote",
     'El hombre no es un ser que no puede evitar ceder al impulso que más urgentemente pide satisfacción. El hombre es un ser capaz de dominar sus instintos, emociones e impulsos; puede racionalizar su comportamiento. Renuncia a satisfacer un impulso urgente para satisfacer otros deseos. No es esclavo de sus anhelos. Tras ordenar en escala valorativa sus deseos y anhelos, elige; en definitiva, actúa. Lo que distingue al hombre de las bestias es precisamente que ajusta su comportamiento deliberadamente. El hombre es el ser capaz de inhibirse; que puede dominar sus impulsos y deseos; que tiene el poder para refrenar sus instintos.',
     'Mises, <em>La acción humana</em>'),

    'Una imagen mental útil para explicar la primacía de la acción humana es pensar en el mundo físico que nos rodea como plastilina inerte, que podemos moldear con nuestras manos para darle diferentes formas y crear objetos con base en nuestro razonamiento e imaginación. Los objetos inanimados son materia muerta, y es la razón humana dando forma a las acciones humanas la que reorganiza esta materia y le da valor, significado y finalidad. El mundo material se entiende mucho mejor si se estudia como el producto de la razón y la acción humana. No son los astros, ni los nombres abstractos, ni las entidades colectivistas los que actúan, sino los individuos. Si se quieren entender las condiciones del mundo material, lo más útil es estudiar las acciones de los seres humanos que lo moldean.',

    'Desde la perspectiva misesiana y austriaca, la acción humana se entiende y define como racional. La palabra «racional» aquí no se refiere a la corrección de la acción según algún criterio objetivo, ni a la idoneidad de la acción para alcanzar los fines del hombre que actúa, ni emite otros juicios morales. Más bien, lo racional se define como el producto de la razón deliberativa. Siempre que el hombre razona y actúa, actúa racionalmente. El hecho de que tal acción conduzca o no al logro de su objetivo, y el hecho de que cuente o no con la aprobación de otra parte, son irrelevantes para la racionalidad tal como la entiende Mises. Una persona puede darse cuenta de que una acción fue contraproducente y arrepentirse de lo que hizo, pero eso no cambia la racionalidad del acto. Como explica Mises, «lo opuesto a la acción humana no es la conducta irracional, sino la reacción refleja de nuestros órganos corporales al estímulo externo, reacción que no puede ser controlada a voluntad».',

    # ============== 1.2 ==============
    ("section", "Análisis económico"),

    'Concebir la economía como el estudio de la acción humana en condiciones de escasez nos permite definir los términos más importantes de la disciplina en función de su relación con las necesidades humanas, de cómo los trata la razón humana y cómo los seres humanos les dan forma. Cuando se explica, define y comprende a través de la lente de la acción humana, la terminología económica se vuelve más clara, y el análisis económico, más fructífero. Hans-Hermann Hoppe lo explica así:',

    ("quote",
     'Todos los teoremas económicos verdaderos consisten en (a) una comprensión del significado de la acción, (b) una situación o un cambio situacional —que se supone dado o identificado como dado— y descrito en términos de categorías de acción, y (c) una deducción lógica de las consecuencias —también en términos de tales categorías— que deben resultar para un actor a causa de esta situación o cambio situacional.',
     'Hans-Hermann Hoppe'),

    'El objetivo central del enfoque austriaco es entender los procesos causales de la actividad económica y sus consecuencias. La deducción lógica, los experimentos mentales y el sentido común basado en la familiaridad con la realidad se emplean para comprender las implicaciones de los procesos económicos. Al principio este enfoque podría parecer banal e infructuoso en comparación con los enfoques dominantes de la economía convencional actual, cimentados en el análisis matemático. Pero una mirada más atenta mostrará por qué el análisis cuantitativo es inadecuado para construir un marco teórico de la economía, y por qué carece de sentido y de utilidad sin deducciones y conclusiones lógicas que lo motiven. En consonancia con esta crítica, el libro presentará y analizará los actos económicos con lenguaje claro, no con ecuaciones matemáticas.',

    # ============== 1.3 ==============
    ("section", "Análisis cuantitativo"),

    'La crítica austriaca al análisis cuantitativo se resume en el pensamiento de Mises:',

    ("quote",
     'La deficiencia fundamental implícita en todo planteamiento cuantitativo de los problemas económicos consiste en olvidar que no existen relaciones constantes entre lo que se denominan dimensiones económicas. No hay constancia ni continuidad en las valoraciones ni en la formación de las relaciones de intercambio entre las distintas mercancías. Cada nuevo dato provoca una reorganización de toda la estructura de precios. El entendimiento, que trata de captar lo que ocurre en la mente de los hombres afectados, puede abordar el problema de la predicción de las condiciones futuras.',
     'Mises, <em>La acción humana</em>'),

    'Todos los fenómenos físicos pueden medirse utilizando un conjunto consistente, estándar y uniforme de unidades básicas. Esto contrasta con lo que ocurre con los fenómenos económicos, ya que no existe una unidad estándar con la que puedan realizarse y compararse las mediciones económicas del valor. El valor es subjetivo. La utilidad que los individuos obtienen de los bienes también es subjetiva y cambia constantemente en función del individuo, del momento en que se realiza la valoración y de la abundancia relativa del bien. No existe la posibilidad de hacer comparaciones interpersonales de utilidad y, por lo tanto, la matematización de la utilidad será siempre hipotética y teórica, nunca precisa y reproducible.',

    'Sin una unidad común con la cual medir y comparar la utilidad, es imposible formular una ley cuantitativa en torno, por ejemplo, a cambios en la oferta y la demanda basados en cambios en los precios, como una ley que plantee que un aumento del 1 % en el precio de un bien corresponde a una disminución porcentual determinada en la cantidad demandada. El impacto de un cambio concreto en el precio sobre la demanda de un bien, por parte de un individuo, se produce a través del mecanismo causal de los cambios en la utilidad evaluada de manera individual. Ese factor no es medible ni cuantificable.',

    'La experimentación reproducible sobre fenómenos económicos también es imposible. Los objetos de estudio de las ciencias naturales son la estructura y el comportamiento del mundo físico, que se asume regular, con propiedades aislables y observables mediante experimentación repetible. Pero los objetos de estudio de las ciencias sociales son las ideas y acciones de los seres humanos, que son inconmensurables y no cuantificables. La experimentación sobre fenómenos irregulares con unidades mal definidas no puede producir resultados comparables y repetibles. Tampoco es posible realizar experimentos precisos en economía, porque su objeto de estudio es la acción de los seres humanos en el mundo real, y las condiciones de los laboratorios no pueden reproducir las consecuencias de las decisiones económicas reales.',

    'Un problema más profundo de los enfoques cuantitativos es que confunden los factores que podemos medir con los factores causales que moldean el mundo. Los métodos cuantitativos que establecen relaciones entre medidas agregadas sitúan a los agregados como las fuerzas causales sin más fundamento que el hecho de que pueden medirse. En las ciencias naturales, la complejidad de las partículas que componen un gas puede reducirse a medidas agregadas básicas de presión, temperatura y volumen, sin pérdida alguna de precisión analítica. Los átomos y las moléculas no tienen voluntad propia, no pueden razonar ni elegir cómo responder al entorno. Como carecen de razón, su comportamiento se puede estudiar y predecir con precisión.',

    'Sin embargo, al examinar las cuestiones económicas, nos enfrentamos a la realidad de que los seres humanos y sus acciones son los factores causales que moldean la realidad económica, motivados por sus consideraciones subjetivas y preferencias personales. Lejos de ser objetos inanimados que reaccionan de forma matemáticamente predecible, los seres humanos reaccionan de manera irreductiblemente compleja. Tratar de disimular esta complejidad examinando sólo medidas agregadas superficiales es el principal error de pseudociencias modernas fallidas como la macroeconomía convencional. Como explica Friedrich Hayek:',

    ("quote",
     'A diferencia de lo que ocurre en las ciencias físicas, en la economía y en otras disciplinas que tratan fenómenos esencialmente complejos, los aspectos de los fenómenos que debemos explicar, sobre los que podemos obtener datos cuantitativos, son necesariamente limitados y pueden no incluir los importantes. Mientras que en las ciencias físicas el investigador podrá medir lo que considera importante de acuerdo con una teoría previa, en las ciencias sociales a menudo se trata como importante lo que resulte ser accesible a la medición. Esto se lleva en ocasiones hasta el punto de que se exige que nuestras teorías se formulen en términos que se refieran sólo a magnitudes medibles.',
     'Friedrich Hayek'),

    'El hecho de que podamos elaborar medidas de desempleo, Producto Bruto Interno, consumo, inversión y otras magnitudes económicas no significa que estos factores estén relacionados causalmente entre sí, en relaciones científicamente predeterminadas. Dado que los motores reales de estas medidas son las acciones de los individuos, no hay razón para suponer que sean algo más que epifenómenos superficiales, sin relación con los mecanismos causales que impulsan las relaciones examinadas.',

    'Intentar formular algo que tenga sentido a partir de las relaciones entre estos agregados es similar a un científico que estudia gases e intenta formular leyes basadas en el color del recipiente, la marca del recipiente, la primera letra de su nombre y otros epifenómenos sin influencia en el experimento. Los que regulan el sistema son la temperatura, la presión y el volumen que surgen de la actividad de las partículas del gas; el color del recipiente y el nombre del científico son irrelevantes. Del mismo modo, es la acción de los seres humanos la que determina los resultados económicos, no las medidas agregadas elaboradas en las oficinas de estadística de los gobiernos.',

    'Esto no quiere decir que todas las medidas estadísticas sean ruido sin valor, ya que tales agregados pueden ser buenas aproximaciones de fenómenos económicos. La objeción austriaca no se refiere a las estadísticas económicas en sí, sino al intento de construir teorías con pretensiones científicas a partir de agregados estadísticos. Los intentos más atroces y dañinos de imitar la metodología de las ciencias naturales en la economía se dan en la macroeconomía. La envidia de los macroeconomistas convencionales por la física ha alimentado, durante un siglo, la búsqueda de un sistema de ecuaciones que aclare la dinámica de una economía del mismo modo que las ecuaciones de la física explican el movimiento de los objetos. Hayek llama a esto cientificismo: la imitación servil del método y el lenguaje de la ciencia donde no es aplicable.',

    'En la macroeconomía convencional, los agregados se construyen a partir de las estadísticas nacionales, y se buscan relaciones matemáticas entre ellos. Dichas relaciones se establecen de manera teórica, basándose en la autoridad de algún economista que haya declarado cómo funcionan los mecanismos causales, no en la experimentación. El sistema macroeconómico de John Maynard Keynes es el ejemplo más destacado. Según Keynes, el estado de la economía es, ante todo, un reflejo de los niveles de gasto: si el gasto es demasiado alto, el resultado es inflación; si es demasiado bajo, desempleo y recesión. Si el desempleo es demasiado alto, las ecuaciones macroeconómicas modernas sugieren aumentar el gasto agregado mediante mayor gasto gubernamental o políticas crediticias expansivas. Una inflación elevada se solucionaría reduciendo el gasto agregado a través de impuestos o políticas crediticias contractivas.',

    'Pero las identidades contables no denotan causalidad en el mundo real. En macroeconomía no hay mecanismos para establecer experimentalmente la causalidad como en las ciencias naturales. Las ecuaciones de Keynes que intentan predecir el impacto de una medida agregada sobre otra no guardan relación con causas y efectos reales, porque no hay forma de medir, testear y verificar nada de ello.',

    'Ninguna investigación puede ensayar la hipótesis de Keynes, porque no se puede experimentar con economías enteras compuestas por millones de personas con planes de vida individuales. Incluso al observar las estadísticas gubernamentales recopiladas por los partidarios de la teoría, la experiencia real ha contradicho la teoría durante décadas. El sistema keynesiano implica una relación inversa entre desempleo e inflación, llamada curva de Phillips, que se supone descendente. Pero la experiencia en el mundo real contradice esta idea, ya que la figura 1, con datos de sesenta años de estadísticas del gobierno de Estados Unidos, no muestra tal <em>trade-off</em>.',

    ("figure", phillips_svg(), "Figura 1 · Inflación y desempleo en Estados Unidos (61 años). La nube de puntos no muestra ninguna pendiente descendente: no hay <em>trade-off</em> visible."),

    'Sin embargo, esta teoría persiste hasta el día de hoy, a pesar de décadas de evidencia acumulada que prueban que no es una explicación correcta de cómo funciona el mundo. En los setenta, cuando la inflación y el desempleo aumentaron al mismo tiempo en todo el mundo, el <em>trade-off</em> keynesiano quedó ampliamente refutado más allá de toda duda. Pero la ventaja de que la economía no disponga de un método sistemático y reproducible de experimentación es que las teorías siempre pueden ajustarse tras su fracaso, de forma que puedan justificar las observaciones del mundo real que no se ajustan a ellas. Esa es la esencia de la pseudociencia.',

    'Lo gracioso es que los keynesianos simplemente actualizaron su teoría agregando un nuevo término: el «shock de oferta». El shock de oferta es un término incoherente, inventado como justificación a posteriori para explicar cómo pueden producirse simultáneamente aumentos del desempleo y la inflación. Desde entonces, las economías del mundo han sido testigos de todas las combinaciones imaginables de tasas de inflación y desempleo, y los keynesianos han mantenido con éxito el engaño de que existe tal <em>trade-off</em>. Cualquier desviación puede explicarse invocando un shock de oferta u otras alternativas a la razón, por lo que ninguna observación puede refutarlo. Lo explica todo y, por lo tanto, no explica nada.',

    'Tras un siglo de imitar a la física y de haber abandonado los fundamentos metodológicos clásicos, la economía no ha logrado producir ni una sola ley o fórmula cuantitativa que pueda testearse y reproducirse de forma independiente. Las ecuaciones macroeconómicas van y vienen con las modas de las escuelas de pensamiento modernas, pero ninguna se ha medido objetivamente y reproducido de forma que pueda calificarse como ley científica. Que la macroeconomía convencional dé poder a los gobiernos centrales y enriquezca a los académicos ayudaría a explicar por qué ha perdurado.',

    # ============== 1.4 ==============
    ("section", "Un contraste de enfoques"),

    'Para ilustrar el enfoque basado en la acción humana y compararlo con la metodología cuantitativa moderna, podemos utilizar como ejemplo la cuestión de los salarios mínimos impuestos por el gobierno, que fijan un límite inferior a lo que los empleadores pueden pagar a sus trabajadores. Se trata de una intervención política popular en la mayor parte del mundo, y las perspectivas opuestas sirven de lección práctica sobre los dos marcos diferentes para pensar la economía: las relaciones entre agregados y la acción humana.',

    'Imaginemos a una política que quiere ganar las elecciones en un país sin ley de salario mínimo. Existe una variación natural en los salarios que ganan los trabajadores. La política decide focalizar su campaña en la mejora del nivel de vida de los miembros más pobres mediante la imposición de un salario mínimo de diez dólares por hora, que imagina garantizará a sus beneficiarios una vida digna. Un economista a su servicio observa que el 20 % de todos los trabajadores, que mantienen al 35 % de toda la población, ganan actualmente menos de diez dólares por hora. El efecto agregado de imponer el salario mínimo conduciría a un aumento de los salarios equivalente a 10 mil millones de dólares al año. Siguiendo sofisticados modelos históricos y teóricos, el economista fíat estima que el aumento se traducirá en un aumento de 8 mil millones de dólares en el gasto de los consumidores, lo que implicaría la creación de 40 mil nuevos puestos de trabajo, un aumento del 12 % en la producción industrial, del 4 % en las exportaciones y de 16 mil millones de dólares en el producto bruto interno.',

    'Según este enfoque colectivista, los agregados son los agentes causales de los fenómenos económicos y actúan de acuerdo con las relaciones teóricas establecidas por los economistas fíat, de forma similar a como los físicos y químicos establecen leyes científicas. La ley de salario mínimo suena como una gran bendición para la sociedad: los trabajadores más pobres aumentarán considerablemente su nivel de vida, algunos desempleados encontrarán trabajo gracias al gasto adicional y toda la sociedad será más productiva.',

    'Si esto parece demasiado bueno para ser cierto, es porque no es cierto. Las cosas se ven de otra manera a través de la lente misesiana del economista sensato. Al saber que la acción humana es el verdadero motor de los asuntos humanos, el economista sensato no analiza el mundo a través de relaciones entre cantidades agregadas. En su lugar, estudia las decisiones de los seres humanos reales afectados por esta nueva ley. El empleo es un acuerdo entre dos individuos: el empleador y el empleado. El empleador contratará a alguien si su contribución a los ingresos de la empresa supera su salario. Si el salario mínimo legal supera los ingresos marginales que aporta, contratarlo le cuesta dinero a la empresa y se convierte en una donación de la empresa al trabajador. Los empleadores saben que contratar a alguien así es un error costoso, y los que no lo sepan pronto verán cómo su empresa fracasa.',

    'Los salarios, como todos los precios del mercado, no son cifras arbitrarias elegidas por empleadores codiciosos. Son un reflejo de la productividad marginal del trabajador. Cuando el gobierno impone un salario mínimo, no altera mágicamente el cálculo del empleador, ni aumenta mágicamente la productividad del trabajador. El empleador seguirá contratando únicamente a trabajadores cuya productividad sea superior a su salario. Así, la ley de salario mínimo hace que sea ilegal contratar a cualquier persona cuya productividad marginal sea inferior a diez dólares por hora. Cualquier trabajador cuya productividad sea inferior a esa cantidad se convertirá en un lastre para cualquier empresa que lo contrate y le pague esa cantidad. O lo despiden, o la empresa quiebra. En todos los casos, estos puestos de trabajo se eliminan, y todo aquel cuya productividad sea inferior a diez dólares por hora es ahora legalmente no empleable.',

    'Visto a través de la lente de la acción humana, el efecto de una ley de salario mínimo es hacer que sea ilegal que los trabajadores con baja productividad consigan trabajo. Los que pierden su empleo son los que tienen la productividad más baja de la sociedad: suelen ser los más pobres, los más jóvenes y los que tienen menos experiencia. Prohibirles trabajar es prohibirles aumentar su productividad aprendiendo en el trabajo. Por lo tanto, las leyes de salario mínimo son especialmente perniciosas para las personas que más necesitan trabajar, y son un factor causal de la aparición del desempleo a gran escala. Otra implicación es que algunas empresas pagarían salarios más altos, pero también subirían los precios de sus productos para financiarlos. Los consumidores pagarían el precio de la ley a través de un aumento de los precios de los bienes que consumen.',

    'Todas estas consecuencias son deducibles por economistas sensatos que analizan las leyes y evalúan las implicaciones que tendrán en individuos que actúan racionalmente. Los precios son un reflejo de la realidad del mercado que subyace a la situación, una realidad impulsada por la acción humana. Intentar alterar la realidad del mercado subyacente alterando su reflejo es inviable. Todos los intentos de imponer controles de precios han fracasado porque este tipo de planificación centralizada ignora el papel de la acción humana. Los reyes, emperadores, políticos y burócratas ordenan que los epifenómenos observables asociados a los mercados se sitúen dentro de rangos aceptables. Suponen que los seres humanos simplemente se limitarán a ajustar sus acciones para garantizar el cumplimiento de estas leyes. Pero en realidad, los seres humanos ajustan sus acciones para optimizar su propio bienestar, no para satisfacer a los burócratas. El comerciante prefiere no vender a vender con pérdidas. O existe el precio de libre mercado o no existe ningún precio de mercado. En esta última economía, los precios reales se expresan en mercados clandestinos, es decir, en los «mercados negros».',

    'Los economistas de verdad entienden que los fenómenos económicos observables no son más que manifestaciones de las acciones subyacentes de los seres humanos involucrados. Los seres humanos siempre buscan mejorar su propia situación en la vida, y resulta inútil obligarlos a actuar en contra de sus propios intereses. La imposición de leyes contrarias al propio interés de los seres humanos no cambia la naturaleza humana, sino que reduce el incentivo para comportarse conforme a la ley, destruyendo así el respeto de la sociedad por las leyes. Esta comprensión esencial es la razón por la que el economista sensato está a favor de la libertad económica individual y en contra de su restricción por parte de los gobiernos. El espíritu humano es indomable, y no actuará de un modo perjudicial para sí mismo.',

    'El mundo ya cuenta con demasiados libros de texto de economía escritos en la tradición cuantitativa pseudocientífica. Este libro no será uno de ellos. No tratará de explicar la economía en el lenguaje de las ciencias naturales y no contendrá ecuaciones que relacionen variables agregadas. Tales enfoques prometen mucho, pero aportan poco en términos de conocimientos confiables, útiles y aplicables.',
]

# CSS extra: subtítulos de sección + citas en bloque + figuras SVG
EXTRA_CSS = """
/* ===== Subtítulos de sección ===== */
.prose h2.section-subtitle {
  font-family: var(--font-body); font-weight: 400;
  font-size: 1.15rem; letter-spacing: 0.02em;
  color: var(--ink); margin: 2.6rem 0 0.9rem;
  padding-bottom: 0.5rem; border-bottom: 1px solid var(--rule);
}
/* ===== Citas en bloque — filete fino a la izquierda ===== */
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
/* ===== Figuras / gráficos en el formato del libro ===== */
.prose .chart-fig {
  margin: 2.6rem 0;
  padding: 0;
  text-align: center;
}
.prose .chart-fig svg {
  width: 100%; max-width: 640px; height: auto;
  display: block; margin: 0 auto;
}
.prose .chart-fig .figcaption {
  margin: 1rem auto 0;
  max-width: 34rem;
  font-size: 0.86rem; font-style: italic; line-height: 1.55;
  color: var(--ink-soft); text-align: center;
}
.phillips-chart .grid  { stroke: var(--rule);     stroke-width: 0.8; fill: none; }
.phillips-chart .axis  { stroke: var(--ink-soft); stroke-width: 1.2; fill: none; }
.phillips-chart .tick-label  { fill: var(--ink-soft); font-size: 12px;
  font-family: var(--font-body); font-variant-numeric: tabular-nums; }
.phillips-chart .axis-title  { fill: var(--ink); font-size: 13px;
  font-style: italic; font-family: var(--font-body); }
.phillips-chart .pt    { fill: var(--verde); opacity: 0.88; }
"""


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
            # aside.no-audio para que extract_text.py salte TODA la figura
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
    # nav-foot: no hay prev (es el cap 1), next = valor (cap 2, por escribir)
    new_nav = ('<nav class="nav-foot">'
               '<a class="prev" href="index.html">Índice</a>'
               '<a class="idx" href="index.html">Índice</a>'
               '<span></span></nav>')
    out = re.sub(r'<nav class="nav-foot">.*?</nav>',
                 lambda _m: new_nav, out, count=1, flags=re.DOTALL)
    out = out.replace('audio/tres-regimenes.mp3', 'audio/accion-humana.mp3')
    out = out.replace('audio/tres-regimenes.alignment.json',
                      'audio/accion-humana.alignment.json')
    out = out.replace('data-storage-key="tres-regimenes"',
                      'data-storage-key="accion-humana"')
    out = out.replace('</style>', EXTRA_CSS + '</style>', 1)

    open('accion-humana.html', 'w', encoding='utf-8').write(out)
    n_par = sum(1 for it in CONTENT if isinstance(it, str) or (isinstance(it, tuple) and it[0] == "lead"))
    n_sec = sum(1 for it in CONTENT if isinstance(it, tuple) and it[0] == "section")
    n_q = sum(1 for it in CONTENT if isinstance(it, tuple) and it[0] == "quote")
    n_fig = sum(1 for it in CONTENT if isinstance(it, tuple) and it[0] == "figure")
    print(f"accion-humana.html creado: {n_par} párrafos, {n_sec} secciones, {n_q} citas, {n_fig} figura(s)")


if __name__ == "__main__":
    main()
