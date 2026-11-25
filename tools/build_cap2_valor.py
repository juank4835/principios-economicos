#!/usr/bin/env python3
"""Construye el cap 2 «Valor» de Principios Económicos.

Capítulo con dos niveles de encabezado:
  - 2.1 ... 2.10 → h2 "section-subtitle"
  - 2.1.1 ... 2.1.6 → h3 "section-subsubtitle" (dentro de 2.1)

Sin notas al pie.
"""
import re

EYEBROW = "Parte I · Fundamentos"
TITLE = "Valor"
SUBTITLE = "Saifedean Ammous — Principios de Economía"

# Items soportados:
#   "texto"                   → párrafo normal <p>
#   ("lead", texto)           → primer párrafo con capital <p class="lead">
#   ("section", título)       → h2.section-subtitle (2.1, 2.2, ...)
#   ("subsection", título)    → h3.section-subsubtitle (2.1.1, 2.1.2, ...)
#   ("quote", texto, cite)    → cita en bloque; cite no se narra
CONTENT = [
    # Epígrafe
    ("quote",
     'Así pues, el valor no es algo inherente a los bienes, ni una propiedad de los mismos, ni una cosa independiente que exista por sí misma. Es un juicio que hacen los hombres economizadores sobre la importancia de los bienes que disponen para la conservación de su vida y de su bienestar. Por lo tanto, el valor no existe fuera de la conciencia de los hombres.',
     'Carl Menger'),

    # Intro
    ("lead",
     'El primer capítulo fue una introducción metodológica al campo de la economía, ilustrando el enfoque austriaco centrado en la acción humana. En este capítulo pasamos a la esencia de la economía, sus conceptos fundamentales y las principales cuestiones que trata de abordar.'),

    'El economista austriaco Carl Menger sentó las bases de la economía moderna a finales del siglo XIX. Aunque la economía como campo de investigación existía desde los tiempos de Aristóteles, la explicación de Menger de la naturaleza subjetiva del valor y de las decisiones económicas, y su introducción del análisis marginal, revolucionaron el campo y le dieron una sólida base teórica y metodológica, permitiendo un análisis sistemático de cómo los seres humanos economizan y actúan. <em>Principios de Economía</em>, escrito en 1871, tal vez sea el libro de texto de economía más antiguo que sigue siendo relevante y legible. Este capítulo resume los conceptos fundamentales sobre los que Menger construyó el análisis económico: el valor subjetivo y el análisis marginal.',

    # ============== 2.1 Utilidad y valor ==============
    ("section", "Utilidad y valor"),

    ("subsection", "Bienes"),
    'Menger define un bien como algo útil que podemos destinar a la satisfacción de necesidades humanas. Para que algo se convierta en un bien, primero es necesario que exista una necesidad humana; segundo, que las propiedades del bien puedan causar la satisfacción de esa necesidad; tercero, que los seres humanos tengan conocimiento de esta conexión causal y, por último, que tener control sobre el bien sea suficiente para destinarlo a la satisfacción de la necesidad humana.',

    ("subsection", "Utilidad"),
    'La utilidad es la capacidad de un bien para satisfacer necesidades humanas. La utilidad depende de nuestra capacidad para comprender la conexión entre un bien y la necesidad que satisface. La utilidad es un prerrequisito general para que un objeto sea un bien. Sólo si algo puede ofrecer utilidad puede ser considerado un bien por los seres humanos.',

    ("subsection", "Escasez"),
    'Los bienes pueden dividirse en dos categorías: económicos y no económicos. La distinción entre ambos es la escasez: la demanda de bienes económicos es siempre superior a la cantidad ofrecida; mientras que, en el caso de los bienes no económicos, su oferta siempre supera las cantidades demandadas por los seres humanos.',
    'Un bien no económico es un bien disponible en cantidades superiores a la demanda del mismo, lo cual imposibilita que haya rivalidad o competencia por obtenerlo. El mejor ejemplo es el aire, que es esencial para la supervivencia humana, pero que, sin embargo, abunda en todas partes donde viven los seres humanos. El aire no es, por lo tanto, un bien económico.',
    'Un bien económico, al ser escaso, tiene una demanda mayor que su oferta, y esto crea rivalidad en torno a su acceso, obligando a los seres humanos a elegir entre él y otros bienes. La escasez obliga a los seres humanos a <em>economizar</em>, a elegir entre alternativas escasas: a conservar las funciones útiles de los bienes, a priorizar las necesidades más urgentes sobre las menos urgentes, y a obtener la mayor satisfacción de la menor cantidad posible de cada uno.',

    ("subsection", "Economía"),
    'La economía, como disciplina, es el estudio de las decisiones humanas en situaciones de escasez. Se centra en analizar cómo los seres humanos intentan encontrar soluciones al problema de la disparidad entre lo que tienen y lo que quieren, y las consecuencias de sus elecciones.',
    'Dado que la escasez es una condición permanente de la existencia, los seres humanos están constantemente eligiendo entre distintos cursos de acción, distintos bienes y distintas necesidades que satisfacer. La necesidad de elegir nos obliga a considerar y comparar la utilidad de los distintos bienes para poder tomar decisiones informadas.',

    ("subsection", "Valor"),
    'El valor es nuestra apreciación subjetiva de la satisfacción que obtenemos, o esperamos obtener, de los bienes, y lo que nos permite tomar decisiones económicas. Menger define el valor como «la importancia que los bienes individuales o cantidades de bienes adquieren para nosotros, cuando somos conscientes de que dependemos de ellos para la satisfacción de nuestras necesidades». El valor es también «la importancia que atribuimos antes que nada a la satisfacción de nuestras necesidades, es decir, a nuestra vida y bienestar, y que, en consecuencia, trasladamos a los bienes económicos como causas exclusivas de la satisfacción de nuestras necesidades».',

    ("subsection", "Subjetividad del valor"),
    'El fundamento del análisis económico, y una de las ideas innovadoras de la obra de Menger, es que el valor es subjetivo. Sólo existe en la mente de la persona que hace la valoración. En palabras de Menger: «el valor no es algo inherente a los bienes, ni una propiedad de los mismos, ni una cosa independiente que exista por sí misma. Es un juicio que hacen los hombres economizadores sobre la importancia de los bienes que disponen para la conservación de su vida y de su bienestar».',
    'No es la naturaleza inherente de los bienes lo que los hace valiosos para nosotros, sino sólo nuestra evaluación de su idoneidad para satisfacer nuestras necesidades. A medida que cambia su capacidad de satisfacer nuestras necesidades, también cambia su valor para nosotros. El valor no es una propiedad física o química de los bienes económicos, sino una propiedad psíquica que sólo adquieren cuando los seres humanos los evalúan. Como dijo Menger: «el valor no existe fuera de la conciencia de los hombres».',
    'El ejemplo favorito de Ammous para ilustrar esta naturaleza subjetiva es el petróleo. Hasta el siglo XIX, la presencia de petróleo en un terreno disminuía su valor, ya que requería una costosa extracción antes de que el terreno pudiera utilizarse para fines agrícolas, comerciales o residenciales. Mientras la conciencia humana consideraba el petróleo como una molestia sucia, el petróleo tenía un valor económico negativo. Una vez que los humanos se dieron cuenta de que el petróleo refinado podía quemarse en un motor de combustión interna para alimentar máquinas que satisficieran sus necesidades de transporte, electricidad y generación de calor, el petróleo pasó de ser una costosa molestia a convertirse en un bien enormemente valioso y esencial. El petróleo del año 2020 no difiere química ni físicamente del petróleo del año 1620 y, sin embargo, su valor ha pasado de negativo a positivo. En palabras de Menger: «El valor de los bienes surge de su relación con nuestras necesidades, y no es inherente a los propios bienes. Al cambiar esta relación, el valor surge y desaparece».',
    'Un caso más reciente lo refuerza. En 2020, con buena parte del mundo bajo suspensiones de movimiento y producción, el petróleo —que se produce para su consumo inmediato y tiene muy poca capacidad de almacenamiento— no tenía adónde ir. El precio cayó en picada e incluso llegó a ser negativo durante unos días: poseer petróleo volvió a ser una carga y sus propietarios tuvieron que pagar para librarse de él. Nada cambió en las propiedades inherentes del petróleo cuando su precio pasó de positivo a negativo y otra vez a positivo; cambiaron las condiciones de quienes lo valoraban.',
    'El valor no puede existir fuera de la valoración y la elección humanas, que reflejan sus preferencias. El valor no puede ser una propiedad constante de los objetos; es un fenómeno consciente en nuestras mentes. Esto no significa que no sea real: el valor es real y significativo, y moldea nuestras acciones para dirigir la producción, el consumo y la utilización de los objetos materiales del mundo. El reconocimiento de Menger de la naturaleza subjetiva del valor fue un punto de inflexión en el pensamiento económico. A los economistas anteriores les había costado explicar cómo se valoraban los bienes y por qué ciertos bienes eran más valiosos que otros. Todos estos misterios sólo se resolvieron con la visión mengeriana de la valoración subjetiva y el análisis marginal.',

    # ============== 2.2 ==============
    ("section", "Valoración: ordinal y cardinal"),

    'La primera consecuencia importante de la naturaleza subjetiva del valor es que no puede medirse ni expresarse objetivamente. Dado que la valoración es subjetiva para el ser humano que la realiza, y dado que cambia constantemente en función de sus necesidades y de su comprensión de la capacidad de los bienes para satisfacerlas, las valoraciones difieren de una persona a otra y de un momento a otro. Para expresar cualquier medida de forma objetiva, se necesita una unidad científica que sirva de patrón: el peso, la longitud, la temperatura se expresan en unidades definibles de manera objetiva y que permiten comparar con precisión distintos objetos. Pero no puede existir tal unidad para la valoración humana, ya que la valoración de un bien no es una propiedad objetiva inherente al bien, sino una propiedad psíquica dependiente de la persona que valora y de condiciones siempre cambiantes.',
    'Sin una unidad común, la valoración no puede expresarse en términos numéricos cardinales objetivos, y es imposible medir el valor económico con precisión matemática. Una persona que quiere instalar una nevera en una cocina puede medir el espacio asignado en centímetros y luego buscar las dimensiones de la nevera para ver si cabe: esta medida tiene sentido porque el cliente y el fabricante comparten una definición clara y precisa de lo que es el centímetro. Sin acordar una unidad común, sería imposible saber si la nevera cabría sin instalarla.',
    'Sin esa unidad común, la única forma de expresar la valoración es en términos <em>ordinales</em>: comparando los bienes entre sí y ordenándolos según las preferencias de quien valora, pero sin asignarles valores cuantitativos explícitos. Es posible saber si uno valora el bien A más que el bien B, y el bien B más que el bien C, porque hay una constante para la comparación: el individuo que valora. Pero es imposible expresar esas preferencias con cifras precisas en una misma unidad, como si dijera «el valor de A = 14 372 unidades, el de B = 4 258, y el de C = 1 273». Esa unidad no existe.',

    ("quote",
     'La eliminación de la insatisfacción sentida puede lograrse en una mayor o menor medida, pero cuánto supera una satisfacción a otra es algo que sólo puede sentirse. No puede establecerse ni comprobarse de manera objetiva. Un juicio de valor no mide, sino que ordena en una escala de grados, califica. Es expresivo de un orden de preferencia y secuencia; no expresa medida ni peso. Sólo se le pueden aplicar los números ordinales; nunca los cardinales.',
     'Mises'),

    'Piense en cómo valora personalmente las cosas en relación con otras. ¿Es capaz de expresar esas valoraciones en términos de una unidad que las cuantifique a todas? Todas las cosas que usted valora —desde los bienes materiales hasta las amistades, la familia y la felicidad— ¿pueden medirse en términos de una misma unidad? ¿Existe un tipo de cambio fijo entre un miembro de su familia y bienes materiales? ¿Cuántos automóviles necesita un ser humano a cambio de su hijo? Las valoraciones humanas no pueden medirse con una unidad estandarizada. Sólo pueden compararse, pero no sumarse, restarse ni multiplicarse. Sin una unidad común y constante, la medición y las operaciones matemáticas no son posibles.',

    # ============== 2.3 ==============
    ("section", "Valor y precio"),

    'El valor de los bienes económicos es distinto de su precio y no debe confundirse con éste. El precio al que se realiza una venta no es la valoración objetiva del bien, ni la valoración subjetiva de ninguna de las partes de la transacción. Sólo ilustra que el vendedor valora el bien <em>menos</em> que el precio, mientras que el comprador lo valora <em>más</em> que el precio. Si no fuera así, la transacción no se habría realizado.',

    'Un error común en economía es confundir valor y precio, y suponer que el valor puede medirse objetivamente, expresado en unidades monetarias. Pero cuando alguien acepta vender un bien por mil dólares, está demostrando que lo valora en menos de mil dólares; si lo valorara en más, no habría aceptado. Cuando el comprador se deshace de mil dólares para adquirirlo, su valoración es necesariamente superior a mil dólares, pues de lo contrario no habría pagado esa suma. No es posible determinar la valoración exacta que un individuo le da a un bien a partir de su transacción; sólo sus límites superior o inferior. El mero acto de intercambio nos dice mucho sobre la valoración.',

    # ============== 2.4 ==============
    ("section", "Libre intercambio"),

    'Cada vez que dos personas deciden voluntariamente intercambiar bienes económicos, debe ser cierto que ambas creen que se beneficiarán del intercambio; de lo contrario, no lo harían. Un intercambio mutuamente beneficioso indica que cada parte ha recibido algo que valora más que lo que ha cedido. La única forma de que esto sea posible es entendiendo que ambas tienen valoraciones subjetivas diferentes del bien intercambiado. Si el valor de los bienes fuera objetivo, no diferiría de una persona a otra, y el intercambio no sería posible, porque ninguna elegiría aceptar el bien de menor valor objetivo a cambio del de mayor valor objetivo. Esto se tratará con más detalle en el capítulo 9, sobre el comercio.',

    # ============== 2.5 ==============
    ("section", "Determinantes del valor"),

    'La diferencia fundamental entre los economistas de la escuela austriaca y los de otras escuelas es que los austriacos consideran el valor como algo subjetivo, mientras que los de otras escuelas lo conciben como algo objetivo u objetivamente medible. Para mantener esa pretensión, algunos libros de texto modernos definen el valor como una función de la utilidad, medida en una unidad imaginaria e indefinida llamada <em>útil</em>. No existe ningún patrón sobre lo que constituye una útil, ni forma de medir nada en términos de útiles. Algunos economistas matemáticos expresan el valor en términos numéricos explícitos, medidos en unidades monetarias, confundiendo así valor con precio. Los marxistas, por su parte, piensan que el valor viene determinado por el trabajo dedicado a la producción de un bien, una idea absurda según la cual las cosas adquieren valor si se dedica trabajo a producirlas, independientemente de que alguien quiera poseerlas. Si se dedicara el mismo tiempo a hornear una tarta normal y una tarta de barro, el marxista sostendría que ambas tendrían el mismo valor.',

    'La noción de que el trabajo determina el valor tiene un atractivo intuitivo. Vemos que los bienes económicos siempre requieren algún elemento de trabajo para satisfacer las necesidades humanas. Incluso las frutas que crecen en la naturaleza requieren el trabajo de recogerlas y comerlas antes de poder satisfacer el hambre. Esto lleva a los defensores de la teoría del valor-trabajo a concluir que es el trabajo lo que da valor a los bienes. Pero la noción es insostenible: los bienes sólo se valoran por su capacidad de satisfacer nuestras necesidades. A un comprador no le interesa saber cuánto tiempo y esfuerzo se invirtió en fabricar un producto cuando lo adquiere, sino sólo los servicios y la utilidad que el producto le proporciona. Se trabaja para producir bienes porque se espera que produzcan un resultado valioso para el consumidor; el trabajo no hace que las cosas sean valiosas por arte de magia. Es posible dedicar trabajo a un proceso de producción fallido que no produzca nada utilizable, y el producto no adquirirá valor sólo por el esfuerzo invertido. No hay correspondencia garantizada entre trabajo empleado y valor de lo producido: sólo la elección de los consumidores en el mercado puede emitir ese juicio.',

    'Desde la perspectiva austriaca, el valor es subjetivo y depende del momento y el lugar en que se realiza la valoración. Se deriva de la elección humana, que es necesaria por la escasez. Lo asignan los individuos a cada unidad en el momento y el lugar en que toman decisiones; no es una propiedad universal del bien. Sin una concepción subjetiva del valor, no es posible encontrar explicaciones coherentes de por qué y cómo los seres humanos toman las decisiones económicas que toman.',

    # ============== 2.6 ==============
    ("section", "Marginalismo"),

    'La otra contribución trascendental de Menger a la economía es el concepto de <em>marginalismo</em>. Tras establecer que el valor de los bienes no es inherente a ellos, sino subjetivo y dependiente de su capacidad para satisfacer nuestras necesidades, Menger lo aplicó al estudio del valor de distintas unidades de un mismo bien y, en el proceso, sentó las bases del análisis económico moderno.',

    'Dado que el valor se deriva de la satisfacción que proporciona un bien, y dado que las distintas satisfacciones tienen un valor desigual para nosotros, el valor de distintas unidades de un mismo bien también será desigual: dependerá de la satisfacción concreta que cada unidad aporta. Un mismo bien tendrá un valor diferente para una misma persona según la necesidad que satisfaga en un momento dado. Los individuos destinan la primera unidad a satisfacer las necesidades más importantes y urgentes; la segunda, a la segunda más urgente; y así sucesivamente. A medida que aumentan sus reservas, las necesidades que esas unidades satisfacen son menos valiosas y menos urgentes. Cada unidad marginal es menos valiosa que la anterior.',

    # ============== 2.7 ==============
    ("section", "Utilidad marginal"),

    'Si bien Menger nunca usó el término, su alumno Friedrich von Wieser introdujo más tarde la expresión <em>utilidad marginal</em> para referirse a la importancia concedida a la satisfacción menos importante obtenida por una sola unidad de la cantidad disponible de un bien. Mises lo definió así: «Llamamos uso menos urgente o uso marginal al uso de una unidad de una provisión homogénea que un hombre realiza si su provisión es de n unidades, pero que no realizaría si, en igualdad de condiciones, su provisión fuera sólo de n-1 unidades, y llamamos utilidad marginal a la utilidad derivada de tal uso».',

    'Por ejemplo, la primera unidad de alimento que ingiere una persona es extremadamente valiosa: es la diferencia entre la inanición y la supervivencia. La segunda será la diferencia entre la mera supervivencia y estar bien alimentado; sigue siendo muy valiosa, pero menos que la primera. Las unidades posteriores se adquirirán para disfrutar del sabor o para reuniones sociales, menos valiosas que las anteriores. Al final llega un punto en el que el individuo no asigna ningún valor a una unidad extra y prefiere prescindir de ella aunque se la ofrezcan gratis. Cada unidad sucesiva se destina a satisfacer necesidades menos urgentes y tiene, por tanto, una utilidad menor.',

    'Con esta idea, Menger refutó la noción de que el valor es inherente a los bienes como tales. Demostró que el valor depende de las necesidades que satisfacen, que a su vez dependen de la abundancia o escasez del bien, y sólo para la persona que valora. Nunca se pide a nadie que valore el suministro total de un bien ni que valore un bien en abstracto: las decisiones económicas se refieren a unidades individuales, y las personas deciden sobre la <em>siguiente</em> unidad que desean consumir, no sobre su provisión a lo largo de toda la vida.',

    # ============== 2.8 ==============
    ("section", "Ley de la utilidad marginal decreciente"),

    'Una consecuencia importante del enfoque de Menger es la <em>ley de la utilidad marginal decreciente</em>. Esta ley establece que la valoración y la utilidad que un individuo obtiene de un bien disminuirán a medida que aumente la cantidad del bien que posee. Como los individuos utilizan las primeras unidades para satisfacer las necesidades más urgentes, la primera unidad será la más valorada. A medida que aumentan sus reservas y cada unidad marginal se destina a una necesidad menos urgente, cada unidad marginal tendrá un valor menor.',

    'La disminución de la utilidad marginal es una idea importante para la toma de decisiones. Cualquiera que haya hecho una compra cara puede sentirse identificado. El primer día que uno tiene un automóvil o un juguete nuevo, el factor novedad es abrumador y lo cautiva. Con el paso del tiempo, la sensación disminuye a medida que uno se acostumbra. Lo que era novedoso se convierte en común y pierde el encanto inicial. Uno todavía disfruta conduciendo el automóvil o jugando con el juguete, pero el disfrute disminuye con cada uso adicional.',

    'La ley de la utilidad marginal decreciente es otro recordatorio de que no existe un valor objetivo del bien X: ese valor cambia según la abundancia del bien y las necesidades que satisface. Lo que existe es la valoración subjetiva de la siguiente unidad —la marginal— para la persona que valora, y depende de sus preferencias y de la abundancia del bien.',

    # ============== 2.9 ==============
    ("section", "Valoración por el uso menos valioso"),

    'Otra consecuencia del enfoque de Menger es la siguiente: a medida que los individuos destinan sus reservas a satisfacer sus necesidades más urgentes, su valoración de la unidad marginal reflejará la valoración de la satisfacción <em>menos</em> importante que este bien asegura. Un hombre que decide pagar por una comida no pagará en función de cuánto valora la comida en abstracto ni de cuánto valora toda la comida que ha consumido a lo largo de su vida. Pagará en función del valor que conceda a la próxima comida en sí. Al tratarse de una sola comida, será considerablemente inferior al valor de las comidas que lo mantienen con vida en general. Cuando las personas tienen que elegir sobre un bien concreto, lo valoran a la luz del uso menos valioso posible, porque ésa es la única opción que existe en el margen: todos los usos más valiosos ya fueron satisfechos con las unidades anteriores.',

    'La persona que se plantea comprar una botella de agua en un restaurante, por ejemplo, no va a pagar en función del valor que obtiene del agua para sobrevivir. Simplemente está decidiendo sobre la próxima unidad marginal de agua que consume, habiendo destinado ya otras unidades a sus necesidades más urgentes. El precio pagado no se acercará en absoluto al valor que el individuo atribuye a la supervivencia, porque la decisión se refiere al consumo de una botella de agua adicional, no a la supervivencia. Esto nos ayuda a entender por qué el agua es relativamente barata a pesar de ser esencial.',

    'En el mundo moderno, las personas no pagan por el agua en función del valor que conceden a la supervivencia. Viven ya en una época y un lugar que cubre sus necesidades más importantes a precios muy bajos. Sus decisiones de compra marginales se refieren a cantidades que pueden aliviar una sed leve, pero que no influyen en la supervivencia. Si pusiéramos a un individuo en una situación en la que no pudiera conseguir agua durante unos días, el uso menos valioso que le ofrecería sería la diferencia entre la vida y la muerte, y eso haría que la valore enormemente.',

    ("quote",
     'El hombre que actúa no se encuentra en una posición en la que deba elegir entre todo el oro y todo el hierro. Elige en un momento y lugar determinados y en unas condiciones determinadas entre una cantidad estrictamente limitada de oro y una cantidad estrictamente limitada de hierro. Su decisión de elegir entre cien onzas de oro y cien toneladas de hierro no depende en absoluto de la decisión que tomaría si se encontrara en la situación altamente improbable de elegir entre todo el oro y todo el hierro. Lo único que cuenta para su elección real es si, en las condiciones existentes, considera que la satisfacción que podrían proporcionarle cien onzas de oro es mayor o menor que la que podría obtener de cien toneladas de hierro. Cuando afronta el problema del valor que debe atribuirse a una unidad de una provisión homogénea, el hombre decide basándose en el valor del uso menos importante que hace de las unidades de toda la provisión; decide basándose en la utilidad marginal.',
     'Mises'),

    # ============== 2.10 ==============
    ("section", "La paradoja del diamante y el agua"),

    'La importancia inmediata del análisis marginal de Menger radica en que fue la primera solución económica a la paradoja del diamante y el agua, cuya explicación había eludido a los economistas durante siglos. ¿Cómo podían explicar que el agua, esencial para la vida humana, fuera por lo general muy barata, si no gratuita, mientras que los diamantes, que no sirven para ningún propósito esencial, fueran muy caros? Si el valor es subjetivo, ¿por qué las personas dan tanto valor a cosas triviales que no necesitan, como los diamantes, mientras dan poco valor a bienes esenciales como el agua? ¿No encajaría esto más con una teoría del valor-trabajo?',

    'Sin embargo, el valor de mercado no se refiere a alguna propiedad inherente al bien ni al valor que nos proporcionan todas sus reservas: se basa en la menos importante de las satisfacciones que proporciona el bien. Dado que el agua potable suele estar disponible en grandes cantidades en cualquier lugar donde se asienten seres humanos, las necesidades más urgentes de agua ya están cubiertas, y se están tomando decisiones de mercado sobre unidades que satisfacen necesidades mucho menos urgentes. Si una persona en una ciudad moderna renuncia a comprar una botella de agua, sólo está renunciando a una pequeña necesidad en un momento determinado; seguirá teniendo acceso al agua que necesita para sus necesidades más urgentes. En cambio, los diamantes, al ser muy raros y estar disponibles en cantidades muy pequeñas, son adquiridos por personas que los destinan a algunos de sus usos más valiosos.',

    'Es posible imaginar un escenario en el que tanto el agua como los diamantes son muy escasos, y las unidades marginales de ambos se destinarían a satisfacer las necesidades más urgentes. Un hombre abandonado en un desierto que lleva días sin beber estaría dispuesto a pagar un precio mucho más alto por la primera unidad de agua que por la primera unidad de diamante, ya que para él el agua sería la diferencia entre la vida y la muerte.',

    'Por lo tanto, es erróneo afirmar que los diamantes son más valiosos que el agua. La paradoja del diamante y el agua ilustra la importancia de las circunstancias individuales en la evaluación subjetiva del valor. En situaciones en las que el agua es abundante y los diamantes son escasos, el agua destinada a sus usos menos valiosos es menos valiosa que los diamantes, cuya escasez garantiza que sus usos menos valiosos sigan siendo muy valiosos. En situaciones en las que el agua es lo suficientemente escasa como para que la unidad marginal se destine a la supervivencia, el agua sería sin duda más valiosa que los diamantes.',
]

