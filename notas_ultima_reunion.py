- Usar funciones auxiliares para generar los boards al correr los tests, no generarlos en el setup. Solo llamar los metodos en los tests que necesito
- De put_chip() eliminar el raise_if_board_is_full() porque pasa a ser redundante con el raise column_is_full (esta operacion debe ser muy rapida)
- Eliminar los tickets que ya fueron cubiertos en otros PR
- El limite de 25ms es muy pequenho, vamos a llevarlo a 500ms (aprox) por turno
- improve_wins_in_diagonal es de baja prioridad
