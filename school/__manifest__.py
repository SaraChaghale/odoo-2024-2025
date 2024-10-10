# -*- coding: utf-8 -*-
{
    'name': "School Module",

    'summary': "Gestión de escuelas y estudiantes",

    'description': """
        Módulo para gestionar escuelas, estudiantes y sus datos relacionados.
        Permite crear, editar y eliminar registros de escuelas y estudiantes,
        así como generar reportes y análisis sobre el rendimiento académico.
    """,

    'author': "Mi Empresa",
    'website': "https://www.tuempresa.com",

    # Categoría del módulo para facilitar su búsqueda en Odoo
    # Consulta la lista completa en:
    # https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    'category': 'Uncategorized',
    'version': '0.1',

    # Dependencias necesarias para que el módulo funcione correctamente
    'depends': ['base'],

    # Archivos de datos que se cargan siempre al instalar el módulo
    'data': [
        'security/ir.model.access.csv',  # Reglas de acceso a modelos
        #'views/School_views.xml',        # Vistas para el modelo School
       # 'views/Student_views.xml',       # Vistas para el modelo Student
        'views/views.xml',
        'views/templates.xml',           # Plantillas (si aplica)
        # Añade otros archivos de datos si es necesario
    ],

    # Archivos que solo se cargan en modo de demostración
    'demo': [
        'demo/demo.xml',
    ],

    # Define si el módulo es instalable
    'installable': True,

    # Define si el módulo es una aplicación completa
    'application': True,

    # Define si el módulo se instala automáticamente si se cumplen las dependencias
    'auto_install': False,

    # Especifica la licencia del módulo
    'license': 'LGPL-3',
}

