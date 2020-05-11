from pymongo import MongoClient

client = MongoClient('localhost')

database = client['ChatBot_DB']
col_respuestas = database['Datos']
col_Saludos = database['Saludos']


col_Saludos.insert_one({"id":"0", "nombre": "saludo", "patrones": ["hola", "como estas", "buenos dias"], "respuestas": ["Hola", "Gracias por venir", "Buenos días!"], "Contexto":""})


col_respuestas.insert_many([
    {
         "id": "1",

         "Respuesta_1": "Hola!."
    },

    {
         "id": "2",

         "Respuesta_2": " La evangelización de la cultura es una tarea misional de la UPB, es decir, que todos sus modos de relación están inspirados por su identidad católica, que asume  a Jesucristo como el modelo de toda transformación humana y social."
    },

    {
         "id": "3",

         "Respuesta_3": " La evangelización tiene la responsabilidad de cuidar y tutelar la vida humana de cada persona que la constituye."
    },

    {
        "id": "4",

        "Respuesta_4": " Bolivarianitos con Jesús es un espacio de formación destinado a niños entre los 7 y los 12 años, hijos de nuestros empleados; el objetivo es brindar a los pequeñosun espacio de formación en la fe y el conocimiento de la persona de Jesús, mediante jornadas de formación que se realizan los sábados en la mañana, una vez por mes. "
    },

    {
        "id": "5",

        "Respuesta_5": " La caminata familiar es un espacio pensado para el fortalecimiento de las relaciones personales con la comunidad universitaria y sus familias."
    },

    {
        "id": "6",

        "Respuesta_6": " A través de la Catequesis la Iglesia cumple con el ciclo de maduración en la fe correspondiente a la iniciación cristiana, es decir los sacramentos del bautismo, primera comunión y confirmación."
    },

    {
        "id": "7",

        "Respuesta_7": " Las convivencias son espacios destinados al desarrollo personal y colectivo de los miembros de la comunidad universitaria, que buscan compartir y reflexionar ciertas temáticas de interés, e invitan al participante a encontrarse consigo mismo a la luz de las enseñanzas de vida del evangelio como guía de la dimensión personal, espiritual y social de los cristianos."
    },

    {
        "id": "8",

        "Respuesta_8": " Las convivencias se realizan como parte de la acción pastoral que tienden a fomentar el crecimiento espiritual y personal de los miembros de la comunidad universitaria, a través de espacios reflexivos, de diálogo, oración y recreación, para el fortalecimiento de la persona en sus diferentes dimensiones como ser humano."
    },

    {
        "id": "9",

        "Respuesta_9": " La dimensión espiritual en el transcurrir diario de la universidad, teniendo en cuenta que el ser humano tiene su dimensión espiritual, la institución nos ofrece momentos en los cuales las personas, puedan celebrar y cultivar su encuentro con Dios, especialmente en la celebración Eucarística, el sacramento de la reconciliación, el acompañamiento y dirección espiritual con lo que buscamos alimentar y fortalecer la fe de los miembros de la comunidad universitaria."
    },

    {
        "id": "10",

        "Respuesta_10": " Celebrar diariamente la eucaristía por dependencias, y con disposición para que en cualquier momento que se requiera, ser partícipes en las diferentes actividades de la universidad en donde se pidan los servicios pastorales."
    },

    {
        "id": "11",

        "Respuesta_11": " Nuestra Iglesia favorece y orienta la religiosidad popular y la piedad de las personas, por tal motivo la UPB Seccional Bucaramanga, nos ofrece espacios determinados para cultivar y celebrar momentos que motiven el encuentro con Dios, alimentando nuestra fe y elevando el espíritu y la vida dentro de nuestro ambiente universitario y por fuera de él."
    },

    {
        "id": "12",

        "Respuesta_12": " Cultivamos el respeto y la orientación de la religiosidad popular de los miembros de la comunidad universitaria, para enriquecernos y construir experiencias de fe, que van madurando y consolidando nuestra identidad cristiana, dentro de un contexto sociocultural."
    },

    {
        "id": "13",

        "Respuesta_13": " La evangelización es una jornada que se desarrolla con el ánimo de promover el criterio y sentido de la paz en la comunidad universitaria desde la acción y la visión pastoral, dado que los continuos cambios con que vive el mundo actual y la necesidad de ser constructores de paz, requieren espacios que, desde la academia, nos permitan reflexionar sobre el sentido de la paz y la manera para alcanzarla, iluminados por el sentir de iglesia y las enseñanzas del evangelio."
    },

    {
        "id": "14",

        "Respuesta_14": " A través de conferencias, exposiciones, actividades lúdicas, entre otras, la comunidad universitaria expresa su sentir, experiencias y expectativas de paz, así como también se compromete a vivir y realizar acciones promotoras de una sociedad más pacífica."
    },

    {
        "id": "15",

        "Respuesta_15": " Líderes UPB es un programa que busca capacitar y formar voluntaria y gratuitamente a los jóvenes universitarios en temas como la proyección solidaria, el trabajo en equipo, el liderazgo, la comunicación asertiva, el voluntariado, entre otros."
    },

    {
        "id": "16",

        "Respuesta_16": " El líder Bolivariano es una persona profundamente respetuosa y con un alto sentido espiritual."
    },

    {
        "id": "17",

        "Respuesta_17": " Características del Líder UPB: Cultiva la armonía de su ser físico, biológico, afectivo e intelectual; Es firme en sus convicciones y en su vida espiritual."
    },

    {
        "id": "18",

        "Respuesta_18": " Característica del Líder UPB: compromiso con la paz y el desarrollo del país; Búsqueda de la verdad y el conocimiento; La creatividad e innovación; La honradez; La justicia; La lealtad; La solidaridad; Reconocimiento y respeto por cada una de las personas sin discriminación alguna."
    },

    {
        "id": "19",

        "Respuesta_19": " Si quieres hacer parte del programa Líderes UPB, ponte en contacto con nosotros: lideres.bucaramanga@upb.edu.co."
    },

    {
        "id": "20",

        "Respuesta_20": " En Líderes UPB buscames hacer parte del apoyo a las actividades institucionales y de proyección social, en diferentes proyectos dentro y fuera de la Universidad."
    },

    {
        "id": "21",

        "Respuesta_21": " Los Líderes UPB están compuesto por estudiantes,  personal administrativo y docentes de la Universidad, que destinan parte de su tiempo para adelantar procesos de formación en comunidades vulnerables durante ciertas épocas del año."
    },

    {
        "id": "22",

        "Respuesta_22": " Los misioneros llevan a cabo un proceso de formación integral y preparación para las actividades que realizan, construyendo paso a paso sus bases humanas, cristianas y axiológicas."
    },

    {
        "id": "23",

        "Respuesta_23": " El Papa Francisco en la carta encíclica Lumen Fidei, presenta a la familia como el primer ámbito iluminado por la fe, esto motiva para que en la vida universitaria se disponga de un retiro familiar, que desde nuestra realidad surge un espacio en el año para que la comunidad educativa asistan con sus familias fuera de la ciudad."
    },

    {
        "id": "24",

        "Respuesta_24": " Retiro familiar es un ejercicio, un camino, como el de los discípulos de Emaús, que mientras caminan y escuchan a Jesús  va ardiendo su corazón y de éste modo son capacitados para reconocer la presencia viva del Resucitado Como fruto de la oración personal de cada miembro de la familia en este espacio de recogimiento."
    },

    {
        "id": "25",

        "Respuesta_25": " Retiros espirituales son espacios para animar y cultivar la fe de los miembros de la comunidad universitaria."
    },

    {
        "id": "26",

        "Respuesta_26": " En las actividades de los retiros espirituales, está la predicación sobre temas específicos inspirados en la Palabra de Dios, espacios para la reflexión, oración y se termina la jornada con la celebración Eucarística."
    },

    {
        "id": "27",

        "Respuesta_27": " La vicerrectoría pastoral es el departamento de la universidad que se encarga de realizar acciones solidarias y potenciar las capacidades, los conocimientos y los activos estratégicos de la Institución para contribuir a la generación de impactos en  el desarrollo social y humano"
    },
    
    {
         "id": "28",

         "Respuesta_28": " Con el propósito de comprenderlo todo y con la intención de no dejar a nadie por fuera, mediante el testimonio de la comunidad creyente que se ofrece a toda persona sin coartar su libertad, dado que la Universidad Pontificia Bolivariana como depositaria de la tradición cristiana revelada, afirma que el que sigue a Cristo."
    },
     
    {
         "id": "29",

         "Respuesta_29": " Hombre perfecto, se perfecciona cada vez más en su propia dignidad de hombre La evangelización es el proceso permanente de humanización que ilumina el modelo pedagógico de la Universidad."
    },
     
    {
         "id": "30",

         "Respuesta_30": " "
    },
     
    {
         "id": "31",

         "Respuesta_31": " La vicerrectoría pastoral se encarga de la espiritualidad en la universidad, gracias a esta área la universidad tiene el título de “Universidad Pontificia”, ya que sobresale tanto por sus cualidades como universalidad, como por la calidad de su identidad y testimonio católicos"
    },
     
    {
         "id": "32",

         "Respuesta_32": " Guiados por la historia del pueblo de Israel, la caminata familiar tiene un significado simbólico referente al recorrido realizado hacia la tierra prometida."
    },
     
    {
         "id": "33",

         "Respuesta_33": " A lo largo de las caminatas familiares existen rutas planificadas para la actividad, fortalecemos nuestros lazos de fraternidad, comunión y cariño con los miembros de la familia UPB, lo que nos permite orientarnos hacia la construcción de una mejor universidad, guiada por el don de la fe y el deseo de una comunión de vida y amor."
    },
     
 
    {
         "id": "34",

         "Respuesta_34": " Dicha catequesis abre un camino para que el catequizando tenga siempre en su conciencia y en su corazón que está lleno del Espíritu Santo, todo esto se logra mediante el proceso de preparación para recibir el sacramento que es conferido por el Obispo después de haber asimilado y reflexionado los temas concretos y concernientes al sacramento."
    },
     
    {
         "id": "35",

         "Respuesta_35": " A lo largo del semestre se brinda la catequesis al grupo de jóvenes que quieren conscientemente prepararse para recibir el sacramento de la confirmación y sus implicaciones tanto personales, eclesiales y su proyección como cristiano en la sociedad."
    },
     
    {
         "id": "36",

         "Respuesta_36": " Al preparar al joven para el sacramento de la confirmación desea que de forma consciente asimile los contenidos que se le brindarán mediante las catequesis, despertando en él su compromiso y su identidad cristiana como miembro de la Iglesia y del pueblo de Dios."
    },
     
    {
         "id": "37",

         "Respuesta_37": " La vicerrectoría pastoral pretende construir la identidad, como institución educativa confesional que acompañe y facilite los momentos celebrativos de los miembros de la UPB Seccional Bucaramanga."
    },
     
    {
         "id": "38",

         "Respuesta_38": " En la vicerrectoría pastoral hecemos posible el acompañamiento y escucha de las personas en su búsqueda de orientación espiritual."
    },
     
    {
         "id": "39",

         "Respuesta_39": " Atender y ayudar en los procesos de arrepentimiento y conversión, de quienes busquen el sacramento de la reconciliación Fortalecimiento de la fe."
    },
     
    {
         "id": "40",

         "Respuesta_40": " Para ello realiza actividades en tiempos litúrgicos y de religiosidad popular como es la oración del santo rosario, novenas a las diferentes advocaciones, viacrucis, corpus cristis y acompañamiento de la fe."
    }, 
     
    {
         "id": "41",

         "Respuesta_41": " Resaltando los tiempos litúrgicos con sus connotaciones propias, que nos ayuden a las personas a contemplar la riqueza litúrgica y espiritual, que la iglesia presenta como instrumentos celebrativos de la fe, encuentros de catequesis, reflexiones, y demás oraciones en las cuales los creyentes, con humildad hacen de su fe, una entrega noble de corazón a Dios."
    },
     
    {
         "id": "42",

         "Respuesta_42": " Con un énfasis particular en el momento de transición que vive nuestro país, la Universidad busca fortalecer los espacios de reflexión y debate con el ánimo de generar un compromiso serio, tanto institucional, como individual para concretizar acciones que propendan por la construcción de escenarios de paz dentro y fuera de la Institución."
    },
     
    {
         "id": "43",

         "Respuesta_43": " Demuestra en la práctica sus valores y se hace protagonista y responsable de la sociedad."
    },
     
    {
         "id": "44",

         "Respuesta_44": " Su excelente formación lo impulsa a actuar con iniciativa propia y con una responsabilidad tal, que sus actos públicos y privados son ejemplo de un pensamiento innovador, honesto y crítico frente a las situaciones que vive."
    },
     
    {
         "id": "45",

         "Respuesta_45": " Su espíritu proactivo y su convicción en actos y palabras, le dan credibilidad ante quienes toma la vocería. Es ante todo un Ser Humano Integro."
    },
     
    {
         "id": "46",

         "Respuesta_46": " Es firme en sus convicciones y en su vida espiritual. Encuentra en Jesús el fundamento de su vida, de sus valores y actitudes."
    },
     
    {
         "id": "47",

         "Respuesta_47": " Es comprometido con la Iglesia, leal a la patria y servidor de la humanidad."
    },
     
    {
         "id": "48",

         "Respuesta_48": " Es responsable, honesto y ético. Cultiva en él y en quienes le siguen los conocimientos y cualidades."
    },
     
    {
         "id": "49",

         "Respuesta_49": " Defiende la vida y la familia. Es solidario con los más necesitados, es justo y pacífico. Es visionario y realista, creativo y decidido, exigente y flexible. Su testimonio y su acción generan cambio y perduran en el tiempo."
    },
     
    {
         "id": "50",

         "Respuesta_50": " Charlas participativas sobre temas alusivos a la formación integral, para cultivar el ser en todas las dimensiones humanas; entre ellos: liderazgo, autoestima, trabajo en equipo, servicio, voluntariado, coaching, espiritualidad de las profesiones."
    },
     
    {
         "id": "51",

         "Respuesta_51": " Talleres en los que se abordan herramientas necesarias para que el líder de hoy se enfrente a los distintos escenarios, situaciones y retos que el mundo actual le presenta."
    },
     
    {
         "id": "52",

         "Respuesta_52": " Talleres para la resolución de conflictos, la expresión oral, teoría en emprenderismo y humanismo cristiano, elementos y formulación de proyectos, carisma y poder de liderazgo y todos aquellos temas afines con la formación integral de la persona."
    },
     
    {
         "id": "53",

         "Respuesta_53": " Encuentro Nacional de Líderes UPB: evento anual en el que los líderes UPB, de ámbito nacional, comparten temas y reflexiones."
    },
     
    {
         "id": "54",

         "Respuesta_54": " Dentro del quehacer de los misioneros se encuentra la realización de campañas de solidaridad, de formación cristiana; misiones a municipios, veredas, barrio de la ciudad;  apoyo a las actividades de pastoral, evangelización y anuncio de la palabra de Dios a través del acompañamiento y la interacción con toda la comunidad."
    },
     
    {
         "id": "55",

         "Respuesta_55": " La filosofía del grupo de los misioneros tiene como base fundamental el humanismo cristiano y la pedagogía de Jesús, lo que motiva a nuestros líderes a entregarse al prójimo como parte de su experiencia universitaria."
    },
     
    {
         "id": "56",

         "Respuesta_56": " Para el grupo de las misiones es muy importante el fortalecimiento de la amistad desde un enfoque Cristocéntrico, la vivencia del amor por el evangelio y la sensibilización de la realidad socioeconómica de nuestro entorno, resaltando además, la importancia de la oración y el agradar a Dios por medio del diario vivir."
    }, 
     
    {
         "id": "57",

         "Respuesta_57": " En el grupo de los misioneros puedes tener un ambiente apropiado para este encuentro con la persona en Cristo."
    },
     
    {
         "id": "58",

         "Respuesta_58": " La eucaristía proporciona un spacio propicio para descubrir que la lectura y la meditación de la palabra de Dios nos permiten encontrarnos personalmente, de manera viva, con Jesús y dejarnos guiar y transformar por  Él."
    },
     
    {
         "id": "59",

         "Respuesta_59": " La palabra de Dios interiorizada y aplicada a nuestra vida nos lleva a la conversión, al amor y al seguimiento del Señor."
    },
     
    {
         "id": "60",

         "Respuesta_60": " Con la palabra se puede entrar en un diálogo para pensar la realidad, tratar varios casos de la vida familiar, social, política, económica y demás temas que pueden se tratados e iluminados por la palabra y a partir de ahí generar una enseñanza para aplicar en la vida individual, familiar y cotidiana."
    },
     
    {
         "id": "61",

         "Respuesta_61": " El primer retiro al finalizar la cuaresma, preparándolos para la celebración del Triduo Pascual y el segundo al finalizar el año, proyectándonos hacia un encuentro con Cristo y revisión de sus vidas, generando espacios que les ayuden en su crecimiento como miembros de la Institución y como personas de fe en la Iglesia."
    },
     
    {
         "id": "62",

         "Respuesta_62": " El fortalecimiento de la vida espiritual y el don de la fe de los miembros de nuestra comunidad universitaria para elevar las cualidades humanas y despertar los carismas que hay en cada persona que nos permitan sentirnos seguros en nuestra opción como creyentes y comprometidos como participés bautizados y miembros de la Iglesia."
    },
     
    {
         "id": "63",

         "Respuesta_63": " Se encarga de realizar acciones solidarias y potenciar las capacidades, los conocimientos y los activos estratégicos de la Institución para contribuir a la generación de impactos en  el desarrollo social y humano."
    },
     
    {
         "id": "64",

         "Respuesta_64": " Celebraciones Eucarísticas, Retiros Espirituales, Grupo Pastoral Universitaria, Evangelización, Confesiones y asesorías espirituales Proceso de evangelización, proceso de proyección solidaria, proceso bienestar institucional, proceso extensión universitaria, proceso egresados."
    },
     
    {
         "id": "65",

         "Respuesta_65": "  la vicerrectoría pastoral es la encargada de la espiritualidad en la universidad, gracias a esta área la universidad tiene el título de Universidad Pontificia, ya que sobresale tanto por sus cualidades como universalidad, como por la calidad de su identidad y testimonio católicos."
    },
    {
         "id": "66",

         "Respuesta_66": " El grupo pastoral universitaria es conformado por la comunidad estudiantil, donde se trabaja desde dos pilares: formación y evangelización."
    },    
    {
         "id": "67",

         "Respuesta_67": " Dentro de los procesos de la vicerrectoría pastoral se encuentran: proceso de evangelización, proceso de proyección solidaria, proceso bienestar institucional, proceso extensión universitaria, proceso egresados."
    }, 
    {
         "id": "68",

         "Respuesta_68": " Las herramientas de la vicerrectoríapastoral son: Celebraciones Eucarísticas, Retiros Espirituales, Grupo Pastoral Universitaria, Evangelización, Confesiones y asesorías espirituales."
    },
     {
         "id": "69",

         "Respuesta_69": " Las actividades de la vicerrectoría pastoral son: Bolivarianitos con Jesús, caminata familiar, catequesis, convivencias, dimensión espiritual, fortalecimiento de la fe, jornada por la paz, programa de formación de líderes UPB, misiones, retiros familiares, retiros espirituales."
    },
     {
         "id": "70",

         "Respuesta_70": " A través de la Catequesis la Iglesia cumple con el ciclo de maduración en la fe correspondiente a la iniciación cristiana, es decir los sacramentos del bautismo, primera comunión y confirmación; a lo largo del semestre se brinda la catequesis al grupo de jóvenes que quieren conscientemente prepararse para recibir el sacramento de la confirmación y sus implicaciones tanto personales, eclesiales y su proyección como cristiano en la sociedad."
    },
])
print("Guardado.")

#@author: Santiago Guevara