# CSS extra: subtítulos + sub-subtítulos + citas
EXTRA_CSS = """
/* ===== Subtítulos de sección (h2) ===== */
.prose h2.section-subtitle {
  font-family: var(--font-body); font-weight: 400;
  font-size: 1.15rem; letter-spacing: 0.02em;
  color: var(--ink); margin: 2.6rem 0 0.9rem;
  padding-bottom: 0.5rem; border-bottom: 1px solid var(--rule);
}
/* ===== Sub-subtítulos (h3, para 2.1.1, 2.1.2, ...) ===== */
.prose h3.section-subsubtitle {
  font-family: var(--font-body); font-weight: 400; font-style: italic;
  font-size: 1.0rem; letter-spacing: 0.02em;
  color: var(--ink-soft);
  margin: 1.9rem 0 0.6rem;
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
        elif it[0] == "subsection":
            parts.append(f'    <h3 class="section-subsubtitle">{it[1]}</h3>\n')
        elif it[0] == "quote":
            _, qtext, cite = it
            parts.append('\n    <blockquote class="pull-quote">\n')
            parts.append(f'      <p>{qtext}</p>\n')
            parts.append(f'      <cite class="no-audio">{cite}</cite>\n')
            parts.append('    </blockquote>\n\n')
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
               '<a class="prev" href="accion-humana.html">Acción humana</a>'
               '<a class="idx" href="index.html">Índice</a>'
               '<span></span></nav>')
    out = re.sub(r'<nav class="nav-foot">.*?</nav>',
                 lambda _m: new_nav, out, count=1, flags=re.DOTALL)
    out = out.replace('audio/tres-regimenes.mp3', 'audio/valor.mp3')
    out = out.replace('audio/tres-regimenes.alignment.json',
                      'audio/valor.alignment.json')
    out = out.replace('data-storage-key="tres-regimenes"',
                      'data-storage-key="valor"')
    out = out.replace('</style>', EXTRA_CSS + '</style>', 1)

    open('valor.html', 'w', encoding='utf-8').write(out)
    n_par = sum(1 for it in CONTENT if isinstance(it, str) or (isinstance(it, tuple) and it[0] == "lead"))
    n_sec = sum(1 for it in CONTENT if isinstance(it, tuple) and it[0] == "section")
    n_sub = sum(1 for it in CONTENT if isinstance(it, tuple) and it[0] == "subsection")
    n_q = sum(1 for it in CONTENT if isinstance(it, tuple) and it[0] == "quote")
    print(f"valor.html creado: {n_par} párrafos, {n_sec} secciones (h2), {n_sub} sub-secciones (h3), {n_q} citas")


if __name__ == "__main__":
    main()
