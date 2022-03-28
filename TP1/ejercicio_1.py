# Ejercicio 1 - Uriel Diaz

entrar = 2
materias = [""]
materia_parciales_1 = []
materia_parciales_2 = []
materia_parciales_3 = []
materia_parciales_4 = []
salir = 1
promedios = []
aprobado_o_no = []


while entrar != 0:
    materias.append(input("\nIngrese las materias que esta cursando: "))
    if len(materias) >= 5:
        while entrar > 1:
            if len(materias) == 5:
                for parciales1 in range(3):
                    materia_parciales_1.append(int(input(f"\nIngrese las notas de los parciales de {materias[1]}: ")))
                
                for parciales2 in range(3):
                    materia_parciales_2.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[2]}: ")))
            
                for parciales3 in range(3):
                    materia_parciales_3.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[3]}: "))) 
            
                for parciales4 in range(3):
                    materia_parciales_4.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[4]}: ")))
                
                promedios.append(sum(materia_parciales_1) / 3)
                promedios.append(sum(materia_parciales_2) / 3)
                promedios.append(sum(materia_parciales_3) / 3)
                promedios.append(sum(materia_parciales_4) / 3)

                for promedio in promedios:
                    if promedio >= 8:
                        aprobado_o_no.append(1) #1 = promocionado
                    if promedio >= 6:
                        aprobado_o_no.append(2) #2 = aprobado
                    else:
                        aprobado_o_no.append(3) #3 = desaprobado

                if aprobado_o_no[0] == 1:
                    print(f"{materias[1]} promocionada!")
                elif aprobado_o_no[0] == 2:
                    print(f"{materias[1]} aprobada.")
                else:
                    print(f"{materias[1]} desaprobada.")
                
                if aprobado_o_no[1] == 1:
                    print(f"{materias[2]} promocionada!")
                elif aprobado_o_no[1] == 2:
                    print(f"{materias[2]} aprobada.")
                else:
                    print(f"{materias[2]} desaprobada.")
                
                if aprobado_o_no[2] == 1:
                    print(f"{materias[3]} promocionada!")
                elif aprobado_o_no[2] == 2:
                    print(f"{materias[3]} aprobada.")
                else:
                    print(f"{materias[3]} desaprobada.")

                if aprobado_o_no[3] == 1:
                    print(f"{materias[4]} promocionada!")
                elif aprobado_o_no[3] == 2:
                    print(f"{materias[4]} aprobada.")
                else:
                    print(f"{materias[4]} desaprobada.")
                
                entrar -= 2   
            elif len(materias) == 6:
                materia_parciales_5 = []
                for parciales1 in range(3):
                    materia_parciales_1.append(int(input(f"\nIngrese las notas de los parciales de {materias[1]}: ")))
                
                for parciales2 in range(3):
                    materia_parciales_2.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[2]}: ")))
            
                for parciales3 in range(3):
                    materia_parciales_3.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[3]}: ")))
            
                for parciales4 in range(3):
                    materia_parciales_4.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[4]}: ")))
                
                for parciales5 in range(3):
                    materia_parciales_5.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[5]}: ")))

                promedios.append(sum(materia_parciales_1) / 3)
                promedios.append(sum(materia_parciales_2) / 3)
                promedios.append(sum(materia_parciales_3) / 3)
                promedios.append(sum(materia_parciales_4) / 3)
                promedios.append(sum(materia_parciales_5) / 3)

                for promedio in promedios:
                    if promedio >= 8:
                        aprobado_o_no.append(1) 
                    if promedio >= 6:
                        aprobado_o_no.append(2) 
                    else:
                        aprobado_o_no.append(3) 
                
                if aprobado_o_no[0] == 1:
                    print(f"{materias[1]} promocionada!")
                elif aprobado_o_no[0] == 2:
                    print(f"{materias[1]} aprobada.")
                else:
                    print(f"{materias[1]} desaprobada.")
                
                if aprobado_o_no[1] == 1:
                    print(f"{materias[2]} promocionada!")
                elif aprobado_o_no[1] == 2:
                    print(f"{materias[2]} aprobada.")
                else:
                    print(f"{materias[2]} desaprobada.")
                
                if aprobado_o_no[2] == 1:
                    print(f"{materias[3]} promocionada!")
                elif aprobado_o_no[2] == 2:
                    print(f"{materias[3]} aprobada.")
                else:
                    print(f"{materias[3]} desaprobada.")

                if aprobado_o_no[3] == 1:
                    print(f"{materias[4]} promocionada!")
                elif aprobado_o_no[3] == 2:
                    print(f"{materias[4]} aprobada.")
                else:
                    print(f"{materias[4]} desaprobada.")
                
                if aprobado_o_no[4] == 1:
                    print(f"{materias[5]} promocionada!")
                elif aprobado_o_no[4] == 2:
                    print(f"{materias[5]} aprobada.")
                else:
                    print(f"{materias[5]} desaprobada.")

                entrar -= 2   
            elif len(materias) == 7:
                materia_parciales_5 = []
                materia_parciales_6 = []
                for parciales1 in range(3):
                    materia_parciales_1.append(int(input(f"\nIngrese las notas de los parciales de {materias[1]}: ")))
                
                for parciales2 in range(3):
                    materia_parciales_2.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[2]}: ")))
            
                for parciales3 in range(3):
                    materia_parciales_3.append(int(input(f"\nIngrese las notas de los parciales de {materias[3]}: ")))
            
                for parciales4 in range(3):
                    materia_parciales_4.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[4]}: ")))
                
                for parciales5 in range(3):
                    materia_parciales_5.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[5]}: ")))
                
                for parciales6 in range(3):
                    materia_parciales_6.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[6]}: ")))

                promedios.append(sum(materia_parciales_1) / 3)
                promedios.append(sum(materia_parciales_2) / 3)
                promedios.append(sum(materia_parciales_3) / 3)
                promedios.append(sum(materia_parciales_4) / 3)
                promedios.append(sum(materia_parciales_5) / 3)
                promedios.append(sum(materia_parciales_6) / 3)

                for promedio in promedios:
                    if promedio >= 8:
                        aprobado_o_no.append(1) 
                    if promedio >= 6:
                        aprobado_o_no.append(2) 
                    else:
                        aprobado_o_no.append(3)

                if aprobado_o_no[0] == 1:
                    print(f"{materias[1]} promocionada!")
                elif aprobado_o_no[0] == 2:
                    print(f"{materias[1]} aprobada.")
                else:
                    print(f"{materias[1]} desaprobada.")
                
                if aprobado_o_no[1] == 1:
                    print(f"{materias[2]} promocionada!")
                elif aprobado_o_no[1] == 2:
                    print(f"{materias[2]} aprobada.")
                else:
                    print(f"{materias[2]} desaprobada.")
                
                if aprobado_o_no[2] == 1:
                    print(f"{materias[3]} promocionada!")
                elif aprobado_o_no[2] == 2:
                    print(f"{materias[3]} aprobada.")
                else:
                    print(f"{materias[3]} desaprobada.")

                if aprobado_o_no[3] == 1:
                    print(f"{materias[4]} promocionada!")
                elif aprobado_o_no[3] == 2:
                    print(f"{materias[4]} aprobada.")
                else:
                    print(f"{materias[4]} desaprobada.")

                if aprobado_o_no[4] == 1:
                    print(f"{materias[5]} promocionada!")
                elif aprobado_o_no[4] == 2:
                    print(f"{materias[5]} aprobada.")
                else:
                    print(f"{materias[5]} desaprobada.")
                
                if aprobado_o_no[5] == 1:
                    print(f"{materias[6]} promocionada!")
                elif aprobado_o_no[5] == 2:
                    print(f"{materias[6]} aprobada.")
                else:
                    print(f"{materias[6]} desaprobada.")
                
                entrar -= 2
     
            elif len(materias) == 8:
                materia_parciales_5 = []
                materia_parciales_6 = []
                materia_parciales_7 = []
                for parciales1 in range(3):
                    materia_parciales_1.append(int(input(f"\nIngrese las notas de los parciales de {materias[1]}: ")))
                
                for parciales2 in range(3):
                    materia_parciales_2.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[2]}: ")))
            
                for parciales3 in range(3):
                    materia_parciales_3.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[3]}: ")))
            
                for parciales4 in range(3):
                    materia_parciales_4.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[4]}: ")))
                
                for parciales5 in range(3):
                    materia_parciales_5.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[5]}: ")))
                
                for parciales6 in range(3):
                    materia_parciales_6.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[6]}: ")))
                
                for parciales7 in range(3):
                    materia_parciales_7.append(int(input(f"\nahora, ingrese las notas de los parciales de {materias[7]}: ")))
                
                promedios.append(sum(materia_parciales_1) / 3)
                promedios.append(sum(materia_parciales_2) / 3)
                promedios.append(sum(materia_parciales_3) / 3)
                promedios.append(sum(materia_parciales_4) / 3)
                promedios.append(sum(materia_parciales_5) / 3)
                promedios.append(sum(materia_parciales_6) / 3)
                promedios.append(sum(materia_parciales_7) / 3)

                for promedio in promedios:
                    if promedio >= 8:
                        aprobado_o_no.append(1) 
                    if promedio >= 6:
                        aprobado_o_no.append(2) 
                    else:
                        aprobado_o_no.append(3)

                if aprobado_o_no[0] == 1:
                    print(f"{materias[1]} promocionada!")
                elif aprobado_o_no[0] == 2:
                    print(f"{materias[1]} aprobada.")
                else:
                    print(f"{materias[1]} desaprobada.")
                
                if aprobado_o_no[1] == 1:
                    print(f"{materias[2]} promocionada!")
                elif aprobado_o_no[1] == 2:
                    print(f"{materias[2]} aprobada.")
                else:
                    print(f"{materias[2]} desaprobada.")
                
                if aprobado_o_no[2] == 1:
                    print(f"{materias[3]} promocionada!")
                elif aprobado_o_no[2] == 2:
                    print(f"{materias[3]} aprobada.")
                else:
                    print(f"{materias[3]} desaprobada.")

                if aprobado_o_no[3] == 1:
                    print(f"{materias[4]} promocionada!")
                elif aprobado_o_no[3] == 2:
                    print(f"{materias[4]} aprobada.")
                else:
                    print(f"{materias[4]} desaprobada.")

                if aprobado_o_no[4] == 1:
                    print(f"{materias[5]} promocionada!")
                elif aprobado_o_no[4] == 2:
                    print(f"{materias[5]} aprobada.")
                else:
                    print(f"{materias[5]} desaprobada.")
                
                if aprobado_o_no[5] == 1:
                    print(f"{materias[6]} promocionada!")
                elif aprobado_o_no[5] == 2:
                    print(f"{materias[6]} aprobada.")
                else:
                    print(f"{materias[6]} desaprobada.")
                
                if aprobado_o_no[6] == 1:
                    print(f"{materias[7]} promocionada!")
                elif aprobado_o_no[6] == 2:
                    print(f"{materias[7]} aprobada.")
                else:
                    print(f"{materias[7]} desaprobada.")
    
                entrar -= 2
            

    

                    

            
    
