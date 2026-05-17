# Procedimiento - paquete base para Power Automate

Este directorio contiene un **paquete base** con la definición del flujo pedido:

1. Trigger: cuando se crea o modifica un archivo en SharePoint.
2. Busca un registro en una lista de SharePoint.
3. Envía aprobación al **revisor**.
4. Si aprueba, envía aprobación al **aprobador**.
5. Si aprueba, crea el archivo en la carpeta final de SharePoint.
6. Si falta configuración o alguien rechaza, envía un mail de aviso.

## Archivos

- `manifest.json` → metadata del paquete
- `connections.json` → referencias de conexión a remapear al importar
- `Microsoft.Flow/flows/<flow-id>/definition.json` → definición del flujo
- `Procedimiento-import.zip` → zip listo para intentar importar

## Placeholders que tenés que completar en Power Automate

- `__SHAREPOINT_SITE_URL__`
- `__SOURCE_LIBRARY__`
- `__SOURCE_FOLDER__`
- `__CONFIG_LIST_NAME__`
- `__FILTER_QUERY__`
- `__REVIEWER_FIELD_INTERNAL_NAME__`
- `__APPROVER_FIELD_INTERNAL_NAME__`
- `__DESTINATION_PATH_FIELD_INTERNAL_NAME__`
- `__NOTIFICATION_EMAIL__`

## Notas importantes

- El paquete está preparado como **base editable/importable**. Puede requerir que Power Automate te pida remapear conexiones y revisar algunas acciones en el diseñador.
- La parte más sensible es el `configFilterQuery`, porque depende de cómo relacionás el archivo con la fila de la lista.
- Si en vez de **copiar** querés **mover** el archivo, cambiá la acción `Create_file_in_destination` por `Move file` desde el diseñador.
