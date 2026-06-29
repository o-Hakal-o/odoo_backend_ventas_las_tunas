FROM odoo:18.0

# Cambiamos a root temporalmente para modificar permisos
USER root

# Le asignamos la terminal bash al usuario odoo
RUN sed -i 's|/usr/sbin/nologin|/bin/bash|g' /etc/passwd

# Volvemos al usuario odoo por seguridad
USER odoo