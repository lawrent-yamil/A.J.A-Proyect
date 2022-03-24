def mostrar_informacion(areaT,sueldo):
    if areaT == "P":
        print(f"""
            Su area de trabajo es: {areaT}
            Su sueldo es: {sueldo} x 6hrs cada dia
            Usted gana por dia: {(sueldo*6) * 0.3} (monto de 30% aplicado)
            Usted gana Semanalmente: {(sueldo*30) * 0.3} (monto de 30% aplicado)
            Usted gana quincenalmente: {(sueldo*90) * 0.3} (monto de 30% aplicado)
            Usted gana Mensualmente: {(sueldo*180) * 0.3} (monto de 30% aplicado)
            Usted gana Anualmente: {(sueldo*2190) * 0.3} (monto de 30% aplicado)
        """)
    elif areaT == "G":
        print(f"""
            Su area de trabajo es: {areaT}
            Su sueldo es: {sueldo} x 6hrs cada dia
            Usted gana por dia: {(sueldo*6) * 0.3} (monto de 30% aplicado)
            Usted gana Semanalmente: {(sueldo*30) * 0.3} (monto de 30% aplicado)
            Usted gana quincenalmente: {(sueldo*90) * 0.3} (monto de 30% aplicado)
            Usted gana Mensualmente: {(sueldo*180) * 0.3} (monto de 30% aplicado)
            Usted gana Anualmente: {(sueldo*2190) * 0.3} (monto de 30% aplicado)
        """)
    else:
        print(f"""
            Su area de trabajo es: {areaT}
            Su sueldo es: {sueldo} x 8hrs cada dia
            Usted gana por dia: {(sueldo*8) * 0.3} (monto de 30% aplicado)
            Usted gana Semanalmente: {(sueldo*40) * 0.3} (monto de 30% aplicado)
            Usted gana quincenalmente: {(sueldo*120) * 0.3} (monto de 30% aplicado)
            Usted gana Mensualmente: {(sueldo*240) * 0.3} (monto de 30% aplicado)
            Usted gana Anualmente: {(sueldo*2920) * 0.3} (monto de 30% aplicado)
        """)